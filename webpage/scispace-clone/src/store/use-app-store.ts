"use client";

import { create } from "zustand";

interface AppState {
  // Sidebar state
  sidebarOpen: boolean;
  sidebarExpanded: boolean;
  toggleSidebar: () => void;
  toggleSidebarExpand: () => void;
  setSidebarExpanded: (expanded: boolean) => void;

  // Mobile sidebar
  mobileSidebarOpen: boolean;
  toggleMobileSidebar: () => void;
  setMobileSidebarOpen: (open: boolean) => void;
}

export const useAppStore = create<AppState>((set) => ({
  // Sidebar state - default collapsed (icons only)
  sidebarOpen: true,
  sidebarExpanded: false,
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
  toggleSidebarExpand: () =>
    set((state) => ({ sidebarExpanded: !state.sidebarExpanded })),
  setSidebarExpanded: (expanded) => set({ sidebarExpanded: expanded }),

  // Mobile sidebar - default closed
  mobileSidebarOpen: false,
  toggleMobileSidebar: () =>
    set((state) => ({ mobileSidebarOpen: !state.mobileSidebarOpen })),
  setMobileSidebarOpen: (open) => set({ mobileSidebarOpen: open }),
}));
