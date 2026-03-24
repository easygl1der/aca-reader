from __future__ import annotations

import os
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from ..segment import Segment

Mode = Literal["noop", "openai", "qwen", "assemblyai"]


@dataclass(frozen=True, slots=True)
class TranscribeResult:
    segments: list[Segment]
    raw: Any | None = None


class TranscribeAgent:
    def __init__(
        self,
        *,
        mode: Mode = "qwen",
        model: str = "qwen3-asr-flash",
        api_key: str | None = None,
    ) -> None:
        self._mode = mode
        self._model = model
        self._api_key = api_key

    def transcribe(self, audio_path: str) -> TranscribeResult:
        if self._mode == "noop":
            return TranscribeResult(segments=[], raw=None)
        elif self._mode == "qwen":
            return self._transcribe_qwen(audio_path)
        elif self._mode == "assemblyai":
            return self._transcribe_assemblyai(audio_path)
        else:
            return self._transcribe_openai(audio_path)

    def _transcribe_qwen(self, audio_path: str) -> TranscribeResult:
        import dashscope

        api_key = self._api_key or os.environ.get("DASHSCOPE_API_KEY")
        if not api_key:
            raise RuntimeError("Missing DASHSCOPE_API_KEY")

        dashscope.api_key = api_key

        # Convert to wav if needed
        wav_path = self._ensure_wav(audio_path)

        try:
            text = self._call_asr(wav_path)
        finally:
            if wav_path != audio_path and Path(wav_path).exists():
                Path(wav_path).unlink()

        # Create a single segment for the audio
        if text.strip():
            from ..chunker import probe_duration_ms
            duration_ms = probe_duration_ms(audio_path)
            segments = [Segment(start_ms=0, end_ms=duration_ms, text=text.strip())]
        else:
            segments = []

        return TranscribeResult(segments=segments, raw={"text": text})

    def _ensure_wav(self, audio_path: str) -> str:
        """Convert audio to wav format if needed."""
        path = Path(audio_path)
        if path.suffix.lower() == ".wav":
            return audio_path

        wav_path = path.with_suffix(".wav")
        cmd = [
            "ffmpeg", "-y", "-v", "error",
            "-i", str(path),
            "-ar", "16000", "-ac", "1",
            str(wav_path)
        ]
        subprocess.run(cmd, check=True)
        return str(wav_path)

    def _call_asr(self, wav_path: str) -> str:
        """Call Qwen ASR API."""
        from dashscope import MultiModalConversation

        messages = [
            {"role": "system", "content": [{"text": ""}]},
            {"role": "user", "content": [{"audio": wav_path}]}
        ]

        response = MultiModalConversation.call(
            model=self._model,
            messages=messages,
            result_format="message",
            asr_options={"language": "zh", "enable_itn": True}
        )

        if response.status_code != 200:
            raise RuntimeError(f"ASR failed: {response.message}")

        choice = response.output.choices[0]
        content = choice.message.content[0]
        return content.get("text", "")

    def _transcribe_openai(self, audio_path: str) -> TranscribeResult:
        api_key = self._api_key or os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("Missing OPENAI_API_KEY")

        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        with open(audio_path, "rb") as f:
            resp = client.audio.transcriptions.create(
                model="whisper-1",
                file=f,
                response_format="verbose_json",
                timestamp_granularities=["segment"],
            )

        segments: list[Segment] = []
        for seg in getattr(resp, "segments", []) or []:
            start_s = getattr(seg, "start", None)
            end_s = getattr(seg, "end", None)
            text = getattr(seg, "text", "") or ""
            if start_s is None or end_s is None:
                continue
            segments.append(Segment(
                start_ms=int(round(float(start_s) * 1000)),
                end_ms=int(round(float(end_s) * 1000)),
                text=" ".join(str(text).split()),
            ))

        return TranscribeResult(segments=segments, raw=resp)

    def _transcribe_assemblyai(self, audio_path: str) -> TranscribeResult:
        api_key = self._api_key or os.environ.get("ASSEMBLYAI_API_KEY")
        if not api_key:
            raise RuntimeError("Missing ASSEMBLYAI_API_KEY")

        from assemblyai import Transcriber, TranscriptionConfig, SpeechModel

        # Configure transcription
        config = TranscriptionConfig(
            language_code="zh",
            punctuate=True,
            format_text=True,
            speech_models=[SpeechModel.universal],
        )

        # Transcribe audio
        transcriber = Transcriber()
        transcript = transcriber.transcribe(audio_path, config)

        # Wait for completion
        if transcript.status != "completed":
            raise RuntimeError(f"Transcription failed: {transcript.status}")

        # Parse words with timestamps
        segments: list[Segment] = []
        words = transcript.words or []

        if words:
            # Group words into segments based on pauses (gaps > 1000ms)
            current_segment_words: list[str] = []
            current_start_ms: int | None = None
            current_end_ms: int = 0

            for i, word in enumerate(words):
                word_text = word.text or ""
                word_start = word.start if word.start else 0
                word_end = word.end if word.end else 0

                if not word_text.strip():
                    continue

                # Check for pause between words
                if current_start_ms is not None and current_end_ms > 0:
                    pause_ms = word_start - current_end_ms
                    if pause_ms > 1000:  # > 1 second pause = new segment
                        # Save current segment
                        if current_segment_words:
                            segments.append(Segment(
                                start_ms=current_start_ms,
                                end_ms=current_end_ms,
                                text=" ".join(current_segment_words),
                            ))
                        # Start new segment
                        current_segment_words = []
                        current_start_ms = None

                if current_start_ms is None:
                    current_start_ms = word_start

                current_segment_words.append(word_text)
                current_end_ms = word_end

            # Add final segment
            if current_segment_words and current_start_ms is not None:
                segments.append(Segment(
                    start_ms=current_start_ms,
                    end_ms=current_end_ms,
                    text=" ".join(current_segment_words),
                ))

        return TranscribeResult(segments=segments, raw=transcript)
