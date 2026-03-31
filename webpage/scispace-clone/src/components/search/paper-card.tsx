"use client";

import { FileText, MessageSquare, Quote, ExternalLink } from "lucide-react";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import type { Paper } from "@/lib/api/semantic-scholar";

interface PaperCardProps {
  paper: Paper;
  onOpenInChat?: (paper: Paper) => void;
  className?: string;
}

export function PaperCard({ paper, onOpenInChat, className }: PaperCardProps) {
  // Truncate abstract to a reasonable length
  const truncatedAbstract = paper.abstract
    ? paper.abstract.length > 300
      ? paper.abstract.slice(0, 300) + "..."
      : paper.abstract
    : "No abstract available.";

  // Format authors list
  const authorsList =
    paper.authors.length > 0
      ? paper.authors
          .slice(0, 5)
          .map((a) => a.name)
          .join(", ") +
        (paper.authors.length > 5 ? ` +${paper.authors.length - 5} more` : "")
      : "Unknown authors";

  return (
    <Card
      className={cn(
        "bg-[#171717] border-[#333333] hover:border-[#525252] transition-colors",
        className
      )}
    >
      <CardHeader className="pb-2">
        <div className="flex items-start justify-between gap-4">
          <div className="flex-1 min-w-0">
            {/* Paper title */}
            <a
              href={`https://www.semanticscholar.org/paper/${paper.paperId}`}
              target="_blank"
              rel="noopener noreferrer"
              className="text-lg font-semibold text-white hover:text-[#7c3aed] transition-colors line-clamp-2"
            >
              {paper.title}
            </a>

            {/* Authors */}
            <p className="mt-1 text-sm text-[#a1a1a1] line-clamp-1">{authorsList}</p>

            {/* Year and venue */}
            <div className="flex items-center gap-2 mt-2 flex-wrap">
              {paper.year && (
                <Badge
                  variant="secondary"
                  className="bg-[#262626] text-[#a1a1a1] border-0"
                >
                  {paper.year}
                </Badge>
              )}
              {paper.venue && (
                <Badge
                  variant="secondary"
                  className="bg-[#262626] text-[#a1a1a1] border-0"
                >
                  {paper.venue}
                </Badge>
              )}
              {paper.externalId && (
                <Badge
                  variant="outline"
                  className="border-[#333333] text-[#525252]"
                >
                  {paper.externalId.startsWith("arXiv:")
                    ? "arXiv"
                    : paper.externalId}
                </Badge>
              )}
            </div>
          </div>

          {/* Citation count */}
          <div className="flex flex-col items-center shrink-0">
            <div className="flex items-center gap-1 text-[#7c3aed]">
              <Quote className="h-4 w-4" />
              <span className="font-semibold">
                {paper.citationCount >= 1000
                  ? `${(paper.citationCount / 1000).toFixed(1)}k`
                  : paper.citationCount}
              </span>
            </div>
            <span className="text-xs text-[#525252]">citations</span>
          </div>
        </div>
      </CardHeader>

      <CardContent className="pt-2">
        {/* Abstract preview */}
        <p className="text-sm text-[#a1a1a1] leading-relaxed line-clamp-3">
          {truncatedAbstract}
        </p>

        {/* Actions */}
        <div className="flex items-center gap-2 mt-4">
          <Button
            variant="outline"
            size="sm"
            className="border-[#333333] bg-[#262626] hover:bg-[#333333] text-white"
            onClick={() =>
              window.open(
                `https://www.semanticscholar.org/paper/${paper.paperId}`,
                "_blank"
              )
            }
          >
            <ExternalLink className="h-4 w-4 mr-1.5" />
            View Paper
          </Button>

          {onOpenInChat && (
            <Button
              variant="default"
              size="sm"
              className="bg-[#7c3aed] hover:bg-[#6d28d9] text-white"
              onClick={() => onOpenInChat(paper)}
            >
              <MessageSquare className="h-4 w-4 mr-1.5" />
              Open in Chat
            </Button>
          )}

          {paper.url && (
            <Button
              variant="ghost"
              size="sm"
              className="text-[#a1a1a1] hover:text-white"
              onClick={() => window.open(paper.url, "_blank")}
            >
              <FileText className="h-4 w-4 mr-1.5" />
              PDF
            </Button>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
