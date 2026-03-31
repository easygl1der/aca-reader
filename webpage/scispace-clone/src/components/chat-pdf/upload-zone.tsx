'use client';

import { useCallback, useState } from 'react';
import { Upload, FileText } from 'lucide-react';

interface UploadZoneProps {
  onFileSelect: (file: File) => void;
}

export default function UploadZone({ onFileSelect }: UploadZoneProps) {
  const [isDragging, setIsDragging] = useState(false);

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(true);
  }, []);

  const handleDragLeave = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  }, []);

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      e.stopPropagation();
      setIsDragging(false);

      const files = e.dataTransfer.files;
      if (files && files.length > 0) {
        const file = files[0];
        if (file.type === 'application/pdf') {
          onFileSelect(file);
        }
      }
    },
    [onFileSelect]
  );

  const handleFileInput = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const files = e.target.files;
      if (files && files.length > 0) {
        onFileSelect(files[0]);
      }
    },
    [onFileSelect]
  );

  return (
    <div
      className={`
        relative flex flex-col items-center justify-center
        w-full h-64 border-2 border-dashed rounded-xl
        transition-all duration-200 cursor-pointer
        ${
          isDragging
            ? 'border-violet-500 bg-violet-500/10'
            : 'border-zinc-600 hover:border-zinc-500 hover:bg-zinc-800/50'
        }
      `}
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
      onClick={() => document.getElementById('pdf-upload-input')?.click()}
    >
      <input
        id="pdf-upload-input"
        type="file"
        accept=".pdf,application/pdf"
        className="hidden"
        onChange={handleFileInput}
      />

      <div
        className={`
          flex items-center justify-center w-16 h-16 mb-4 rounded-full
          transition-colors duration-200
          ${isDragging ? 'bg-violet-500/20' : 'bg-zinc-800'}
        `}
      >
        {isDragging ? (
          <FileText className="w-8 h-8 text-violet-400" />
        ) : (
          <Upload className="w-8 h-8 text-zinc-400" />
        )}
      </div>

      <p className="text-lg font-medium text-zinc-300 mb-1">
        {isDragging ? 'Drop your PDF here' : 'Drag & drop your PDF'}
      </p>
      <p className="text-sm text-zinc-500">
        or click to browse (only .pdf files)
      </p>
    </div>
  );
}
