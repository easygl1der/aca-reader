#!/usr/bin/env python3
"""
Gemini Video Understanding - Video Analysis Script
使用 Google Gemini API 分析视频内容
"""

import os
import sys
import argparse
import json
import time
from pathlib import Path

# Try to import google.genai
try:
    from google import genai
    from google.genai import types
except ImportError:
    print("❌ 请先安装 google-genai: pip install google-genai")
    sys.exit(1)


def get_api_key():
    """Get API key from various sources"""
    # 1. Environment variable
    api_key = os.environ.get('GEMINI_API_KEY')
    if api_key:
        return api_key

    # 2. Check .env files
    locations = [
        Path(__file__).parent / '.env',
        Path('.env'),
        Path.home / '.claude' / '.env',
    ]

    for env_file in locations:
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    if line.startswith('GEMINI_API_KEY='):
                        return line.split('=', 1)[1].strip()

    return None


def get_available_models():
    """Return dictionary of available models with descriptions"""
    return {
        # Gemini 3.1 Series (Latest)
        "gemini-3.1-pro": "Latest flagship model, best reasoning, 2M context",
        "gemini-3.1-flash": "Latest flash model, high performance, 2M context",
        "gemini-3.1-flash-preview": "Preview features, 2M context",

        # Gemini 2.5 Series
        "gemini-2.5-pro": "Best quality, 1M context",
        "gemini-2.5-flash": "Balanced quality/speed, 1M context",
        "gemini-2.5-flash-preview-05-20": "Latest preview, 1M context",
        "gemini-2.5-flash-preview-09-2025": "Older preview, 1M context",

        # Gemini 2.0 Series
        "gemini-2.0-flash-exp": "Experimental fast model",
        "gemini-2.0-flash": "Fast processing",
        "gemini-2.0-flash-lite": "Lightweight option",

        # Legacy Models
        "gemini-1.5-pro": "Stable, 1M context",
        "gemini-1.5-flash": "Lightweight, 1M context",
    }


def list_models():
    """Print available models"""
    models = get_available_models()
    print("\n📋 Available Gemini Models for Video Understanding:")
    print("=" * 60)

    # Group by series
    series = {
        "Gemini 3.1 Series (Latest)": ["gemini-3.1-pro", "gemini-3.1-flash", "gemini-3.1-flash-preview"],
        "Gemini 2.5 Series": ["gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.5-flash-preview-05-20", "gemini-2.5-flash-preview-09-2025"],
        "Gemini 2.0 Series": ["gemini-2.0-flash-exp", "gemini-2.0-flash", "gemini-2.0-flash-lite"],
        "Legacy Models": ["gemini-1.5-pro", "gemini-1.5-flash"],
    }

    for series_name, model_names in series.items():
        print(f"\n🔹 {series_name}:")
        for model in model_names:
            desc = models.get(model, "")
            print(f"   • {model}")
            if desc:
                print(f"     └─ {desc}")

    print("\n" + "=" * 60)
    print("💡 Usage: --model <model-name>")
    print(f"📌 Default: gemini-2.5-flash")
    print()


def upload_file(client, file_path: str, verbose: bool = False):
    """Upload video file to Gemini API"""
    if verbose:
        print(f"📤 Uploading file: {file_path}")

    try:
        file = client.files.upload(file=file_path)
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return None

    # Poll for file processing
    if verbose:
        print(f"⏳ File state: {file.state.name}")

    while file.state.name == "PROCESSING":
        time.sleep(2)
        file = client.files.get(name=file.name)
        if verbose:
            print(f"   State: {file.state.name}")

    if file.state.name != "ACTIVE":
        print(f"❌ File not active: {file.state.name}")
        return None

    if verbose:
        print(f"✅ File uploaded and ready: {file.uri}")
    return file


def analyze_video(
    video_path: str = None,
    youtube_url: str = None,
    video_paths: list = None,
    prompt: str = "Describe this video",
    model: str = "gemini-2.5-flash",
    start_offset: str = None,
    end_offset: str = None,
    fps: int = 1,
    output_file: str = None,
    verbose: bool = False
):
    """Analyze video(s) using Gemini API"""

    # Get API key
    api_key = get_api_key()
    if not api_key:
        print("❌ GEMINI_API_KEY not found!")
        print("请设置环境变量: export GEMINI_API_KEY='your-api-key'")
        print("或创建 .env 文件: echo \"GEMINI_API_KEY=your-key\" > .env")
        return None

    # Initialize client
    client = genai.Client(api_key=api_key)

    # Build video sources
    video_sources = []

    # Handle YouTube URL
    if youtube_url:
        if verbose:
            print(f"🎬 Processing YouTube URL: {youtube_url}")
        video_sources.append(youtube_url)

    # Handle local video files
    if video_path:
        if verbose:
            print(f"🎬 Processing local video: {video_path}")

        # Check file size
        file_size = os.path.getsize(video_path)
        if verbose:
            print(f"   File size: {file_size / (1024*1024):.2f} MB")

        if file_size > 20 * 1024 * 1024:
            # Use Files API for large files
            file = upload_file(client, video_path, verbose)
            if file:
                video_sources.append(file.uri)
        else:
            # Use inline data for small files
            with open(video_path, 'rb') as f:
                video_data = f.read()
            video_sources.append(types.Part.from_bytes(data=video_data, mime_type='video/mp4'))

    # Handle multiple video files
    if video_paths:
        for path in video_paths:
            if os.path.exists(path):
                file = upload_file(client, path, verbose)
                if file:
                    video_sources.append(file.uri)

    if not video_sources:
        print("❌ No video source provided!")
        return None

    # Build the request
    contents = [{"role": "user", "parts": []}]

    # Add video sources to first part
    for source in video_sources:
        if isinstance(source, str) and source.startswith('https://'):
            # YouTube or file URI
            contents[0]["parts"].append({"file_data": {"file_uri": source, "mime_type": "video/mp4"}})
        else:
            # Inline data
            contents[0]["parts"].append(source)

    # Add text prompt
    contents[0]["parts"].append({"text": prompt})

    # Configure generation
    generate_content_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 65536,
        "response_modalities": ["text"],
    }

    # Add video timing config if offsets specified
    if start_offset or end_offset:
        video_metadata = {}
        if start_offset:
            video_metadata["startOffset"] = start_offset
        if end_offset:
            video_metadata["endOffset"] = end_offset
        generate_content_config["video_metadata"] = [video_metadata]

    if verbose:
        print(f"🤖 Using model: {model}")
        print(f"📝 Prompt: {prompt}")
        print("⏳ Generating response...")

    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=generate_content_config,
        )

        result = response.text

        # Output result
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"✅ 结果已保存到: {output_file}")
        else:
            print("\n" + "=" * 50)
            print("分析结果:")
            print("=" * 50)
            print(result)

        return result

    except Exception as e:
        print(f"❌ 分析失败: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description='Gemini Video Understanding - 视频分析工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 分析本地视频
  python analyze_video.py --video-path video.mp4 --prompt "总结这个视频"

  # 分析 YouTube 视频
  python analyze_video.py --youtube-url "https://www.youtube.com/watch?v=xxx" --prompt "主要内容是什么?"

  # 视频转录（带时间戳）
  python analyze_video.py --video-path video.mp4 --prompt "转录音频并标注时间戳"

  # 截取视频片段
  python analyze_video.py --video-path video.mp4 --prompt "总结这部分" --start-offset "1m30s" --end-offset "3m"

  # 多个视频对比
  python analyze_video.py --video-paths video1.mp4 video2.mp4 --prompt "对比这两个视频"

  # 指定模型 (使用最新3.1系列)
  python analyze_video.py --video-path video.mp4 --prompt "分析" --model gemini-3.1-flash

  # 列出所有可用模型
  python analyze_video.py --list-models
        """
    )

    # Required - one of these
    parser.add_argument('--video-path', type=str, help='本地视频文件路径')
    parser.add_argument('--youtube-url', type=str, help='YouTube 视频URL')
    parser.add_argument('--video-paths', type=str, nargs='+', help='多个视频文件路径 (Gemini 2.5+)')

    # Required (optional when --list-models is used)
    parser.add_argument('--prompt', type=str, help='分析提示词/问题')

    # Optional
    parser.add_argument('--model', type=str, default='gemini-2.5-flash',
                        help='使用的模型 (默认: gemini-2.5-flash, 使用 --list-models 查看所有模型)')
    parser.add_argument('--start-offset', type=str, help='视频片段开始时间 (如: "30s", "1m30s")')
    parser.add_argument('--end-offset', type=str, help='视频片段结束时间 (如: "1m", "2m30s")')
    parser.add_argument('--fps', type=int, default=1, help='帧采样率 (默认: 1)')
    parser.add_argument('--output-file', type=str, help='保存结果到文件')
    parser.add_argument('--verbose', action='store_true', help='显示详细输出')
    parser.add_argument('--list-models', action='store_true', help='列出所有可用的模型')

    args = parser.parse_args()

    # Handle list-models option
    if args.list_models:
        list_models()
        return

    # Validate inputs - prompt is required for video analysis
    if not args.prompt:
        parser.error("必须指定 --prompt")

    if not args.video_path and not args.youtube_url and not args.video_paths:
        parser.error("必须指定 --video-path, --youtube-url, 或 --video-paths 之一")

    # Run analysis
    analyze_video(
        video_path=args.video_path,
        youtube_url=args.youtube_url,
        video_paths=args.video_paths,
        prompt=args.prompt,
        model=args.model,
        start_offset=args.start_offset,
        end_offset=args.end_offset,
        fps=args.fps,
        output_file=args.output_file,
        verbose=args.verbose
    )


if __name__ == '__main__':
    main()
