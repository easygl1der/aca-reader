"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import Link from "next/link";
import {
  Send,
  Bot,
  User,
  ChevronLeft,
  ChevronRight,
  Link2,
  Filter,
  MessageSquare,
  Network,
  LayoutGrid,
  Plus,
  Minus,
  ZoomIn,
  ZoomOut,
  ChevronDown,
  PanelLeftClose,
  PanelLeft,
} from "lucide-react";

interface Node {
  id: string;
  label: string;
  type: "topic" | "subtopic" | "entity";
  connections: number;
}

const nodes: Node[] = [
  { id: "1", label: "AGI", type: "topic", connections: 12 },
  { id: "2", label: "Alignment", type: "subtopic", connections: 8 },
  { id: "3", label: "Safety", type: "subtopic", connections: 6 },
  { id: "4", label: "Governance", type: "subtopic", connections: 5 },
  { id: "5", label: "Policy", type: "subtopic", connections: 4 },
  { id: "6", label: "Superalignment", type: "entity", connections: 3 },
  { id: "7", label: "RLHF", type: "entity", connections: 4 },
  { id: "8", label: "Interpretability", type: "entity", connections: 2 },
  { id: "9", label: "Eval", type: "entity", connections: 3 },
  { id: "10", label: "Red Team", type: "entity", connections: 2 },
  { id: "11", label: "Blue Team", type: "entity", connections: 2 },
  { id: "12", label: "EU Regulation", type: "entity", connections: 1 },
  { id: "13", label: "Ethics", type: "entity", connections: 3 },
  { id: "14", label: "Bias", type: "entity", connections: 2 },
];

const suggestedQuestions = [
  "What are the key components of AI alignment?",
  "How does RLHF contribute to model safety?",
  "What regulations apply to AI systems in the EU?",
];

const chatMessages = [
  {
    type: "ai",
    text: "Hello! I'm your AI Navigator. I can help you explore the knowledge graph, answer questions about AGI, Alignment, Safety, and more. What would you like to know?",
  },
];

const getNodeColor = (type: Node["type"]) => {
  switch (type) {
    case "topic":
      return "bg-green-500";
    case "subtopic":
      return "bg-purple-400";
    case "entity":
      return "bg-gray-300";
  }
};

const getNodeBorder = (type: Node["type"]) => {
  switch (type) {
    case "topic":
      return "border-green-500";
    case "subtopic":
      return "border-purple-400";
    case "entity":
      return "border-gray-300";
  }
};

export default function NavigatorPage() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [isChatOpen, setIsChatOpen] = useState(true);
  const [viewMode, setViewMode] = useState<"graph" | "table">("graph");
  const [messages, setMessages] = useState(chatMessages);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [selectedNode, setSelectedNode] = useState<string | null>(null);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = input;
    const conversationMessages = [
      ...messages.map((m) => ({ role: m.type === "user" ? "user" : "assistant", content: m.text })),
      { role: "user", content: userMessage },
    ];

    setMessages((prev) => [...prev, { type: "user", text: userMessage }]);
    setInput("");
    setIsTyping(true);

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: conversationMessages }),
      });

      const data = await response.json();
      const reply = data.reply || "Sorry, I couldn't get a response.";

      setMessages((prev) => [...prev, { type: "ai", text: reply }]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { type: "ai", text: "Error: Failed to connect to AI service." },
      ]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className="h-screen flex flex-col bg-gray-100">
      {/* Header Bar */}
      <header className="h-14 bg-white border-b border-gray-200 px-4 flex items-center justify-between flex-shrink-0">
        <div className="flex items-center gap-4">
          <button
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
            className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            {isSidebarOpen ? (
              <PanelLeftClose className="w-5 h-5 text-gray-600" />
            ) : (
              <PanelLeft className="w-5 h-5 text-gray-600" />
            )}
          </button>

          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-primary-light flex items-center justify-center">
              <Bot className="w-4 h-4 text-white" />
            </div>
            <div>
              <h1 className="font-semibold text-gray-900 text-sm">AI Navigator</h1>
              <p className="text-xs text-gray-500">14 concepts · 13 connections</p>
            </div>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <Link
            href="/navigator/document"
            className="px-3 py-1.5 text-sm bg-primary hover:bg-primary-light text-white font-medium rounded-lg transition-colors flex items-center gap-2"
          >
            <Link2 className="w-4 h-4" />
            Connect
          </Link>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex-1 flex overflow-hidden">
        {/* Left Sidebar - Nodes */}
        <AnimatePresence>
          {isSidebarOpen && (
            <motion.aside
              initial={{ width: 0, opacity: 0 }}
              animate={{ width: 280, opacity: 1 }}
              exit={{ width: 0, opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="bg-white border-r border-gray-200 flex flex-col h-full"
            >
              {/* Sidebar Header */}
              <div className="px-4 py-3 border-b border-gray-200 flex items-center justify-between flex-shrink-0">
                <h2 className="font-semibold text-gray-900">Nodes</h2>
                <span className="text-xs text-gray-500">{nodes.length}</span>
              </div>

              {/* Filter Section */}
              <div className="px-4 py-2 border-b border-gray-100 flex-shrink-0">
                <div className="flex items-center gap-2 text-sm text-gray-600 mb-2">
                  <Filter className="w-3.5 h-3.5" />
                  <span>Filter</span>
                </div>
                <div className="flex flex-wrap gap-1.5">
                  {["Topic", "Subtopic", "Entity"].map((type) => (
                    <span
                      key={type}
                      className={`px-2 py-0.5 text-xs rounded-full cursor-pointer ${
                        type === "Topic"
                          ? "bg-green-100 text-green-700"
                          : type === "Subtopic"
                          ? "bg-purple-100 text-purple-700"
                          : "bg-gray-100 text-gray-600"
                      }`}
                    >
                      {type}
                    </span>
                  ))}
                </div>
              </div>

              {/* Nodes List */}
              <div className="flex-1 overflow-auto">
                {["Topic", "Subtopic", "Entity"].map((category) => (
                  <div key={category} className="border-b border-gray-100 last:border-0">
                    <button className="w-full px-4 py-2 flex items-center justify-between text-left hover:bg-gray-50">
                      <span className="text-xs font-medium text-gray-500 uppercase">
                        {category}
                      </span>
                      <ChevronDown className="w-3.5 h-3.5 text-gray-400" />
                    </button>
                    <div className="px-2 pb-2">
                      {nodes
                        .filter((n) => n.type === category.toLowerCase() as Node["type"])
                        .map((node) => (
                          <button
                            key={node.id}
                            onClick={() => setSelectedNode(node.id === selectedNode ? null : node.id)}
                            className={`w-full px-3 py-2 rounded-lg text-left text-sm mb-1 transition-all flex items-center justify-between group ${
                              selectedNode === node.id
                                ? "bg-primary/10 text-primary"
                                : "hover:bg-gray-50 text-gray-700"
                            }`}
                          >
                            <div className="flex items-center gap-2">
                              <div className={`w-2 h-2 rounded-full ${getNodeColor(node.type)}`} />
                              <span>{node.label}</span>
                            </div>
                            <span className="text-xs text-gray-400 group-hover:text-gray-600">
                              {node.connections}
                            </span>
                          </button>
                        ))}
                    </div>
                  </div>
                ))}
              </div>
            </motion.aside>
          )}
        </AnimatePresence>

        {/* Main Graph/Table Area */}
        <main className="flex-1 flex flex-col overflow-hidden">
          {/* View Mode Tabs */}
          <div className="bg-white border-b border-gray-200 px-4 py-2 flex items-center justify-between">
            <div className="flex gap-1">
              {[
                { id: "graph", label: "Graph", icon: Network },
                { id: "table", label: "Table", icon: LayoutGrid },
              ].map((tab) => (
                <button
                  key={tab.id}
                  onClick={() => setViewMode(tab.id as "graph" | "table")}
                  className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors flex items-center gap-2 ${
                    viewMode === tab.id
                      ? "bg-gray-900 text-white"
                      : "text-gray-600 hover:bg-gray-100"
                  }`}
                >
                  <tab.icon className="w-4 h-4" />
                  {tab.label}
                </button>
              ))}
            </div>

            <div className="flex items-center gap-2">
              <button className="p-1.5 hover:bg-gray-100 rounded transition-colors">
                <ZoomOut className="w-4 h-4 text-gray-500" />
              </button>
              <span className="text-xs text-gray-600 w-12 text-center">100%</span>
              <button className="p-1.5 hover:bg-gray-100 rounded transition-colors">
                <ZoomIn className="w-4 h-4 text-gray-500" />
              </button>
              <button className="p-1.5 hover:bg-gray-100 rounded transition-colors ml-2">
                <Plus className="w-4 h-4 text-gray-500" />
              </button>
              <button className="p-1.5 hover:bg-gray-100 rounded transition-colors">
                <Minus className="w-4 h-4 text-gray-500" />
              </button>
            </div>
          </div>

          {/* Content */}
          <div className="flex-1 overflow-hidden relative">
            {viewMode === "graph" ? (
              /* Graph View */
              <div className="h-full flex items-center justify-center bg-gray-50">
                {/* Graph visualization placeholder */}
                <div className="relative w-[600px] h-[400px]">
                  {/* Connection lines */}
                  <svg className="absolute inset-0 w-full h-full" style={{ zIndex: 0 }}>
                    {nodes.slice(1).map((node, i) => {
                      const startX = 300;
                      const startY = 200;
                      const angle = ((i + 1) * 360) / nodes.length;
                      const rad = (angle * Math.PI) / 180;
                      const endX = startX + Math.cos(rad) * 150;
                      const endY = startY + Math.sin(rad) * 120;
                      return (
                        <line
                          key={node.id}
                          x1={startX}
                          y1={startY}
                          x2={endX}
                          y2={endY}
                          stroke="#E5E7EB"
                          strokeWidth="1.5"
                          strokeDasharray="4 2"
                        />
                      );
                    })}
                  </svg>

                  {/* Center node - AGI */}
                  <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-16 h-16 rounded-full bg-green-500 border-4 border-green-600 flex items-center justify-center cursor-pointer hover:scale-105 transition-transform"
                    style={{ zIndex: 10 }}
                  >
                    <span className="text-white font-bold text-sm">AGI</span>
                  </motion.div>

                  {/* Surrounding nodes */}
                  {nodes.slice(1).map((node, i) => {
                    const angle = ((i + 1) * 360) / nodes.length;
                    const rad = (angle * Math.PI) / 180;
                    const x = 300 + Math.cos(rad) * 150 - 20;
                    const y = 200 + Math.sin(rad) * 120 - 20;

                    return (
                      <motion.div
                        key={node.id}
                        initial={{ opacity: 0, scale: 0 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: i * 0.05 }}
                        className={`absolute w-10 h-10 rounded-full ${getNodeColor(node.type)} border-2 ${getNodeBorder(node.type)} flex items-center justify-center cursor-pointer hover:scale-110 transition-transform`}
                        style={{ left: x, top: y, zIndex: 5 }}
                      >
                        <span className="text-white text-[8px] font-medium">
                          {node.label.slice(0, 4)}
                        </span>
                      </motion.div>
                    );
                  })}
                </div>

                {/* Graph label */}
                <div className="absolute bottom-4 left-4 px-3 py-1.5 bg-white/90 backdrop-blur rounded-lg border border-gray-200 text-xs text-gray-500">
                  Gen AI 2024 · Knowledge Graph
                </div>
              </div>
            ) : (
              /* Table View */
              <div className="h-full overflow-auto bg-white">
                <table className="w-full">
                  <thead className="bg-gray-50 sticky top-0">
                    <tr>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Name</th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Type</th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Connections</th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-100">
                    {nodes.map((node) => (
                      <tr key={node.id} className="hover:bg-gray-50">
                        <td className="px-4 py-3">
                          <div className="flex items-center gap-2">
                            <div className={`w-2.5 h-2.5 rounded-full ${getNodeColor(node.type)}`} />
                            <span className="text-sm font-medium text-gray-900">{node.label}</span>
                          </div>
                        </td>
                        <td className="px-4 py-3">
                          <span className={`px-2 py-0.5 text-xs rounded-full capitalize ${
                            node.type === "topic"
                              ? "bg-green-100 text-green-700"
                              : node.type === "subtopic"
                              ? "bg-purple-100 text-purple-700"
                              : "bg-gray-100 text-gray-600"
                          }`}>
                            {node.type}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-sm text-gray-600">{node.connections}</td>
                        <td className="px-4 py-3">
                          <button className="text-primary hover:text-primary-light text-sm">
                            View →
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </main>

        {/* Right Chat Panel */}
        <AnimatePresence>
          {isChatOpen && (
            <motion.aside
              initial={{ width: 0, opacity: 0 }}
              animate={{ width: 320, opacity: 1 }}
              exit={{ width: 0, opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="bg-white border-l border-gray-200 flex flex-col overflow-hidden"
            >
              {/* Chat Header */}
              <div className="px-4 py-3 border-b border-gray-200 flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <MessageSquare className="w-4 h-4 text-gray-500" />
                  <h2 className="font-semibold text-gray-900">Chat</h2>
                </div>
                <button
                  onClick={() => setIsChatOpen(false)}
                  className="p-1 hover:bg-gray-100 rounded transition-colors"
                >
                  <ChevronRight className="w-4 h-4 text-gray-400" />
                </button>
              </div>

              {/* Messages */}
              <div className="flex-1 overflow-auto p-4 space-y-4">
                {messages.map((msg, index) => (
                  <div
                    key={index}
                    className={`flex gap-2 ${msg.type === "user" ? "flex-row-reverse" : ""}`}
                  >
                    {msg.type === "ai" && (
                      <div className="w-7 h-7 rounded-full bg-primary flex items-center justify-center flex-shrink-0">
                        <Bot className="w-3.5 h-3.5 text-white" />
                      </div>
                    )}
                    <div
                      className={`max-w-[85%] px-3 py-2 text-sm ${
                        msg.type === "user" ? "chat-bubble-user" : "chat-bubble-ai"
                      }`}
                    >
                      {msg.text}
                    </div>
                    {msg.type === "user" && (
                      <div className="w-7 h-7 rounded-full bg-gray-200 flex items-center justify-center flex-shrink-0">
                        <User className="w-3.5 h-3.5 text-gray-600" />
                      </div>
                    )}
                  </div>
                ))}

                {isTyping && (
                  <div className="flex gap-2">
                    <div className="w-7 h-7 rounded-full bg-primary flex items-center justify-center">
                      <Bot className="w-3.5 h-3.5 text-white" />
                    </div>
                    <div className="chat-bubble-ai px-3 py-2">
                      <div className="flex gap-1">
                        <span className="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" />
                        <span className="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: "0.1s" }} />
                        <span className="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: "0.2s" }} />
                      </div>
                    </div>
                  </div>
                )}
              </div>

              {/* Suggested Questions */}
              <div className="border-t border-gray-100 p-3 bg-gray-50">
                <p className="text-xs text-gray-500 mb-2">Try asking...</p>
                <div className="space-y-1.5">
                  {suggestedQuestions.map((q, i) => (
                    <button
                      key={i}
                      onClick={() => setInput(q)}
                      className="w-full text-left text-xs px-3 py-2 bg-white border border-gray-200 rounded-lg hover:border-primary hover:text-primary transition-colors"
                    >
                      {q}
                    </button>
                  ))}
                </div>
              </div>

              {/* Input */}
              <div className="p-3 border-t border-gray-200">
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === "Enter" && handleSend()}
                    placeholder="Ask a question..."
                    className="flex-1 px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary"
                  />
                  <button
                    onClick={handleSend}
                    disabled={!input.trim()}
                    className="p-2 bg-primary hover:bg-primary-light disabled:bg-gray-300 disabled:cursor-not-allowed text-white rounded-lg transition-colors"
                  >
                    <Send className="w-4 h-4" />
                  </button>
                </div>
              </div>
            </motion.aside>
          )}
        </AnimatePresence>

        {/* Chat Toggle Button when chat is closed */}
        {!isChatOpen && (
          <button
            onClick={() => setIsChatOpen(true)}
            className="absolute right-4 bottom-4 p-3 bg-primary hover:bg-primary-light text-white rounded-full shadow-lg transition-colors"
          >
            <MessageSquare className="w-5 h-5" />
          </button>
        )}
      </div>
    </div>
  );
}
