"use client";

import { useState } from "react";
import { Filter, ChevronDown, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";
import { getCommonVenues } from "@/lib/api/semantic-scholar";

export interface FilterState {
  yearFrom?: number;
  yearTo?: number;
  venue?: string;
  minCitations?: number;
  openAccessOnly?: boolean;
}

interface FiltersProps {
  filters: FilterState;
  onChange: (filters: FilterState) => void;
  className?: string;
}

const CURRENT_YEAR = new Date().getFullYear();
const YEARS = Array.from({ length: CURRENT_YEAR - 1950 + 1 }, (_, i) => CURRENT_YEAR - i);
const VENUES = getCommonVenues();

export function Filters({ filters, onChange, className }: FiltersProps) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [localFilters, setLocalFilters] = useState<FilterState>(filters);

  const handleApply = () => {
    onChange(localFilters);
    setIsExpanded(false);
  };

  const handleReset = () => {
    const resetFilters: FilterState = {};
    setLocalFilters(resetFilters);
    onChange(resetFilters);
    setIsExpanded(false);
  };

  const handleYearFromChange = (value: string) => {
    const year = value ? parseInt(value, 10) : undefined;
    setLocalFilters({ ...localFilters, yearFrom: year });
  };

  const handleYearToChange = (value: string) => {
    const year = value ? parseInt(value, 10) : undefined;
    setLocalFilters({ ...localFilters, yearTo: year });
  };

  const handleVenueChange = (value: string) => {
    setLocalFilters({ ...localFilters, venue: value || undefined });
  };

  const handleCitationsChange = (value: number) => {
    setLocalFilters({ ...localFilters, minCitations: value || undefined });
  };

  const handleOpenAccessToggle = () => {
    setLocalFilters({ ...localFilters, openAccessOnly: !localFilters.openAccessOnly });
  };

  // Count active filters
  const activeFilterCount = [
    filters.yearFrom,
    filters.yearTo,
    filters.venue,
    filters.minCitations,
    filters.openAccessOnly,
  ].filter(Boolean).length;

  return (
    <div className={cn("w-full", className)}>
      {/* Filter toggle bar */}
      <div className="flex items-center justify-between gap-4 py-3">
        <div className="flex items-center gap-2">
          <Filter className="h-4 w-4 text-[#a1a1a1]" />
          <span className="text-sm font-medium text-white">Filters</span>
          {activeFilterCount > 0 && (
            <Badge className="bg-[#7c3aed] text-white">{activeFilterCount}</Badge>
          )}
        </div>

        <Button
          variant="ghost"
          size="sm"
          onClick={() => setIsExpanded(!isExpanded)}
          className="text-[#a1a1a1] hover:text-white"
        >
          <span className="mr-1">Options</span>
          <ChevronDown
            className={cn(
              "h-4 w-4 transition-transform",
              isExpanded && "rotate-180"
            )}
          />
        </Button>
      </div>

      {/* Expanded filter panel */}
      {isExpanded && (
        <div className="bg-[#171717] border border-[#333333] rounded-xl p-4 mt-2">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {/* Year range filter */}
            <div className="space-y-2">
              <label className="text-sm font-medium text-[#a1a1a1]">
                Year Range
              </label>
              <div className="flex items-center gap-2">
                <select
                  value={localFilters.yearFrom || ""}
                  onChange={(e) => handleYearFromChange(e.target.value)}
                  className="flex-1 h-9 px-3 bg-[#262626] border border-[#333333] rounded-lg text-sm text-white focus:border-[#7c3aed] focus:outline-none"
                >
                  <option value="">From</option>
                  {YEARS.map((year) => (
                    <option key={year} value={year}>
                      {year}
                    </option>
                  ))}
                </select>
                <span className="text-[#525252]">-</span>
                <select
                  value={localFilters.yearTo || ""}
                  onChange={(e) => handleYearToChange(e.target.value)}
                  className="flex-1 h-9 px-3 bg-[#262626] border border-[#333333] rounded-lg text-sm text-white focus:border-[#7c3aed] focus:outline-none"
                >
                  <option value="">To</option>
                  {YEARS.map((year) => (
                    <option key={year} value={year}>
                      {year}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            {/* Venue filter */}
            <div className="space-y-2">
              <label className="text-sm font-medium text-[#a1a1a1]">Venue</label>
              <select
                value={localFilters.venue || ""}
                onChange={(e) => handleVenueChange(e.target.value)}
                className="w-full h-9 px-3 bg-[#262626] border border-[#333333] rounded-lg text-sm text-white focus:border-[#7c3aed] focus:outline-none"
              >
                <option value="">All Venues</option>
                {VENUES.map((venue) => (
                  <option key={venue} value={venue}>
                    {venue}
                  </option>
                ))}
              </select>
            </div>

            {/* Min citations slider */}
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <label className="text-sm font-medium text-[#a1a1a1]">
                  Min Citations
                </label>
                <span className="text-sm text-[#7c3aed]">
                  {localFilters.minCitations || 0}
                </span>
              </div>
              <input
                type="range"
                min="0"
                max="10000"
                step="100"
                value={localFilters.minCitations || 0}
                onChange={(e) => handleCitationsChange(parseInt(e.target.value, 10))}
                className="w-full h-2 bg-[#262626] rounded-lg appearance-none cursor-pointer accent-[#7c3aed]"
              />
              <div className="flex justify-between text-xs text-[#525252]">
                <span>0</span>
                <span>10k+</span>
              </div>
            </div>

            {/* Open access toggle */}
            <div className="space-y-2">
              <label className="text-sm font-medium text-[#a1a1a1]">
                Access Type
              </label>
              <button
                type="button"
                onClick={handleOpenAccessToggle}
                className={cn(
                  "w-full h-9 px-4 rounded-lg border text-sm font-medium transition-colors",
                  localFilters.openAccessOnly
                    ? "bg-[#7c3aed] border-[#7c3aed] text-white"
                    : "bg-[#262626] border-[#333333] text-[#a1a1a1] hover:border-[#525252]"
                )}
              >
                {localFilters.openAccessOnly ? "Open Access Only" : "All Papers"}
              </button>
            </div>
          </div>

          {/* Active filter badges */}
          {activeFilterCount > 0 && (
            <div className="flex flex-wrap gap-2 mt-4 pt-4 border-t border-[#333333]">
              {localFilters.yearFrom && (
                <Badge
                  variant="secondary"
                  className="bg-[#262626] text-white gap-1 pr-1"
                >
                  From {localFilters.yearFrom}
                  <button
                    onClick={() =>
                      setLocalFilters({ ...localFilters, yearFrom: undefined })
                    }
                    className="ml-1 p-0.5 hover:bg-[#333333] rounded"
                  >
                    <X className="h-3 w-3" />
                  </button>
                </Badge>
              )}
              {localFilters.yearTo && (
                <Badge
                  variant="secondary"
                  className="bg-[#262626] text-white gap-1 pr-1"
                >
                  To {localFilters.yearTo}
                  <button
                    onClick={() =>
                      setLocalFilters({ ...localFilters, yearTo: undefined })
                    }
                    className="ml-1 p-0.5 hover:bg-[#333333] rounded"
                  >
                    <X className="h-3 w-3" />
                  </button>
                </Badge>
              )}
              {localFilters.venue && (
                <Badge
                  variant="secondary"
                  className="bg-[#262626] text-white gap-1 pr-1"
                >
                  {localFilters.venue}
                  <button
                    onClick={() =>
                      setLocalFilters({ ...localFilters, venue: undefined })
                    }
                    className="ml-1 p-0.5 hover:bg-[#333333] rounded"
                  >
                    <X className="h-3 w-3" />
                  </button>
                </Badge>
              )}
              {localFilters.minCitations && (
                <Badge
                  variant="secondary"
                  className="bg-[#262626] text-white gap-1 pr-1"
                >
                  {localFilters.minCitations}+ citations
                  <button
                    onClick={() =>
                      setLocalFilters({ ...localFilters, minCitations: undefined })
                    }
                    className="ml-1 p-0.5 hover:bg-[#333333] rounded"
                  >
                    <X className="h-3 w-3" />
                  </button>
                </Badge>
              )}
              {localFilters.openAccessOnly && (
                <Badge
                  variant="secondary"
                  className="bg-[#262626] text-white gap-1 pr-1"
                >
                  Open Access
                  <button
                    onClick={() =>
                      setLocalFilters({
                        ...localFilters,
                        openAccessOnly: false,
                      })
                    }
                    className="ml-1 p-0.5 hover:bg-[#333333] rounded"
                  >
                    <X className="h-3 w-3" />
                  </button>
                </Badge>
              )}
            </div>
          )}

          {/* Action buttons */}
          <div className="flex justify-end gap-2 mt-4">
            <Button
              variant="ghost"
              size="sm"
              onClick={handleReset}
              className="text-[#a1a1a1] hover:text-white"
            >
              Reset
            </Button>
            <Button
              variant="default"
              size="sm"
              onClick={handleApply}
              className="bg-[#7c3aed] hover:bg-[#6d28d9] text-white"
            >
              Apply Filters
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}
