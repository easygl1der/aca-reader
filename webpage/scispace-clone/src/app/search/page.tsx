"use client";

import { useState, useEffect, useCallback } from "react";
import { SearchBar } from "@/components/search/search-bar";
import { PaperCard } from "@/components/search/paper-card";
import { Filters, FilterState } from "@/components/search/filters";
import { Button } from "@/components/ui/button";
import { searchPapers, type Paper, type SearchResult } from "@/lib/api/semantic-scholar";
import { ChevronLeft, ChevronRight, FileQuestion } from "lucide-react";
import { useRouter } from "next/navigation";
import { cn } from "@/lib/utils";

const ITEMS_PER_PAGE = 10;

export default function SearchPage() {
  const router = useRouter();
  const [query, setQuery] = useState("");
  const [searchQuery, setSearchQuery] = useState("");
  const [filters, setFilters] = useState<FilterState>({});
  const [result, setResult] = useState<SearchResult | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [hasSearched, setHasSearched] = useState(false);

  // Perform search
  const performSearch = useCallback(
    async (q: string, f: FilterState, offset: number = 0) => {
      if (!q.trim()) return;

      setIsLoading(true);
      setHasSearched(true);

      try {
        const searchResult = await searchPapers(
          { query: q, ...f },
          ITEMS_PER_PAGE,
          offset
        );
        setResult(searchResult);
      } catch (error) {
        console.error("Search error:", error);
        setResult(null);
      } finally {
        setIsLoading(false);
      }
    },
    []
  );

  // Handle search submit
  const handleSearch = (q: string) => {
    setSearchQuery(q);
    setCurrentPage(1);
    performSearch(q, filters, 0);
  };

  // Handle filter change
  const handleFilterChange = (newFilters: FilterState) => {
    setFilters(newFilters);
    if (searchQuery) {
      setCurrentPage(1);
      performSearch(searchQuery, newFilters, 0);
    }
  };

  // Handle page change
  const handlePageChange = (page: number) => {
    setCurrentPage(page);
    const offset = (page - 1) * ITEMS_PER_PAGE;
    performSearch(searchQuery, filters, offset);
    // Scroll to top of results
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  // Handle paper open in chat
  const handleOpenInChat = (paper: Paper) => {
    // In a real implementation, this would navigate to chat-pdf with the paper pre-loaded
    console.log("Open paper in chat:", paper.title);
    // For now, just log and show feedback
    alert(`Paper "${paper.title}" would be opened in Chat with PDF for analysis.`);
  };

  // Calculate pagination
  const totalPages = result ? Math.ceil(result.total / ITEMS_PER_PAGE) : 0;
  const startItem = result ? result.offset + 1 : 0;
  const endItem = result ? Math.min(result.offset + ITEMS_PER_PAGE, result.total) : 0;

  // Generate page numbers to display
  const getPageNumbers = () => {
    const pages: (number | "ellipsis")[] = [];
    if (totalPages <= 7) {
      for (let i = 1; i <= totalPages; i++) pages.push(i);
    } else {
      pages.push(1);
      if (currentPage > 3) pages.push("ellipsis");
      for (
        let i = Math.max(2, currentPage - 1);
        i <= Math.min(totalPages - 1, currentPage + 1);
        i++
      ) {
        pages.push(i);
      }
      if (currentPage < totalPages - 2) pages.push("ellipsis");
      pages.push(totalPages);
    }
    return pages;
  };

  return (
    <div className="min-h-screen bg-[#0a0a0a]">
      {/* Hero section with search */}
      <div className="bg-gradient-to-b from-[#171717] to-[#0a0a0a] border-b border-[#333333]">
        <div className="max-w-5xl mx-auto px-4 py-12 pt-16">
          {/* Page title */}
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold text-white mb-2">
              Search Academic Papers
            </h1>
            <p className="text-[#a1a1a1]">
              Discover research papers from Semantic Scholar&apos;s database of over 200
              million papers
            </p>
          </div>

          {/* Search bar */}
          <SearchBar
            value={query}
            onChange={setQuery}
            onSubmit={handleSearch}
            isLoading={isLoading}
            className="mx-auto"
          />
        </div>
      </div>

      {/* Filters */}
      <div className="max-w-5xl mx-auto px-4 py-4">
        <Filters filters={filters} onChange={handleFilterChange} />
      </div>

      {/* Results section */}
      <div className="max-w-5xl mx-auto px-4 py-6">
        {/* Initial state - no search yet */}
        {!hasSearched && !isLoading && (
          <div className="flex flex-col items-center justify-center py-20 text-center">
            <FileQuestion className="h-16 w-16 text-[#333333] mb-4" />
            <h2 className="text-xl font-medium text-white mb-2">
              Start Your Search
            </h2>
            <p className="text-[#a1a1a1] max-w-md">
              Enter keywords, author names, or topics to discover relevant academic
              papers from leading conferences and journals.
            </p>
          </div>
        )}

        {/* Loading state */}
        {isLoading && (
          <div className="flex flex-col items-center justify-center py-20">
            <div className="relative w-16 h-16 mb-4">
              <div className="absolute inset-0 border-4 border-[#262626] rounded-full" />
              <div className="absolute inset-0 border-4 border-t-[#7c3aed] rounded-full animate-spin" />
            </div>
            <p className="text-[#a1a1a1]">Searching papers...</p>
          </div>
        )}

        {/* Results */}
        {!isLoading && result && (
          <>
            {/* Results header */}
            <div className="flex items-center justify-between mb-6">
              <div className="text-sm text-[#a1a1a1]">
                {result.total > 0 ? (
                  <>
                    Showing{" "}
                    <span className="text-white font-medium">{startItem}</span>-
                    <span className="text-white font-medium">{endItem}</span> of{" "}
                    <span className="text-white font-medium">{result.total}</span>{" "}
                    results
                    {searchQuery && (
                      <span className="ml-2">
                        for &quot;<span className="text-[#7c3aed]">{searchQuery}</span>
                        &quot;
                      </span>
                    )}
                  </>
                ) : (
                  <>No results found</>
                )}
              </div>
            </div>

            {/* Paper list */}
            {result.papers.length > 0 ? (
              <div className="space-y-4">
                {result.papers.map((paper) => (
                  <PaperCard
                    key={paper.paperId}
                    paper={paper}
                    onOpenInChat={handleOpenInChat}
                  />
                ))}
              </div>
            ) : (
              <div className="flex flex-col items-center justify-center py-20 text-center">
                <FileQuestion className="h-16 w-16 text-[#333333] mb-4" />
                <h2 className="text-xl font-medium text-white mb-2">
                  No Papers Found
                </h2>
                <p className="text-[#a1a1a1] max-w-md">
                  Try adjusting your search terms or filters to find more relevant
                  papers.
                </p>
              </div>
            )}

            {/* Pagination */}
            {totalPages > 1 && (
              <div className="flex items-center justify-center gap-2 mt-8">
                <Button
                  variant="outline"
                  size="icon"
                  onClick={() => handlePageChange(currentPage - 1)}
                  disabled={currentPage === 1}
                  className="border-[#333333] bg-[#171717] hover:bg-[#262626] disabled:opacity-50"
                >
                  <ChevronLeft className="h-4 w-4" />
                </Button>

                <div className="flex items-center gap-1">
                  {getPageNumbers().map((page, index) =>
                    page === "ellipsis" ? (
                      <span
                        key={`ellipsis-${index}`}
                        className="px-2 text-[#525252]"
                      >
                        ...
                      </span>
                    ) : (
                      <Button
                        key={page}
                        variant={currentPage === page ? "default" : "outline"}
                        size="sm"
                        onClick={() => handlePageChange(page)}
                        className={cn(
                          "min-w-9",
                          currentPage === page
                            ? "bg-[#7c3aed] hover:bg-[#6d28d9] text-white"
                            : "border-[#333333] bg-[#171717] hover:bg-[#262626] text-[#a1a1a1]"
                        )}
                      >
                        {page}
                      </Button>
                    )
                  )}
                </div>

                <Button
                  variant="outline"
                  size="icon"
                  onClick={() => handlePageChange(currentPage + 1)}
                  disabled={currentPage === totalPages}
                  className="border-[#333333] bg-[#171717] hover:bg-[#262626] disabled:opacity-50"
                >
                  <ChevronRight className="h-4 w-4" />
                </Button>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
