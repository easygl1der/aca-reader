"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Layers,
  FileText,
  MessageSquare,
  Workflow,
  RefreshCw,
  ShieldCheck,
} from "lucide-react";

const tabs = [
  {
    id: "unify",
    label: "Unify Knowledge",
    icon: Layers,
    title: "One Connected Knowledge Layer",
    description:
      "Unify manuals, SOPs, tickets, FAQs, and tribal knowledge into one private, connected Knowledge Layer.",
    color: "#6D28D9",
  },
  {
    id: "complex",
    label: "Complex Documents",
    icon: FileText,
    title: "Understand Complex Documents",
    description:
      "Understand complex documents and PDFs with tables, diagrams, pictures, and boolean logic.",
    color: "#7C3AED",
  },
  {
    id: "source",
    label: "Source-Backed Answers",
    icon: MessageSquare,
    title: "Trust and Verify Every Answer",
    description:
      "Deliver answers backed by sources, so your users can trust and verify every answer. Drive AI adoption to avoid project failure.",
    color: "#8B5CF6",
  },
  {
    id: "integrate",
    label: "AI Siloes Integration",
    icon: Workflow,
    title: "Work Where You Work",
    description:
      "Leverage full-stack APIs to plug into your existing tools and workflows, delivering data to your systems and knowledge to your users.",
    color: "#06B6D4",
  },
  {
    id: "dynamic",
    label: "Dynamic Updates",
    icon: RefreshCw,
    title: "Always Current Knowledge",
    description:
      "Continuously and dynamically update your knowledge bases, taxonomies, and graphs with AI. Leverage Content Analytics to ensure your knowledge base is always current.",
    color: "#6D28D9",
  },
  {
    id: "governance",
    label: "Governance & Compliance",
    icon: ShieldCheck,
    title: "Enforce Consistency",
    description:
      "Enforce consistency, auditability, and compliance across all your knowledge assets.",
    color: "#7C3AED",
  },
];

export default function EnterpriseTabs() {
  const [activeTab, setActiveTab] = useState(0);
  const activeData = tabs[activeTab];
  const ActiveIcon = activeData.icon;

  return (
    <section id="enterprise" className="py-20 lg:py-32">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="font-sans text-3xl lg:text-4xl font-bold text-gray-900">
            For enterprises, Implicit solves 6 key problems
          </h2>
        </div>

        {/* Tab Buttons */}
        <div className="flex flex-wrap justify-center gap-2 lg:gap-4 mb-12">
          {tabs.map((tab, index) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(index)}
              className={`px-4 py-2 rounded-lg font-medium transition-all ${
                activeTab === index
                  ? "bg-primary text-white shadow-lg"
                  : "bg-gray-100 text-gray-600 hover:bg-gray-200"
              }`}
            >
              <span className="hidden lg:inline">{tab.label}</span>
              <span className="lg:hidden">
                <tab.icon className="w-5 h-5" />
              </span>
            </button>
          ))}
        </div>

        {/* Tab Content */}
        <AnimatePresence mode="wait">
          <motion.div
            key={activeTab}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.2 }}
            className="bg-white rounded-2xl border border-gray-200 overflow-hidden"
          >
            <div className="grid lg:grid-cols-2">
              {/* Text Content */}
              <div className="p-8 lg:p-12 flex flex-col justify-center">
                <div
                  className="w-12 h-12 rounded-xl flex items-center justify-center mb-6"
                  style={{ backgroundColor: `${activeData.color}20` }}
                >
                  <ActiveIcon
                    className="w-6 h-6"
                    style={{ color: activeData.color }}
                  />
                </div>
                <h3 className="font-sans text-2xl lg:text-3xl font-bold text-gray-900 mb-4">
                  {activeData.title}
                </h3>
                <p className="text-gray-600 text-lg leading-relaxed">
                  {activeData.description}
                </p>
                <div className="mt-8">
                  <a
                    href="#"
                    className="inline-flex items-center gap-2 text-primary font-medium hover:gap-3 transition-all"
                  >
                    Learn more
                    <svg
                      className="w-4 h-4"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M9 5l7 7-7 7"
                      />
                    </svg>
                  </a>
                </div>
              </div>

              {/* Visual Content - Abstract representation */}
              <div className="bg-gradient-to-br from-gray-50 to-white p-8 lg:p-12 flex items-center justify-center min-h-[300px]">
                <div className="relative w-full max-w-sm">
                  {/* Abstract UI Mockup */}
                  <div className="bg-white rounded-xl shadow-lg border border-gray-100 p-6">
                    <div className="flex items-center gap-3 mb-4">
                      <div
                        className="w-3 h-3 rounded-full"
                        style={{ backgroundColor: activeData.color }}
                      />
                      <span className="text-sm font-medium text-gray-500">
                        {activeData.label}
                      </span>
                    </div>
                    <div className="space-y-3">
                      {[1, 2, 3].map((i) => (
                        <div
                          key={i}
                          className="h-3 rounded-full bg-gray-100"
                          style={{
                            width: `${100 - i * 20}%`,
                            backgroundColor: `${activeData.color}15`,
                          }}
                        />
                      ))}
                    </div>
                    <div
                      className="mt-6 h-24 rounded-lg"
                      style={{
                        background: `linear-gradient(135deg, ${activeData.color}10, ${activeData.color}05)`,
                        border: `1px solid ${activeData.color}20`,
                      }}
                    />
                  </div>

                  {/* Decorative elements */}
                  <div
                    className="absolute -top-4 -right-4 w-20 h-20 rounded-full opacity-20 blur-xl"
                    style={{ backgroundColor: activeData.color }}
                  />
                </div>
              </div>
            </div>
          </motion.div>
        </AnimatePresence>
      </div>
    </section>
  );
}
