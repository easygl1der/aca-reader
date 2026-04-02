import { create } from 'zustand';

export interface Message {
  id: string;
  role: 'user' | 'ai';
  content: string;
  timestamp: Date;
}

export type TranscriptionStatus = 'idle' | 'processing' | 'done' | 'error';

export interface LibraryItem {
  id: string;
  name: string;
  file: File;
  url: string;
  uploadDate: Date;
  transcriptionStatus: TranscriptionStatus;
  markdownContent: string | null;
  totalPages: number;
}

interface ChatStore {
  // PDF state
  pdfFile: File | null;
  pdfUrl: string | null;
  currentPage: number;
  totalPages: number;
  setPdfFile: (file: File | null) => void;
  setPdfUrl: (url: string | null) => void;
  setCurrentPage: (page: number) => void;
  setTotalPages: (total: number) => void;

  // Library state
  library: LibraryItem[];
  currentItem: LibraryItem | null;
  transcriptionStatus: TranscriptionStatus;
  markdownContent: string | null;
  addToLibrary: (file: File, url: string, totalPages: number) => LibraryItem;
  selectItem: (item: LibraryItem | null) => void;
  removeFromLibrary: (id: string) => void;
  setTranscriptionStatus: (status: TranscriptionStatus) => void;
  setMarkdown: (content: string | null) => void;
  updateLibraryItem: (id: string, updates: Partial<LibraryItem>) => void;

  // View mode
  viewMode: 'pdf' | 'markdown';
  setViewMode: (mode: 'pdf' | 'markdown') => void;

  // Chat state
  messages: Message[];
  isLoading: boolean;
  scope: 'this-paper' | 'all-papers';
  addMessage: (role: 'user' | 'ai', content: string) => void;
  setIsLoading: (loading: boolean) => void;
  setScope: (scope: 'this-paper' | 'all-papers') => void;
  clearMessages: () => void;
}

export const useChatStore = create<ChatStore>((set, get) => ({
  // PDF state
  pdfFile: null,
  pdfUrl: null,
  currentPage: 1,
  totalPages: 0,
  setPdfFile: (file) => set({ pdfFile: file }),
  setPdfUrl: (url) => set({ pdfUrl: url }),
  setCurrentPage: (page) => set({ currentPage: page }),
  setTotalPages: (total) => set({ totalPages: total }),

  // Library state
  library: [],
  currentItem: null,
  transcriptionStatus: 'idle',
  markdownContent: null,
  addToLibrary: (file, url, totalPages) => {
    const newItem: LibraryItem = {
      id: `lib-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
      name: file.name,
      file,
      url,
      uploadDate: new Date(),
      transcriptionStatus: 'idle',
      markdownContent: null,
      totalPages,
    };
    set((state) => ({
      library: [newItem, ...state.library],
    }));
    return newItem;
  },
  selectItem: (item) =>
    set({
      currentItem: item,
      pdfFile: item?.file || null,
      pdfUrl: item?.url || null,
      currentPage: 1,
      totalPages: item?.totalPages || 0,
      markdownContent: item?.markdownContent || null,
      transcriptionStatus: item?.transcriptionStatus || 'idle',
    }),
  removeFromLibrary: (id) =>
    set((state) => {
      const item = state.library.find((i) => i.id === id);
      if (item) {
        URL.revokeObjectURL(item.url);
      }
      const newLibrary = state.library.filter((i) => i.id !== id);
      const newCurrentItem = state.currentItem?.id === id ? null : state.currentItem;
      return {
        library: newLibrary,
        currentItem: newCurrentItem,
        pdfFile: newCurrentItem ? newCurrentItem.file : null,
        pdfUrl: newCurrentItem ? newCurrentItem.url : null,
        markdownContent: newCurrentItem?.markdownContent || null,
      };
    }),
  setTranscriptionStatus: (status) => set({ transcriptionStatus: status }),
  setMarkdown: (content) => set({ markdownContent: content }),
  updateLibraryItem: (id, updates) =>
    set((state) => ({
      library: state.library.map((item) =>
        item.id === id ? { ...item, ...updates } : item
      ),
      currentItem:
        state.currentItem?.id === id
          ? { ...state.currentItem, ...updates }
          : state.currentItem,
    })),

  // View mode
  viewMode: 'pdf',
  setViewMode: (mode) => set({ viewMode: mode }),

  // Chat state
  messages: [],
  isLoading: false,
  scope: 'this-paper',
  addMessage: (role, content) =>
    set((state) => ({
      messages: [
        ...state.messages,
        {
          id: `msg-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
          role,
          content,
          timestamp: new Date(),
        },
      ],
    })),
  setIsLoading: (loading) => set({ isLoading: loading }),
  setScope: (scope) => set({ scope }),
  clearMessages: () => set({ messages: [] }),
}));
