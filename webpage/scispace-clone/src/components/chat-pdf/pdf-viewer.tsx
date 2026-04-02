'use client';

import { useEffect, useRef, useState } from 'react';
import {
  ChevronLeft,
  ChevronRight,
  FileText,
  ZoomIn,
  ZoomOut,
  Maximize2,
} from 'lucide-react';

interface PdfViewerProps {
  pdfUrl: string | null;
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}

const ZOOM_LEVELS = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0];

export default function PdfViewer({
  pdfUrl,
  currentPage,
  totalPages,
  onPageChange,
}: PdfViewerProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const [pdfDoc, setPdfDoc] = useState<any>(null);
  const [scale, setScale] = useState(1.5);
  const [isLoading, setIsLoading] = useState(false);
  const [isPageInputOpen, setIsPageInputOpen] = useState(false);
  const [pageInputValue, setPageInputValue] = useState(String(currentPage));
  const pageInputRef = useRef<HTMLInputElement>(null);

  // Update page input when currentPage changes externally
  useEffect(() => {
    setPageInputValue(String(currentPage));
  }, [currentPage]);

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

  const handleZoomIn = () => {
    const currentIndex = ZOOM_LEVELS.indexOf(scale);
    if (currentIndex < ZOOM_LEVELS.length - 1) {
      setScale(ZOOM_LEVELS[currentIndex + 1]);
    } else if (currentIndex === -1) {
      // Find next level above current scale
      const nextLevel = ZOOM_LEVELS.find((level) => level > scale);
      if (nextLevel) setScale(nextLevel);
    }
  };

  const handleZoomOut = () => {
    const currentIndex = ZOOM_LEVELS.indexOf(scale);
    if (currentIndex > 0) {
      setScale(ZOOM_LEVELS[currentIndex - 1]);
    } else if (currentIndex === -1) {
      // Find next level below current scale
      const prevLevel = [...ZOOM_LEVELS].reverse().find((level) => level < scale);
      if (prevLevel) setScale(prevLevel);
    }
  };

  const handleFitToWidth = () => {
    if (containerRef.current && canvasRef.current) {
      const containerWidth = containerRef.current.clientWidth - 32; // padding
      const canvasWidth = canvasRef.current.width / scale;
      const fitScale = containerWidth / canvasWidth;
      setScale(Math.min(fitScale, 3.0)); // Cap at max zoom
    }
  };

  const handlePageInputSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const page = parseInt(pageInputValue, 10);
    if (!isNaN(page) && page >= 1 && page <= totalPages) {
      onPageChange(page);
    } else {
      setPageInputValue(String(currentPage));
    }
    setIsPageInputOpen(false);
  };

  const handlePageInputBlur = () => {
    setPageInputValue(String(currentPage));
    setIsPageInputOpen(false);
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
      {/* PDF Canvas Area - Scrollable */}
      <div
        ref={containerRef}
        className="flex-1 overflow-auto p-4 flex justify-center"
      >
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

      {/* Toolbar - Zoom and Fit Controls */}
      <div className="flex items-center justify-between px-4 py-2 bg-zinc-800/80 border-t border-zinc-700">
        <div className="flex items-center gap-1">
          <button
            onClick={handleZoomOut}
            disabled={scale <= ZOOM_LEVELS[0]}
            className={`
              flex items-center justify-center w-8 h-8 rounded-lg
              transition-colors duration-200
              ${
                scale <= ZOOM_LEVELS[0]
                  ? 'text-zinc-600 cursor-not-allowed'
                  : 'text-zinc-400 hover:bg-zinc-700 hover:text-white'
              }
            `}
            title="Zoom out"
          >
            <ZoomOut className="w-4 h-4" />
          </button>

          <div className="flex items-center gap-1 px-2">
            <span className="text-sm text-zinc-400 min-w-[48px] text-center">
              {Math.round(scale * 100)}%
            </span>
          </div>

          <button
            onClick={handleZoomIn}
            disabled={scale >= ZOOM_LEVELS[ZOOM_LEVELS.length - 1]}
            className={`
              flex items-center justify-center w-8 h-8 rounded-lg
              transition-colors duration-200
              ${
                scale >= ZOOM_LEVELS[ZOOM_LEVELS.length - 1]
                  ? 'text-zinc-600 cursor-not-allowed'
                  : 'text-zinc-400 hover:bg-zinc-700 hover:text-white'
              }
            `}
            title="Zoom in"
          >
            <ZoomIn className="w-4 h-4" />
          </button>

          <button
            onClick={handleFitToWidth}
            className="flex items-center justify-center w-8 h-8 rounded-lg
              text-zinc-400 hover:bg-zinc-700 hover:text-white
              transition-colors duration-200"
            title="Fit to width"
          >
            <Maximize2 className="w-4 h-4" />
          </button>
        </div>

        {/* Page Navigation */}
        <div className="flex items-center gap-2">
          <button
            onClick={goToPreviousPage}
            disabled={currentPage <= 1}
            className={`
              flex items-center gap-1 px-2 py-1.5 rounded-lg text-sm
              transition-colors duration-200
              ${
                currentPage <= 1
                  ? 'text-zinc-600 cursor-not-allowed'
                  : 'text-zinc-300 hover:bg-zinc-700 hover:text-white'
              }
            `}
          >
            <ChevronLeft className="w-4 h-4" />
          </button>

          {isPageInputOpen ? (
            <form onSubmit={handlePageInputSubmit}>
              <input
                ref={pageInputRef}
                type="text"
                value={pageInputValue}
                onChange={(e) => setPageInputValue(e.target.value)}
                onBlur={handlePageInputBlur}
                className="w-14 px-2 py-1 bg-zinc-700 border border-zinc-600 rounded text-center
                  text-white text-sm focus:outline-none focus:ring-2 focus:ring-violet-500"
                autoFocus
              />
            </form>
          ) : (
            <button
              onClick={() => {
                setIsPageInputOpen(true);
                setPageInputValue(String(currentPage));
              }}
              className="text-sm text-zinc-400 hover:text-white transition-colors"
            >
              <span className="text-white font-medium">{currentPage}</span>
              <span className="mx-1">/</span>
              <span>{totalPages || '...'}</span>
            </button>
          )}

          <button
            onClick={goToNextPage}
            disabled={currentPage >= totalPages}
            className={`
              flex items-center gap-1 px-2 py-1.5 rounded-lg text-sm
              transition-colors duration-200
              ${
                currentPage >= totalPages
                  ? 'text-zinc-600 cursor-not-allowed'
                  : 'text-zinc-300 hover:bg-zinc-700 hover:text-white'
              }
            `}
          >
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
}
