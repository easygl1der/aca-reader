"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Home,
  FileText,
  BookOpen,
  PenTool,
  Bot,
  Lightbulb,
  Database,
  BookCopy,
  RefreshCw,
  ShieldCheck,
  ChevronLeft,
  ChevronRight,
  X,
} from "lucide-react";
import { cn } from "@/lib/utils";
import { useAppStore } from "@/store/use-app-store";

interface NavItem {
  icon: React.ElementType;
  label: string;
  href: string;
}

const navItems: NavItem[] = [
  { icon: Home, label: "Home", href: "/" },
  { icon: FileText, label: "Chat with PDF", href: "/chat-pdf" },
  { icon: BookOpen, label: "Literature Review", href: "/literature-review" },
  { icon: PenTool, label: "AI Writer", href: "/ai-writer" },
  { icon: Bot, label: "Agents", href: "/agents" },
  { icon: Lightbulb, label: "Find Topics", href: "/concepts" },
  { icon: Database, label: "Extract Data", href: "/extract-data" },
  { icon: BookCopy, label: "Citation Generator", href: "/citation-generator" },
  { icon: RefreshCw, label: "Paraphraser", href: "/paraphraser" },
  { icon: ShieldCheck, label: "AI Detector", href: "/ai-detector" },
];

const SIDEBAR_COLLAPSED_WIDTH = 64;
const SIDEBAR_EXPANDED_WIDTH = 240;

export function Sidebar() {
  const pathname = usePathname();
  const { sidebarExpanded, toggleSidebarExpand, mobileSidebarOpen, setMobileSidebarOpen } =
    useAppStore();

  return (
    <>
      {/* Mobile overlay */}
      {mobileSidebarOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-40 lg:hidden"
          onClick={() => setMobileSidebarOpen(false)}
        />
      )}

      {/* Mobile sidebar */}
      <aside
        className={cn(
          "fixed left-0 top-0 z-50 h-screen bg-[#0a0a0a] border-r border-[#333333] transition-transform duration-300 lg:hidden",
          mobileSidebarOpen ? "translate-x-0" : "-translate-x-full",
          "w-64"
        )}
      >
        <div className="flex h-full flex-col">
          <div className="flex items-center justify-between p-4 border-b border-[#333333]">
            <span className="text-lg font-semibold text-white">SciSpace</span>
            <button
              onClick={() => setMobileSidebarOpen(false)}
              className="p-1 hover:bg-[#262626] rounded"
            >
              <X className="h-5 w-5 text-[#a1a1a1]" />
            </button>
          </div>
          <nav className="flex-1 overflow-y-auto p-2">
            {navItems.map((item) => {
              const isActive = pathname === item.href;
              const Icon = item.icon;
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  onClick={() => setMobileSidebarOpen(false)}
                  className={cn(
                    "flex items-center gap-3 px-3 py-2.5 rounded-lg mb-1 transition-colors",
                    isActive
                      ? "bg-[#7c3aed] text-white"
                      : "text-[#a1a1a1] hover:bg-[#262626] hover:text-white"
                  )}
                >
                  <Icon className="h-5 w-5 shrink-0" />
                  <span className="text-sm font-medium">{item.label}</span>
                </Link>
              );
            })}
          </nav>
        </div>
      </aside>

      {/* Desktop sidebar */}
      <aside
        className={cn(
          "hidden lg:flex flex-col fixed left-0 top-0 h-screen bg-[#0a0a0a] border-r border-[#333333] transition-all duration-300 z-30",
          sidebarExpanded ? `w-[${SIDEBAR_EXPANDED_WIDTH}px]` : `w-[${SIDEBAR_COLLAPSED_WIDTH}px]`,
          sidebarExpanded ? "w-[240px]" : "w-[64px]"
        )}
        onMouseEnter={() => !sidebarExpanded && useAppStore.getState().setSidebarExpanded(true)}
        onMouseLeave={() => sidebarExpanded && useAppStore.getState().setSidebarExpanded(false)}
      >
        {/* Logo area */}
        <div className="flex items-center h-16 px-4 border-b border-[#333333]">
          <span
            className={cn(
              "font-bold text-xl text-white transition-opacity duration-200",
              sidebarExpanded ? "opacity-100" : "opacity-0 w-0 overflow-hidden"
            )}
          >
            SciSpace
          </span>
          {sidebarExpanded && (
            <button
              onClick={toggleSidebarExpand}
              className="ml-auto p-1 hover:bg-[#262626] rounded transition-colors"
            >
              <ChevronLeft className="h-4 w-4 text-[#a1a1a1]" />
            </button>
          )}
        </div>

        {/* Collapse button when collapsed */}
        {!sidebarExpanded && (
          <button
            onClick={toggleSidebarExpand}
            className="flex items-center justify-center h-10 mx-2 mt-2 hover:bg-[#262626] rounded-lg transition-colors"
          >
            <ChevronRight className="h-4 w-4 text-[#a1a1a1]" />
          </button>
        )}

        {/* Navigation */}
        <nav className="flex-1 overflow-y-auto p-2">
          {navItems.map((item) => {
            const isActive = pathname === item.href;
            const Icon = item.icon;
            return (
              <Link
                key={item.href}
                href={item.href}
                className={cn(
                  "flex items-center gap-3 px-3 py-2.5 rounded-lg mb-1 transition-colors relative group",
                  isActive
                    ? "bg-[#7c3aed] text-white"
                    : "text-[#a1a1a1] hover:bg-[#262626] hover:text-white"
                )}
              >
                <Icon className="h-5 w-5 shrink-0" />
                <span
                  className={cn(
                    "text-sm font-medium whitespace-nowrap transition-opacity duration-200",
                    sidebarExpanded ? "opacity-100" : "opacity-0"
                  )}
                >
                  {item.label}
                </span>

                {/* Tooltip when collapsed */}
                {!sidebarExpanded && (
                  <div className="absolute left-full ml-2 px-2 py-1 bg-[#262626] text-white text-sm rounded-md opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all whitespace-nowrap z-50">
                    {item.label}
                  </div>
                )}
              </Link>
            );
          })}
        </nav>
      </aside>
    </>
  );
}
