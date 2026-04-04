'use client';

import { useCallback, useEffect, useState } from 'react';
import dynamic from 'next/dynamic';
import { Upload, Library, FileText, File, FileDown } from 'lucide-react';
import { useChatStore } from '@/store/use-chat-store';
import UploadZone from '@/components/chat-pdf/upload-zone';
import ChatArea from '@/components/chat-pdf/chat-area';
import LibrarySidebar from '@/components/chat-pdf/library-sidebar';
import MarkdownViewer from '@/components/chat-pdf/markdown-viewer';

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
  const [showLibrary, setShowLibrary] = useState(true);

  const {
    pdfFile,
    pdfUrl,
    currentPage,
    totalPages,
    scope,
    viewMode,
    markdownContent,
    library,
    currentItem,
    transcriptionStatus,
    setPdfFile,
    setPdfUrl,
    setCurrentPage,
    setTotalPages,
    setScope,
    setViewMode,
    setMarkdown,
    addToLibrary,
    selectItem,
    setTranscriptionStatus,
  } = useChatStore();

  // Handle hydration
  useEffect(() => {
    setMounted(true);
  }, []);

  // Debug logging
  useEffect(() => {
    console.log('[ChatPdf] currentItem:', currentItem?.name, 'url:', currentItem?.url);
    console.log('[ChatPdf] pdfUrl:', pdfUrl);
    console.log('[ChatPdf] viewMode:', viewMode);
  }, [currentItem, pdfUrl, viewMode]);

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

        // Add to library and select it
        const newItem = addToLibrary(file, url, pdf.numPages);
        selectItem(newItem);
      } catch (error) {
        console.error('Error loading PDF:', error);
      }
    },
    [setPdfFile, setPdfUrl, setTotalPages, addToLibrary]
  );

  const handleUploadClick = () => {
    setShowUploadZone(true);
    setShowLibrary(false);
    selectItem(null);
  };

  const handleLibraryClick = () => {
    setShowLibrary(!showLibrary);
  };

  const handleViewModeToggle = (mode: 'pdf' | 'markdown') => {
    setViewMode(mode);
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
                showUploadZone && !pdfUrl
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
            className={`
              flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium
              transition-all duration-200
              ${
                showLibrary
                  ? 'bg-violet-600 text-white'
                  : 'bg-zinc-800 text-zinc-300 hover:bg-zinc-700'
              }
            `}
          >
            <Library className="w-4 h-4" />
            My Library
            {library.length > 0 && (
              <span className="ml-1 px-1.5 py-0.5 bg-violet-500/30 text-violet-300 text-xs rounded-md">
                {library.length}
              </span>
            )}
          </button>
        </div>

        {/* Center - View mode toggle (when document is loaded) */}
        {currentItem && (
          <div className="flex items-center gap-1 p-1 bg-zinc-800 rounded-xl">
            <button
              onClick={() => handleViewModeToggle('pdf')}
              className={`
                flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm font-medium
                transition-all duration-200
                ${
                  viewMode === 'pdf'
                    ? 'bg-violet-600 text-white'
                    : 'text-zinc-400 hover:text-white'
                }
              `}
            >
              <File className="w-4 h-4" />
              PDF
            </button>
            <button
              onClick={() => handleViewModeToggle('markdown')}
              disabled={transcriptionStatus !== 'done'}
              className={`
                flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm font-medium
                transition-all duration-200
                ${
                  viewMode === 'markdown'
                    ? 'bg-violet-600 text-white'
                    : 'text-zinc-400 hover:text-white'
                }
                ${transcriptionStatus !== 'done' ? 'opacity-50 cursor-not-allowed' : ''}
              `}
            >
              <FileDown className="w-4 h-4" />
              Markdown
            </button>
          </div>
        )}

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

      {/* Main Content - Three Panel Layout */}
      <div className="flex-1 flex min-h-0">
        {/* Library Sidebar */}
        {showLibrary && (
          <div className="w-72 flex-shrink-0 border-r border-zinc-700">
            <LibrarySidebar onUploadClick={handleUploadClick} />
          </div>
        )}

        {/* Document Viewer Area */}
        <div className="flex-1 flex flex-col min-w-0">
          {/* Show Upload Zone when uploading and no PDF selected */}
          {showUploadZone && !pdfUrl ? (
            <div className="flex-1 flex flex-col p-4 min-h-0">
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
          ) : currentItem ? (
            /* View toggle between PDF and Markdown */
            viewMode === 'pdf' ? (
              <div className="flex-1 p-4 min-h-0">
                <PdfViewer
                  pdfUrl={currentItem.url}
                  currentPage={currentPage}
                  totalPages={currentItem.totalPages}
                  onPageChange={setCurrentPage}
                />
              </div>
            ) : (
              <div className="flex-1 p-4 min-h-0">
                <MarkdownViewer
                  content={markdownContent}
                  isLoading={transcriptionStatus === 'processing'}
                />
              </div>
            )
          ) : (
            /* No document selected */
            <div className="flex-1 flex items-center justify-center">
              <div className="text-center">
                <FileText className="w-16 h-16 text-zinc-600 mx-auto mb-4" />
                <p className="text-zinc-400 text-lg mb-2">
                  No document selected
                </p>
                <p className="text-zinc-500 text-sm">
                  Upload a PDF or select one from your library
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Chat Area */}
        <div className="w-[400px] flex-shrink-0 border-l border-zinc-700 p-4">
          <ChatArea pdfFileName={currentItem?.name || pdfFile?.name || null} />
        </div>
      </div>
    </div>
  );
}
