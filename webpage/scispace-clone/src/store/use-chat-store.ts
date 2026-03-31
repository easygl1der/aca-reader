import { create } from 'zustand';

export interface Message {
  id: string;
  role: 'user' | 'ai';
  content: string;
  timestamp: Date;
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

  // Chat state
  messages: Message[];
  isLoading: boolean;
  scope: 'this-paper' | 'all-papers';
  addMessage: (role: 'user' | 'ai', content: string) => void;
  setIsLoading: (loading: boolean) => void;
  setScope: (scope: 'this-paper' | 'all-papers') => void;
  clearMessages: () => void;
}

export const useChatStore = create<ChatStore>((set) => ({
  // PDF state
  pdfFile: null,
  pdfUrl: null,
  currentPage: 1,
  totalPages: 0,
  setPdfFile: (file) => set({ pdfFile: file }),
  setPdfUrl: (url) => set({ pdfUrl: url }),
  setCurrentPage: (page) => set({ currentPage: page }),
  setTotalPages: (total) => set({ totalPages: total }),

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
