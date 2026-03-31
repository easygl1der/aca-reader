'use client';

import { useEffect, useRef, useState } from 'react';
import { ChevronLeft, ChevronRight, FileText } from 'lucide-react';

interface PdfViewerProps {
  pdfUrl: string | null;
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}

export default function PdfViewer({
  pdfUrl,
  currentPage,
  totalPages,
  onPageChange,
}: PdfViewerProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [pdfDoc, setPdfDoc] = useState<any>(null);
  const [scale, setScale] = useState(1.5);
  const [isLoading, setIsLoading] = useState(false);

  // Load PDF document
  useEffect(() => {
    if (!pdfUrl) return;

    setIsLoading(true);

    const loadPdf = async () => {
      try {
        // Dynamically import pdfjs-dist to avoid SSR issues
        const pdfjsLib = await import('pdfjs-dist');

        // Set up the worker for pdf.js
        pdfjsLib.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version}/pdf.worker.min.js`;

        const loadingTask = pdfjsLib.getDocument(pdfUrl);
        const pdf = await loadingTask.promise;
        setPdfDoc(pdf);
        onPageChange(1); // Reset to first page when new PDF is loaded
      } catch (error) {
        console.error('Error loading PDF:', error);
      } finally {
        setIsLoading(false);
      }
    };

    loadPdf();

    return () => {
      pdfDoc?.destroy();
    };
  }, [pdfUrl]);

  // Render current page
  useEffect(() => {
    if (!pdfDoc || !canvasRef.current) return;

    const renderPage = async () => {
      setIsLoading(true);
      try {
        const page = await pdfDoc.getPage(currentPage);
        const viewport = page.getViewport({ scale });

        const canvas = canvasRef.current!;
        const context = canvas.getContext('2d')!;

        canvas.height = viewport.height;
        canvas.width = viewport.width;

        await page.render({
          canvasContext: context,
          viewport: viewport,
          canvas: canvas,
        }).promise;
      } catch (error) {
        console.error('Error rendering page:', error);
      } finally {
        setIsLoading(false);
      }
    };

    renderPage();
  }, [pdfDoc, currentPage, scale]);

  const goToPreviousPage = () => {
    if (currentPage > 1) {
      onPageChange(currentPage - 1);
    }
  };

  const goToNextPage = () => {
    if (currentPage < totalPages) {
      onPageChange(currentPage + 1);
    }
  };

  if (!pdfUrl) {
    return (
      <div className="flex flex-col items-center justify-center h-full bg-zinc-900 rounded-xl border border-zinc-700">
        <FileText className="w-16 h-16 text-zinc-600 mb-4" />
        <p className="text-zinc-400 text-lg">No PDF loaded</p>
        <p className="text-zinc-500 text-sm mt-1">
          Upload a PDF to get started
        </p>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full bg-zinc-900 rounded-xl border border-zinc-700 overflow-hidden">
      {/* PDF Canvas Area */}
      <div className="flex-1 overflow-auto p-4 flex justify-center">
        <div className="relative">
          <canvas
            ref={canvasRef}
            className="max-w-full shadow-2xl"
            style={{ display: 'block' }}
          />
          {isLoading && (
            <div className="absolute inset-0 flex items-center justify-center bg-zinc-900/50">
              <div className="w-8 h-8 border-4 border-violet-500 border-t-transparent rounded-full animate-spin" />
            </div>
          )}
        </div>
      </div>

      {/* Page Navigation */}
      <div className="flex items-center justify-between px-4 py-3 bg-zinc-800 border-t border-zinc-700">
        <button
          onClick={goToPreviousPage}
          disabled={currentPage <= 1}
          className={`
            flex items-center gap-1 px-3 py-1.5 rounded-lg text-sm
            transition-colors duration-200
            ${
              currentPage <= 1
                ? 'text-zinc-600 cursor-not-allowed'
                : 'text-zinc-300 hover:bg-zinc-700 hover:text-white'
            }
          `}
        >
          <ChevronLeft className="w-4 h-4" />
          Previous
        </button>

        <div className="flex items-center gap-2">
          <span className="text-sm text-zinc-400">
            Page{' '}
            <span className="text-white font-medium">{currentPage}</span> of{' '}
            <span className="text-white font-medium">{totalPages || '...'}</span>
          </span>
        </div>

        <button
          onClick={goToNextPage}
          disabled={currentPage >= totalPages}
          className={`
            flex items-center gap-1 px-3 py-1.5 rounded-lg text-sm
            transition-colors duration-200
            ${
              currentPage >= totalPages
                ? 'text-zinc-600 cursor-not-allowed'
                : 'text-zinc-300 hover:bg-zinc-700 hover:text-white'
            }
          `}
        >
          Next
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
