"use client";

import { Search, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { cn } from "@/lib/utils";

interface SearchBarProps {
  value: string;
  onChange: (value: string) => void;
  onSubmit: (value: string) => void;
  isLoading?: boolean;
  className?: string;
}

export function SearchBar({
  value,
  onChange,
  onSubmit,
  isLoading = false,
  className,
}: SearchBarProps) {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (value.trim()) {
      onSubmit(value.trim());
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && value.trim()) {
      onSubmit(value.trim());
    }
  };

  const handleClear = () => {
    onChange("");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className={cn(
        "flex w-full max-w-3xl items-center gap-2",
        className
      )}
    >
      <div className="relative flex-1">
        <Search className="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-[#525252]" />
        <Input
          type="text"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Search for papers, authors, topics..."
          className="h-14 pl-12 pr-12 bg-[#171717] border-[#333333] text-white text-lg rounded-xl focus:border-[#7c3aed] focus:ring-[#7c3aed]/20 placeholder:text-[#525252]"
        />
        {value && (
          <button
            type="button"
            onClick={handleClear}
            className="absolute right-4 top-1/2 -translate-y-1/2 p-1 hover:bg-[#262626] rounded-full transition-colors"
          >
            <X className="h-4 w-4 text-[#a1a1a1]" />
          </button>
        )}
      </div>
      <Button
        type="submit"
        disabled={isLoading || !value.trim()}
        className="h-14 px-8 bg-[#7c3aed] hover:bg-[#6d28d9] text-white font-medium rounded-xl transition-colors disabled:opacity-50"
      >
        {isLoading ? (
          <span className="flex items-center gap-2">
            <svg
              className="animate-spin h-5 w-5"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              />
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              />
            </svg>
            Searching
          </span>
        ) : (
          "Search"
        )}
      </Button>
    </form>
  );
}
