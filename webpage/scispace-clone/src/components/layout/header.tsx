"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ChevronRight, Upload, User, Menu } from "lucide-react";
import { cn } from "@/lib/utils";
import { useAppStore } from "@/store/use-app-store";

/**
 * Format a pathname segment to a readable label
 */
function formatLabel(segment: string): string {
  return segment
    .replace(/-/g, " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
}

/**
 * Generate breadcrumb items from the current pathname
 */
function getBreadcrumbs(pathname: string): { label: string; href: string }[] {
  const segments = pathname.split("/").filter(Boolean);
  const breadcrumbs = [{ label: "Home", href: "/" }];

  let currentPath = "";
  for (const segment of segments) {
    currentPath += `/${segment}`;
    breadcrumbs.push({
      label: formatLabel(segment),
      href: currentPath,
    });
  }

  return breadcrumbs;
}

export function Header() {
  const pathname = usePathname();
  const { setMobileSidebarOpen } = useAppStore();
  const breadcrumbs = getBreadcrumbs(pathname);

  return (
    <header className="sticky top-0 z-20 flex items-center h-16 px-4 bg-[#0a0a0a] border-b border-[#333333] lg:px-6">
      {/* Mobile menu button */}
      <button
        onClick={() => setMobileSidebarOpen(true)}
        className="p-2 mr-2 hover:bg-[#262626] rounded-lg lg:hidden"
      >
        <Menu className="h-5 w-5 text-[#a1a1a1]" />
      </button>

      {/* Breadcrumbs */}
      <nav className="flex items-center gap-1 text-sm overflow-x-auto">
        {breadcrumbs.map((crumb, index) => (
          <div key={crumb.href} className="flex items-center gap-1 shrink-0">
            {index > 0 && (
              <ChevronRight className="h-4 w-4 text-[#525252] shrink-0" />
            )}
            {index === breadcrumbs.length - 1 ? (
              <span className="text-white font-medium">{crumb.label}</span>
            ) : (
              <Link
                href={crumb.href}
                className="text-[#a1a1a1] hover:text-white transition-colors"
              >
                {crumb.label}
              </Link>
            )}
          </div>
        ))}
      </nav>

      {/* Right side actions */}
      <div className="ml-auto flex items-center gap-3">
        {/* Upload PDF button */}
        <button className="hidden sm:flex items-center gap-2 px-4 py-2 bg-[#7c3aed] hover:bg-[#6d28d9] text-white text-sm font-medium rounded-lg transition-colors">
          <Upload className="h-4 w-4" />
          <span>Upload PDF</span>
        </button>

        {/* User avatar */}
        <button className="flex items-center justify-center h-9 w-9 bg-[#262626] hover:bg-[#333333] rounded-full transition-colors">
          <User className="h-5 w-5 text-[#a1a1a1]" />
        </button>
      </div>
    </header>
  );
}
