"use client";

import { useState, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  FileText,
  MessageSquare,
  Network,
  ChevronRight,
  Download,
  Maximize2,
  ZoomIn,
  ZoomOut,
  Search,
  Bookmark,
  Highlighter,
  Home,
  Library,
  FileCheck,
  GitGraph,
  Settings,
  PanelLeftClose,
  PanelLeft,
} from "lucide-react";

const documentContent = {
  title: "What is prompt injection?",
  source: "LLM Security - NIST",
  page: "24 of 156",
  content: `Prompt injection is a security vulnerability that occurs when an attacker manipulates the input to a large language model (LLM) to cause unintended behavior. Unlike traditional code injection, prompt injection targets the application's use of the LLM rather than the model itself.

The attack works by crafting inputs that include malicious instructions designed to override the system's original instructions. These can be delivered through:

• User-provided text inputs
• Data from external sources used in prompt construction
• Third-party content integrated into prompts

Common attack vectors include the injection of commands disguised as user instructions, the extraction of sensitive information through carefully constructed queries, and the manipulation of model outputs for malicious purposes.

Defensive measures should include input validation, output filtering, and the use of separate contexts for trusted and untrusted content.`,
};

interface Entity {
  id: string;
  text: string;
  type: "concept" | "risk" | "mitigation" | "reference";
  start: number;
  end: number;
}

const entities: Entity[] = [
  { id: "1", text: "prompt injection", type: "concept", start: 0, end: 17 },
  { id: "2", text: "security vulnerability", type: "risk", start: 32, end: 53 },
  { id: "3", text: "LLM", type: "concept", start: 87, end: 90 },
  { id: "4", text: "input validation", type: "mitigation", start: 892, end: 908 },
  { id: "5", text: "NIST", type: "reference", start: 45, end: 49 },
];

const relatedConcepts = [
  { id: "1", label: "LLM Security", type: "core" },
  { id: "2", label: "Adversarial Attacks", type: "branch" },
  { id: "3", label: "AI Alignment", type: "branch" },
  { id: "4", label: "Safety Measures", type: "branch" },
  { id: "5", label: "Red Teaming", type: "leaf" },
  { id: "6", label: "Output Filtering", type: "leaf" },
];

const entityColorMap: Record<Entity["type"], { bg: string; text: string; border: string }> = {
  concept: { bg: "bg-purple-100", text: "text-purple-700", border: "border-purple-300" },
  risk: { bg: "bg-red-100", text: "text-red-700", border: "border-red-300" },
  mitigation: { bg: "bg-green-100", text: "text-green-700", border: "border-green-300" },
  reference: { bg: "bg-blue-100", text: "text-blue-700", border: "border-blue-300" },
};

function HighlightedText({ text }: { text: string }) {
  const entityList = entities;

  if (entityList.length === 0) return <>{text}</>;

  // Sort by text length descending to match longer phrases first
  const sorted = [...entityList].sort((a, b) => b.text.length - a.text.length);

  // Build a regex pattern that matches any entity text (case insensitive)
  const escapedPatterns = sorted.map((e) =>
    e.text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
  );
  const pattern = new RegExp(escapedPatterns.join("|"), "gi");

  const parts: React.ReactNode[] = [];
  let lastIndex = 0;
  let match: RegExpExecArray | null;
  let keyIdx = 0;

  while ((match = pattern.exec(text)) !== null) {
    // Add text before the match
    if (match.index > lastIndex) {
      parts.push(text.slice(lastIndex, match.index));
    }

    // Find which entity matched
    const matchedText = match[0];
    const entity = sorted.find(
      (e) => e.text.toLowerCase() === matchedText.toLowerCase()
    );

    if (entity) {
      const colors = entityColorMap[entity.type];
      parts.push(
        <span
          key={`entity-${keyIdx++}`}
          className={`px-1 py-0.5 rounded border font-medium ${colors.bg} ${colors.text} ${colors.border}`}
          title={`${entity.type}: ${entity.text}`}
        >
          {matchedText}
        </span>
      );
    } else {
      parts.push(matchedText);
    }

    lastIndex = pattern.lastIndex;
  }

  // Add remaining text
  if (lastIndex < text.length) {
    parts.push(text.slice(lastIndex));
  }

  return <>{parts}</>;
}

function renderBlock(block: string): React.ReactNode {
  if (block.startsWith("•")) {
    // Bullet point
    const content = block.replace(/^[•]\s*/, "");
    return (
      <li className="ml-4 mb-2 text-gray-700 leading-relaxed">
        <HighlightedText text={content} />
      </li>
    );
  }
  // Regular paragraph
  return (
    <p className="text-gray-700 leading-relaxed mb-4">
      <HighlightedText text={block} />
    </p>
  );
}

export default function DocumentViewer() {
  const [activeTab, setActiveTab] = useState<"chat" | "graph">("chat");
  const [zoom, setZoom] = useState(100);
  const [selectedEntity, setSelectedEntity] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  const sidebarLinks = [
    { icon: Home, label: "Home", href: "/" },
    { icon: Library, label: "Library", href: "#" },
    { icon: FileCheck, label: "Documents", href: "/navigator/document", active: true },
    { icon: GitGraph, label: "Knowledge Graph", href: "/navigator" },
    { icon: Settings, label: "Settings", href: "#" },
  ];

  const contentBlocks = useMemo(() => {
    return documentContent.content.split(/\n\n/);
  }, []);

  return (
    <div className="h-screen flex flex-col bg-gray-50">
      {/* Top Bar */}
      <div className="bg-white border-b border-gray-200 px-4 py-3 flex-shrink-0">
        <div className="flex items-center justify-between">
          {/* Left: Sidebar toggle + Document info */}
          <div className="flex items-center gap-4">
            <button
              onClick={() => setIsSidebarOpen(!isSidebarOpen)}
              className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
            >
              {isSidebarOpen ? (
                <PanelLeftClose className="w-5 h-5 text-gray-500" />
              ) : (
                <PanelLeft className="w-5 h-5 text-gray-500" />
              )}
            </button>

            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-primary to-primary-light flex items-center justify-center">
                <FileText className="w-5 h-5 text-white" />
              </div>
              <div>
                <h1 className="font-semibold text-gray-900 text-lg leading-tight">
                  {documentContent.title}
                </h1>
                <p className="text-sm text-gray-500">
                  {documentContent.source} · Page {documentContent.page}
                </p>
              </div>
            </div>
          </div>

          {/* Right: Action buttons */}
          <div className="flex items-center gap-1">
            <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors group" title="Bookmark">
              <Bookmark className="w-4 h-4 text-gray-500 group-hover:text-primary" />
            </button>
            <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors group" title="Highlight">
              <Highlighter className="w-4 h-4 text-gray-500 group-hover:text-primary" />
            </button>
            <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors group" title="Download">
              <Download className="w-4 h-4 text-gray-500 group-hover:text-primary" />
            </button>
            <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors group" title="Maximize">
              <Maximize2 className="w-4 h-4 text-gray-500 group-hover:text-primary" />
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex overflow-hidden">
        {/* Left Sidebar */}
        <AnimatePresence>
          {isSidebarOpen && (
            <motion.aside
              initial={{ width: 0, opacity: 0 }}
              animate={{ width: 220, opacity: 1 }}
              exit={{ width: 0, opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="bg-white border-r border-gray-200 flex flex-col overflow-hidden"
            >
              <div className="p-4 flex flex-col gap-1">
                {sidebarLinks.map((link) => (
                  <a
                    key={link.label}
                    href={link.href}
                    className={`flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors ${
                      link.active
                        ? "bg-primary/10 text-primary"
                        : "text-gray-600 hover:bg-gray-50 hover:text-gray-900"
                    }`}
                  >
                    <link.icon className="w-4 h-4" />
                    {link.label}
                  </a>
                ))}
              </div>

              {/* Legend at bottom */}
              <div className="mt-auto p-4 border-t border-gray-100">
                <p className="text-xs font-medium text-gray-500 uppercase mb-2">Legend</p>
                <div className="space-y-1.5">
                  {([
                    { type: "concept" as const, label: "Concept" },
                    { type: "risk" as const, label: "Risk" },
                    { type: "mitigation" as const, label: "Mitigation" },
                    { type: "reference" as const, label: "Reference" },
                  ]).map(({ type, label }) => {
                    const colors = entityColorMap[type];
                    return (
                      <div key={type} className="flex items-center gap-2">
                        <span className={`w-3 h-3 rounded-sm ${colors.bg} ${colors.border} border`} />
                        <span className="text-xs text-gray-600">{label}</span>
                      </div>
                    );
                  })}
                </div>
              </div>
            </motion.aside>
          )}
        </AnimatePresence>

        {/* Document Panel */}
        <div className="flex-1 flex flex-col border-r border-gray-200">
          {/* Document Toolbar */}
          <div className="bg-white border-b border-gray-200 px-4 py-2 flex items-center justify-between flex-shrink-0">
            <div className="flex items-center gap-4">
              <div className="relative">
                <Search className="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Search in document..."
                  className="pl-9 pr-4 py-1.5 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary w-64"
                />
              </div>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => setZoom(Math.max(50, zoom - 25))}
                className="p-1.5 hover:bg-gray-100 rounded transition-colors"
              >
                <ZoomOut className="w-4 h-4 text-gray-500" />
              </button>
              <span className="text-sm text-gray-600 w-14 text-center font-medium">{zoom}%</span>
              <button
                onClick={() => setZoom(Math.min(200, zoom + 25))}
                className="p-1.5 hover:bg-gray-100 rounded transition-colors"
              >
                <ZoomIn className="w-4 h-4 text-gray-500" />
              </button>
            </div>
          </div>

          {/* Document Content */}
          <div className="flex-1 overflow-auto p-8">
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              className="max-w-3xl mx-auto bg-white rounded-xl shadow-sm border border-gray-200 p-8"
              style={{ transform: `scale(${zoom / 100})`, transformOrigin: "top center" }}
            >
              <h1 className="text-2xl font-bold text-gray-900 mb-6">
                {documentContent.title}
              </h1>

              <div className="prose prose-gray max-w-none">
                {contentBlocks.map((block, idx) => (
                  <div key={idx}>{renderBlock(block)}</div>
                ))}
              </div>
            </motion.div>
          </div>
        </div>

        {/* Right Panel */}
        <div className="w-96 bg-white flex flex-col">
          {/* Tab Switcher */}
          <div className="border-b border-gray-200 flex-shrink-0">
            <div className="flex">
              <button
                onClick={() => setActiveTab("chat")}
                className={`flex-1 px-4 py-3 text-sm font-medium transition-colors ${
                  activeTab === "chat"
                    ? "text-primary border-b-2 border-primary"
                    : "text-gray-500 hover:text-gray-700"
                }`}
              >
                <div className="flex items-center justify-center gap-2">
                  <MessageSquare className="w-4 h-4" />
                  Chat
                </div>
              </button>
              <button
                onClick={() => setActiveTab("graph")}
                className={`flex-1 px-4 py-3 text-sm font-medium transition-colors ${
                  activeTab === "graph"
                    ? "text-primary border-b-2 border-primary"
                    : "text-gray-500 hover:text-gray-700"
                }`}
              >
                <div className="flex items-center justify-center gap-2">
                  <Network className="w-4 h-4" />
                  Graph View
                </div>
              </button>
            </div>
          </div>

          {/* Tab Content */}
          <div className="flex-1 overflow-auto">
            {activeTab === "chat" ? (
              <div className="p-4">
                {/* AI Summary */}
                <div className="mb-4">
                  <h3 className="text-sm font-semibold text-gray-900 mb-2 flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-primary" />
                    AI Summary
                  </h3>
                  <div className="bg-primary/5 border border-primary/20 rounded-lg p-4">
                    <p className="text-sm text-gray-700">
                      This section covers{" "}
                      <span className="font-medium text-primary">prompt injection</span>{" "}
                      attacks, a critical security concern for LLM-powered applications.
                      Key defensive strategies include input validation and output filtering.
                    </p>
                  </div>
                </div>

                {/* Key Points */}
                <div className="mb-4">
                  <h3 className="text-sm font-semibold text-gray-900 mb-2 flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-primary" />
                    Key Points
                  </h3>
                  <ul className="space-y-2">
                    {[
                      "Attacks override system instructions",
                      "Multiple attack vectors exist",
                      "Input validation is essential",
                      "Related to alignment and safety",
                    ].map((point, i) => (
                      <li key={i} className="flex items-start gap-2 text-sm text-gray-600">
                        <ChevronRight className="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                        {point}
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Ask Follow-up */}
                <div>
                  <h3 className="text-sm font-semibold text-gray-900 mb-2 flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-primary" />
                    Ask Follow-up
                  </h3>
                  <div className="space-y-2">
                    {[
                      "How to prevent prompt injection?",
                      "Real-world examples of attacks",
                      "LLM security best practices",
                    ].map((q, i) => (
                      <button
                        key={i}
                        className="w-full text-left px-3 py-2.5 text-sm bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors text-gray-700 border border-transparent hover:border-gray-200"
                      >
                        {q}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            ) : (
              <div className="p-4">
                {/* Mini Knowledge Graph */}
                <div className="mb-4">
                  <h3 className="text-sm font-semibold text-gray-900 mb-2">
                    Related Concepts
                  </h3>
                  <div className="bg-gray-50 rounded-lg p-4">
                    <div className="relative h-44 flex items-center justify-center">
                      {/* Connection lines */}
                      <svg className="absolute inset-0 w-full h-full" style={{ zIndex: 0 }}>
                        {/* Center to branches */}
                        <line x1="50%" y1="50%" x2="20%" y2="25%" stroke="#E5E7EB" strokeWidth="1.5" strokeDasharray="4 2" />
                        <line x1="50%" y1="50%" x2="80%" y2="25%" stroke="#E5E7EB" strokeWidth="1.5" strokeDasharray="4 2" />
                        <line x1="50%" y1="50%" x2="20%" y2="75%" stroke="#E5E7EB" strokeWidth="1.5" strokeDasharray="4 2" />
                        <line x1="50%" y1="50%" x2="80%" y2="75%" stroke="#E5E7EB" strokeWidth="1.5" strokeDasharray="4 2" />
                        {/* Branch to leaf */}
                        <line x1="20%" y1="25%" x2="10%" y2="15%" stroke="#E5E7EB" strokeWidth="1" strokeDasharray="3 2" />
                        <line x1="80%" y1="25%" x2="90%" y2="15%" stroke="#E5E7EB" strokeWidth="1" strokeDasharray="3 2" />
                      </svg>

                      {/* Center node */}
                      <motion.div
                        initial={{ scale: 0 }}
                        animate={{ scale: 1 }}
                        className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-14 h-14 rounded-full bg-primary flex items-center justify-center shadow-md z-10"
                      >
                        <span className="text-white text-xs font-bold text-center leading-tight">
                          LLM<br />Security
                        </span>
                      </motion.div>

                      {/* Branch nodes */}
                      {[
                        { top: "25%", left: "20%", label: "Adversarial", color: "bg-purple-100 text-purple-700 border-purple-300" },
                        { top: "25%", left: "80%", label: "AI Alignment", color: "bg-purple-100 text-purple-700 border-purple-300" },
                        { top: "75%", left: "20%", label: "Safety", color: "bg-purple-100 text-purple-700 border-purple-300" },
                        { top: "75%", left: "80%", label: "Red Teaming", color: "bg-green-100 text-green-700 border-green-300" },
                      ].map((node, i) => (
                        <motion.div
                          key={i}
                          initial={{ opacity: 0, scale: 0 }}
                          animate={{ opacity: 1, scale: 1 }}
                          transition={{ delay: 0.1 + i * 0.05 }}
                          className={`absolute px-3 py-1.5 rounded-full text-xs font-medium border ${node.color} z-10`}
                          style={{ top: node.top, left: node.left, transform: "translate(-50%, -50%)" }}
                        >
                          {node.label}
                        </motion.div>
                      ))}

                      {/* Leaf nodes */}
                      {[
                        { top: "12%", left: "10%", label: "Red Teaming" },
                        { top: "12%", left: "90%", label: "Output Filtering" },
                      ].map((leaf, i) => (
                        <motion.div
                          key={i}
                          initial={{ opacity: 0, scale: 0 }}
                          animate={{ opacity: 1, scale: 1 }}
                          transition={{ delay: 0.3 + i * 0.05 }}
                          className="absolute px-2 py-1 rounded-full text-[10px] font-medium bg-gray-200 text-gray-600 border border-gray-300 z-10"
                          style={{ top: leaf.top, left: leaf.left, transform: "translate(-50%, -50%)" }}
                        >
                          {leaf.label}
                        </motion.div>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Direct Connections */}
                <div>
                  <h3 className="text-sm font-semibold text-gray-900 mb-2">
                    Connections
                  </h3>
                  <div className="space-y-1.5">
                    {relatedConcepts.map((node) => (
                      <div
                        key={node.id}
                        className="flex items-center justify-between px-3 py-2 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors cursor-pointer"
                      >
                        <div className="flex items-center gap-2">
                          <div
                            className={`w-2 h-2 rounded-full ${
                              node.type === "core"
                                ? "bg-primary"
                                : node.type === "branch"
                                ? "bg-purple-400"
                                : "bg-gray-300"
                            }`}
                          />
                          <span className="text-sm text-gray-700">{node.label}</span>
                        </div>
                        <ChevronRight className="w-4 h-4 text-gray-400" />
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
