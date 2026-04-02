'use client';

import { useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import 'katex/dist/katex.min.css';
import { FileText, Loader2 } from 'lucide-react';

interface MarkdownViewerProps {
  content: string | null;
  isLoading?: boolean;
}

export default function MarkdownViewer({
  content,
  isLoading = false,
}: MarkdownViewerProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  // Scroll to top when content changes
  useEffect(() => {
    if (containerRef.current) {
      containerRef.current.scrollTop = 0;
    }
  }, [content]);

  if (isLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-full bg-zinc-900 rounded-xl border border-zinc-700">
        <Loader2 className="w-8 h-8 text-violet-400 animate-spin mb-3" />
        <p className="text-zinc-400 text-sm">Loading markdown...</p>
      </div>
    );
  }

  if (!content) {
    return (
      <div className="flex flex-col items-center justify-center h-full bg-zinc-900 rounded-xl border border-zinc-700">
        <FileText className="w-16 h-16 text-zinc-600 mb-4" />
        <p className="text-zinc-400 text-lg">No markdown content</p>
        <p className="text-zinc-500 text-sm mt-1">
          Process a PDF with MinerU to generate transcript
        </p>
      </div>
    );
  }

  return (
    <div
      ref={containerRef}
      className="h-full overflow-y-auto bg-zinc-900 rounded-xl border border-zinc-700"
    >
      <div className="p-6 max-w-4xl mx-auto">
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          rehypePlugins={[rehypeKatex]}
          components={{
            // Headings
            h1: ({ children }) => (
              <h1 className="text-2xl font-bold text-white mt-8 mb-4 pb-2 border-b border-zinc-700 first:mt-0">
                {children}
              </h1>
            ),
            h2: ({ children }) => (
              <h2 className="text-xl font-semibold text-white mt-6 mb-3">
                {children}
              </h2>
            ),
            h3: ({ children }) => (
              <h3 className="text-lg font-medium text-zinc-200 mt-4 mb-2">
                {children}
              </h3>
            ),
            h4: ({ children }) => (
              <h4 className="text-base font-medium text-zinc-300 mt-3 mb-2">
                {children}
              </h4>
            ),
            // Paragraphs
            p: ({ children }) => (
              <p className="text-zinc-300 leading-relaxed mb-4">{children}</p>
            ),
            // Lists
            ul: ({ children }) => (
              <ul className="list-disc list-inside text-zinc-300 mb-4 space-y-1">
                {children}
              </ul>
            ),
            ol: ({ children }) => (
              <ol className="list-decimal list-inside text-zinc-300 mb-4 space-y-1">
                {children}
              </ol>
            ),
            li: ({ children }) => (
              <li className="text-zinc-300 leading-relaxed">{children}</li>
            ),
            // Code blocks
            code: ({ className, children, ...props }) => {
              const isInline = !className;
              if (isInline) {
                return (
                  <code
                    className="px-1.5 py-0.5 bg-zinc-800 text-violet-300 rounded text-sm font-mono"
                    {...props}
                  >
                    {children}
                  </code>
                );
              }
              return (
                <code className={`${className} block`} {...props}>
                  {children}
                </code>
              );
            },
            pre: ({ children }) => (
              <pre className="bg-zinc-800 border border-zinc-700 rounded-lg p-4 mb-4 overflow-x-auto">
                {children}
              </pre>
            ),
            // Tables
            table: ({ children }) => (
              <div className="overflow-x-auto mb-4">
                <table className="min-w-full border border-zinc-700 rounded-lg overflow-hidden">
                  {children}
                </table>
              </div>
            ),
            thead: ({ children }) => (
              <thead className="bg-zinc-800">{children}</thead>
            ),
            th: ({ children }) => (
              <th className="px-4 py-2 text-left text-zinc-200 font-medium border-b border-zinc-700">
                {children}
              </th>
            ),
            td: ({ children }) => (
              <td className="px-4 py-2 text-zinc-300 border-b border-zinc-700">
                {children}
              </td>
            ),
            tr: ({ children }) => (
              <tr className="even:bg-zinc-800/50 hover:bg-zinc-800">
                {children}
              </tr>
            ),
            // Blockquotes
            blockquote: ({ children }) => (
              <blockquote className="border-l-4 border-violet-500 pl-4 py-2 my-4 bg-zinc-800/50 rounded-r-lg">
                {children}
              </blockquote>
            ),
            // Links
            a: ({ href, children }) => (
              <a
                href={href}
                target="_blank"
                rel="noopener noreferrer"
                className="text-violet-400 hover:text-violet-300 underline"
              >
                {children}
              </a>
            ),
            // Emphasis
            strong: ({ children }) => (
              <strong className="font-semibold text-white">{children}</strong>
            ),
            em: ({ children }) => (
              <em className="italic text-zinc-300">{children}</em>
            ),
            // Horizontal rules
            hr: () => <hr className="border-zinc-700 my-6" />,
            // KaTeX specific styling
            span: ({ className, children, ...props }) => {
              // Check if this is a KaTeX element
              if (className?.startsWith('katex')) {
                return (
                  <span className={className} {...props}>
                    {children}
                  </span>
                );
              }
              return (
                <span className={className} {...props}>
                  {children}
                </span>
              );
            },
          }}
        >
          {content}
        </ReactMarkdown>
      </div>
    </div>
  );
}
