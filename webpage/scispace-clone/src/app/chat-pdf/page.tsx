'use client';

import { useCallback, useEffect, useState } from 'react';
import dynamic from 'next/dynamic';
import { Upload, Library, FileText } from 'lucide-react';
import { useChatStore } from '@/store/use-chat-store';
import UploadZone from '@/components/chat-pdf/upload-zone';
import ChatArea from '@/components/chat-pdf/chat-area';

// Dynamic import for PdfViewer with ssr disabled (pdfjs-dist requires browser APIs)
const PdfViewer = dynamic(
  () => import('@/components/chat-pdf/pdf-viewer').then((mod) => mod.default),
  {
    ssr: false,
    loading: () => (
      <div className="flex items-center justify-center h-full bg-zinc-900 rounded-xl border border-zinc-700">
        <div className="w-8 h-8 border-4 border-violet-500 border-t-transparent rounded-full animate-spin" />
      </div>
    ),
  }
);

export default function ChatPdfPage() {
  const [mounted, setMounted] = useState(false);
  const [showUploadZone, setShowUploadZone] = useState(true);

  const {
    pdfFile,
    pdfUrl,
    currentPage,
    totalPages,
    scope,
    setPdfFile,
    setPdfUrl,
    setCurrentPage,
    setTotalPages,
    setScope,
  } = useChatStore();

  // Handle hydration
  useEffect(() => {
    setMounted(true);
  }, []);

  // Update total pages when pdfDoc is ready
  const handleFileSelect = useCallback(
    async (file: File) => {
      setPdfFile(file);
      setShowUploadZone(false);

      // Create object URL for the file
      const url = URL.createObjectURL(file);
      setPdfUrl(url);

      // Load PDF to get total pages
      try {
        const pdfjsLib = await import('pdfjs-dist');
        const loadingTask = pdfjsLib.getDocument(url);
        const pdf = await loadingTask.promise;
        setTotalPages(pdf.numPages);
      } catch (error) {
        console.error('Error loading PDF:', error);
      }
    },
    [setPdfFile, setPdfUrl, setTotalPages]
  );

  const handleUploadClick = () => {
    setShowUploadZone(true);
  };

  const handleLibraryClick = () => {
    // Mock library action
    alert('Library feature coming soon!');
  };

  if (!mounted) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="w-8 h-8 border-4 border-violet-500 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full">
      {/* Top Bar */}
      <div className="flex items-center justify-between px-4 py-3 bg-zinc-900 border-b border-zinc-700">
        {/* Left side - Upload and Library buttons */}
        <div className="flex items-center gap-2">
          <button
            onClick={handleUploadClick}
            className={`
              flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium
              transition-all duration-200
              ${
                showUploadZone
                  ? 'bg-violet-600 text-white'
                  : 'bg-zinc-800 text-zinc-300 hover:bg-zinc-700'
              }
            `}
          >
            <Upload className="w-4 h-4" />
            Upload PDF
          </button>
          <button
            onClick={handleLibraryClick}
            className="flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium
              bg-zinc-800 text-zinc-300 hover:bg-zinc-700
              transition-all duration-200"
          >
            <Library className="w-4 h-4" />
            My Library
          </button>
        </div>

        {/* Right side - Scope toggles */}
        <div className="flex items-center gap-1 p-1 bg-zinc-800 rounded-xl">
          <button
            onClick={() => setScope('this-paper')}
            className={`
              px-4 py-1.5 rounded-lg text-sm font-medium
              transition-all duration-200
              ${
                scope === 'this-paper'
                  ? 'bg-violet-600 text-white'
                  : 'text-zinc-400 hover:text-white'
              }
            `}
          >
            Only This Paper
          </button>
          <button
            onClick={() => setScope('all-papers')}
            className={`
              px-4 py-1.5 rounded-lg text-sm font-medium
              transition-all duration-200
              ${
                scope === 'all-papers'
                  ? 'bg-violet-600 text-white'
                  : 'text-zinc-400 hover:text-white'
              }
            `}
          >
            All Papers
          </button>
        </div>
      </div>

      {/* Main Content - Two Panel Layout */}
      <div className="flex-1 flex flex-col lg:flex-row gap-4 p-4 min-h-0">
        {/* Left Panel - PDF Viewer */}
        <div className="flex-1 lg:w-1/2 min-h-[300px] lg:min-h-0">
          {showUploadZone && !pdfUrl ? (
            <div className="h-full flex flex-col">
              <UploadZone onFileSelect={handleFileSelect} />

              {/* Show current PDF info if loaded */}
              {pdfFile && (
                <div className="mt-4 p-4 bg-zinc-800 rounded-xl border border-zinc-700">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-lg bg-violet-600/20 flex items-center justify-center">
                      <FileText className="w-5 h-5 text-violet-400" />
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-white font-medium truncate">
                        {pdfFile.name}
                      </p>
                      <p className="text-zinc-400 text-sm">
                        {(pdfFile.size / 1024 / 1024).toFixed(2)} MB
                      </p>
                    </div>
                    <button
                      onClick={() => setShowUploadZone(false)}
                      className="px-3 py-1.5 bg-violet-600 hover:bg-violet-500 text-white text-sm rounded-lg
                        transition-colors duration-200"
                    >
                      View PDF
                    </button>
                  </div>
                </div>
              )}
            </div>
          ) : (
            <PdfViewer
              pdfUrl={pdfUrl}
              currentPage={currentPage}
              totalPages={totalPages}
              onPageChange={setCurrentPage}
            />
          )}
        </div>

        {/* Right Panel - Chat Area */}
        <div className="flex-1 lg:w-1/2 min-h-[400px] lg:min-h-0">
          <ChatArea pdfFileName={pdfFile?.name || null} />
        </div>
      </div>
    </div>
  );
}
