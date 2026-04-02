'use client';

import { useState } from 'react';
import {
  FolderOpen,
  FileText,
  Trash2,
  Loader2,
  CheckCircle,
  AlertCircle,
  File,
  Sparkles,
  ChevronRight,
  ChevronDown,
} from 'lucide-react';
import { useChatStore, LibraryItem } from '@/store/use-chat-store';

interface LibrarySidebarProps {
  onUploadClick: () => void;
}

export default function LibrarySidebar({ onUploadClick }: LibrarySidebarProps) {
  const {
    library,
    currentItem,
    selectItem,
    removeFromLibrary,
    transcriptionStatus,
    updateLibraryItem,
    setMarkdown,
    setTranscriptionStatus,
    setViewMode,
    setPdfFile,
    setPdfUrl,
    setCurrentPage,
    setTotalPages,
  } = useChatStore();

  const [isProcessing, setIsProcessing] = useState<string | null>(null);

  const handleSelectItem = (item: LibraryItem) => {
    selectItem(item);
    setViewMode('pdf');
  };

  const handleDeleteItem = (e: React.MouseEvent, id: string) => {
    e.stopPropagation();
    if (currentItem?.id === id) {
      selectItem(null);
      setPdfFile(null);
      setPdfUrl(null);
      setMarkdown(null);
    }
    removeFromLibrary(id);
  };

  const handleProcessWithMinerU = async (e: React.MouseEvent, item: LibraryItem) => {
    e.stopPropagation();
    setIsProcessing(item.id);
    setTranscriptionStatus('processing');
    updateLibraryItem(item.id, { transcriptionStatus: 'processing' });

    // Simulate minerU API call
    await new Promise((resolve) => setTimeout(resolve, 3000));

    // Mock markdown content
    const mockMarkdown = `# Sample Paper: ${item.name}

## Abstract

This paper presents a comprehensive study on machine learning techniques and their applications in modern computational problems. We introduce novel approaches that significantly improve performance over existing methods.

## 1. Introduction

The field of machine learning has seen tremendous growth in recent years. Deep learning architectures have revolutionized how we approach complex problems in computer vision, natural language processing, and reinforcement learning.

### 1.1 Background

Traditional machine learning approaches relied heavily on feature engineering. However, the advent of deep neural networks has shifted the paradigm towards learning representations directly from raw data.

## 2. Mathematical Foundations

The optimization objective can be expressed as:

$$\\min_{\\theta} \\mathcal{L}(\\theta) = \\frac{1}{n} \\sum_{i=1}^{n} \\ell(f_\\theta(x_i), y_i)$$

Where:
- $\\theta$ represents the model parameters
- $\\mathcal{L}$ is the loss function
- $f_\\theta$ is the model with parameters $\\theta$

### Theorem 2.1 (Convergence)
For a convex loss function $\\mathcal{L}$, gradient descent converges to the global optimum at a rate of $O(1/k)$.

## 3. Methodology

Our approach consists of three main components:

1. **Data Preprocessing**: Normalization and augmentation
2. **Model Architecture**: Transformer-based encoder-decoder
3. **Training Strategy**: Curriculum learning with warmup

\`\`\`python
class OurModel(nn.Module):
    def __init__(self, d_model=512, nhead=8):
        self.encoder = TransformerEncoder(d_model, nhead)
        self.decoder = TransformerDecoder(d_model, nhead)
        self.output_layer = Linear(d_model, vocab_size)
\`\`\`

## 4. Experimental Results

| Model | Accuracy | F1 Score |
|-------|----------|----------|
| Baseline | 85.2% | 0.84 |
| Ours | 92.7% | 0.91 |

## 5. Conclusion

We have demonstrated that our approach achieves state-of-the-art results on multiple benchmarks. Future work includes exploring larger-scale experiments and applications to real-world problems.

## References

1. Vaswani et al. (2017) Attention Is All You Need
2. Devlin et al. (2018) BERT: Pre-training of Deep Bidirectional Transformers
`;

    setMarkdown(mockMarkdown);
    setTranscriptionStatus('done');
    updateLibraryItem(item.id, {
      transcriptionStatus: 'done',
      markdownContent: mockMarkdown,
    });
    setIsProcessing(null);
    setViewMode('markdown');
  };

  const getStatusIcon = (status: LibraryItem['transcriptionStatus']) => {
    switch (status) {
      case 'idle':
        return <File className="w-4 h-4 text-zinc-500" />;
      case 'processing':
        return <Loader2 className="w-4 h-4 text-amber-500 animate-spin" />;
      case 'done':
        return <CheckCircle className="w-4 h-4 text-emerald-500" />;
      case 'error':
        return <AlertCircle className="w-4 h-4 text-red-500" />;
    }
  };

  const formatDate = (date: Date) => {
    return new Intl.DateTimeFormat('en-US', {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    }).format(date);
  };

  return (
    <div className="flex flex-col h-full bg-zinc-900 border-r border-zinc-700">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-zinc-700">
        <div className="flex items-center gap-2">
          <FolderOpen className="w-5 h-5 text-violet-400" />
          <span className="font-medium text-white">My Library</span>
        </div>
        <button
          onClick={onUploadClick}
          className="flex items-center gap-1 px-2 py-1 bg-violet-600 hover:bg-violet-500
            text-white text-xs font-medium rounded-lg transition-colors duration-200"
        >
          + Upload
        </button>
      </div>

      {/* Library List */}
      <div className="flex-1 overflow-y-auto">
        {library.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full p-4 text-center">
            <FileText className="w-12 h-12 text-zinc-600 mb-3" />
            <p className="text-zinc-400 text-sm mb-1">No documents yet</p>
            <p className="text-zinc-500 text-xs">
              Upload a PDF to get started
            </p>
          </div>
        ) : (
          <div className="p-2 space-y-1">
            {library.map((item) => (
              <div
                key={item.id}
                onClick={() => handleSelectItem(item)}
                className={`
                  group relative p-3 rounded-xl cursor-pointer transition-all duration-200
                  ${
                    currentItem?.id === item.id
                      ? 'bg-violet-600/20 border border-violet-500/50'
                      : 'hover:bg-zinc-800 border border-transparent'
                  }
                `}
              >
                {/* Document Icon and Info */}
                <div className="flex items-start gap-3">
                  <div
                    className={`
                      flex-shrink-0 w-8 h-8 rounded-lg flex items-center justify-center
                      ${
                        currentItem?.id === item.id
                          ? 'bg-violet-600/30'
                          : 'bg-zinc-800'
                      }
                    `}
                  >
                    <FileText
                      className={`w-4 h-4 ${
                        currentItem?.id === item.id
                          ? 'text-violet-400'
                          : 'text-zinc-400'
                      }`}
                    />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p
                      className={`
                        text-sm font-medium truncate
                        ${
                          currentItem?.id === item.id
                            ? 'text-white'
                            : 'text-zinc-300'
                        }
                      `}
                    >
                      {item.name}
                    </p>
                    <div className="flex items-center gap-2 mt-1">
                      {getStatusIcon(item.transcriptionStatus)}
                      <span className="text-xs text-zinc-500">
                        {formatDate(item.uploadDate)}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Action Buttons - visible on hover */}
                <div className="absolute top-2 right-2 flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                  {item.transcriptionStatus === 'idle' && (
                    <button
                      onClick={(e) => handleProcessWithMinerU(e, item)}
                      disabled={isProcessing === item.id}
                      className="flex items-center gap-1 px-2 py-1 bg-zinc-700 hover:bg-violet-600
                        text-zinc-300 hover:text-white text-xs rounded-lg transition-colors duration-200"
                      title="Process with MinerU"
                    >
                      {isProcessing === item.id ? (
                        <Loader2 className="w-3 h-3 animate-spin" />
                      ) : (
                        <Sparkles className="w-3 h-3" />
                      )}
                    </button>
                  )}
                  {item.transcriptionStatus === 'done' && (
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setViewMode('markdown');
                      }}
                      className="flex items-center gap-1 px-2 py-1 bg-zinc-700 hover:bg-emerald-600
                        text-zinc-300 hover:text-white text-xs rounded-lg transition-colors duration-200"
                      title="View Markdown"
                    >
                      <FileText className="w-3 h-3" />
                    </button>
                  )}
                  <button
                    onClick={(e) => handleDeleteItem(e, item.id)}
                    className="flex items-center gap-1 px-2 py-1 bg-zinc-700 hover:bg-red-600
                      text-zinc-300 hover:text-white text-xs rounded-lg transition-colors duration-200"
                    title="Delete"
                  >
                    <Trash2 className="w-3 h-3" />
                  </button>
                </div>

                {/* Transcription Status Indicator */}
                {item.transcriptionStatus === 'processing' && (
                  <div className="mt-2">
                    <div className="flex items-center gap-2 text-xs text-amber-500">
                      <Loader2 className="w-3 h-3 animate-spin" />
                      <span>Processing with MinerU...</span>
                    </div>
                    <div className="mt-1 h-1 bg-zinc-700 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-amber-500 animate-pulse"
                        style={{ width: '60%' }}
                      />
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Status Bar */}
      {transcriptionStatus !== 'idle' && (
        <div className="px-4 py-2 border-t border-zinc-700 bg-zinc-800/50">
          <div className="flex items-center gap-2 text-xs">
            {transcriptionStatus === 'processing' && (
              <>
                <Loader2 className="w-3 h-3 text-amber-500 animate-spin" />
                <span className="text-amber-500">Processing document...</span>
              </>
            )}
            {transcriptionStatus === 'done' && (
              <>
                <CheckCircle className="w-3 h-3 text-emerald-500" />
                <span className="text-emerald-500">Ready for chat</span>
              </>
            )}
            {transcriptionStatus === 'error' && (
              <>
                <AlertCircle className="w-3 h-3 text-red-500" />
                <span className="text-red-500">Processing failed</span>
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
