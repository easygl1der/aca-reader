"use client";

import Link from "next/link";
import {
  FileText,
  BookOpen,
  PenTool,
  Lightbulb,
  Database,
  BookCopy,
  Search,
  Upload,
  Sparkles,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

const features = [
  {
    icon: FileText,
    title: "Chat with PDF",
    description: "Upload any PDF and chat with it to understand complex papers instantly",
    href: "/chat-pdf",
  },
  {
    icon: BookOpen,
    title: "Literature Review",
    description: "Search and synthesize findings across thousands of academic papers",
    href: "/literature-review",
  },
  {
    icon: PenTool,
    title: "AI Writer",
    description: "Generate well-structured academic content with proper citations",
    href: "/ai-writer",
  },
  {
    icon: Lightbulb,
    title: "Find Topics",
    description: "Discover research gaps and emerging trends in your field",
    href: "/concepts",
  },
  {
    icon: Database,
    title: "Extract Data",
    description: "Automatically extract tables, figures, and data from papers",
    href: "/extract-data",
  },
  {
    icon: BookCopy,
    title: "Citation Generator",
    description: "Generate accurate citations in APA, MLA, Chicago, and more formats",
    href: "/citation-generator",
  },
];

const quickActions = [
  { label: "Upload PDF", icon: Upload, href: "/chat-pdf" },
  { label: "Search Papers", icon: Search, href: "/search" },
  { label: "Start Writing", icon: PenTool, href: "/ai-writer" },
];

export default function HomePage() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section */}
      <section className="flex-1 flex flex-col items-center justify-center px-4 py-16">
        <div className="w-full max-w-3xl mx-auto text-center space-y-8">
          {/* Heading */}
          <div className="space-y-4">
            <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-white">
              Research Faster with{" "}
              <span className="bg-gradient-to-r from-[#7c3aed] to-[#a855f7] bg-clip-text text-transparent">
                AI
              </span>
            </h1>
            <p className="text-xl text-[#a1a1a1] max-w-2xl mx-auto">
              Your AI-powered academic research assistant. Understand papers, find
              insights, and write better research.
            </p>
          </div>

          {/* Search Bar */}
          <div className="relative w-full max-w-2xl mx-auto">
            <div className="relative flex items-center">
              <Search className="absolute left-4 h-5 w-5 text-[#525252]" />
              <Input
                type="text"
                placeholder="Search papers, topics, or paste a PDF link..."
                className="w-full h-14 pl-12 pr-32 text-base bg-[#171717] border-[#333333] rounded-xl focus:border-[#7c3aed] focus:ring-2 focus:ring-[#7c3aed]/20"
              />
              <Button className="absolute right-2 h-10 px-6 bg-[#7c3aed] hover:bg-[#6d28d9] rounded-lg">
                Search
              </Button>
            </div>
          </div>

          {/* Quick Action Buttons */}
          <div className="flex flex-wrap items-center justify-center gap-3">
            {quickActions.map((action) => {
              const Icon = action.icon;
              return (
                <Link key={action.href} href={action.href}>
                  <Button
                    variant="outline"
                    className="border-[#333333] bg-[#171717] hover:bg-[#262626] text-[#a1a1a1] hover:text-white gap-2"
                  >
                    <Icon className="h-4 w-4" />
                    {action.label}
                  </Button>
                </Link>
              );
            })}
          </div>
        </div>
      </section>

      {/* Feature Cards Section */}
      <section className="px-4 py-16 bg-[#0a0a0a]">
        <div className="max-w-6xl mx-auto">
          {/* Section Header */}
          <div className="text-center mb-12">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#7c3aed]/10 text-[#7c3aed] text-sm font-medium mb-4">
              <Sparkles className="h-4 w-4" />
              Features
            </div>
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
              Everything you need for academic research
            </h2>
            <p className="text-[#a1a1a1] max-w-2xl mx-auto">
              Powerful AI tools designed to help you read, understand, and write
              academic research faster.
            </p>
          </div>

          {/* Cards Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {features.map((feature) => {
              const Icon = feature.icon;
              return (
                <Link key={feature.href} href={feature.href}>
                  <Card className="h-full bg-[#171717] border-[#333333] hover:border-[#7c3aed] transition-colors cursor-pointer group">
                    <CardHeader>
                      <div className="h-12 w-12 rounded-lg bg-[#7c3aed]/10 flex items-center justify-center mb-4 group-hover:bg-[#7c3aed]/20 transition-colors">
                        <Icon className="h-6 w-6 text-[#7c3aed]" />
                      </div>
                      <CardTitle className="text-white group-hover:text-[#7c3aed] transition-colors">
                        {feature.title}
                      </CardTitle>
                      <CardDescription className="text-[#a1a1a1]">
                        {feature.description}
                      </CardDescription>
                    </CardHeader>
                    <CardContent>
                      <span className="inline-flex items-center text-sm text-[#7c3aed] font-medium">
                        Get started
                        <svg
                          className="ml-1 h-4 w-4 group-hover:translate-x-1 transition-transform"
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
                      </span>
                    </CardContent>
                  </Card>
                </Link>
              );
            })}
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="px-4 py-12 border-t border-[#333333]">
        <div className="max-w-6xl mx-auto">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div className="space-y-2">
              <div className="text-3xl font-bold text-white">200M+</div>
              <div className="text-sm text-[#a1a1a1]">Academic Papers</div>
            </div>
            <div className="space-y-2">
              <div className="text-3xl font-bold text-white">50M+</div>
              <div className="text-sm text-[#a1a1a1]">Researchers</div>
            </div>
            <div className="space-y-2">
              <div className="text-3xl font-bold text-white">190+</div>
              <div className="text-sm text-[#a1a1a1]">Countries</div>
            </div>
            <div className="space-y-2">
              <div className="text-3xl font-bold text-white">24/7</div>
              <div className="text-sm text-[#a1a1a1]">AI Assistance</div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer CTA */}
      <section className="px-4 py-16 bg-gradient-to-b from-[#0a0a0a] to-[#171717]">
        <div className="max-w-3xl mx-auto text-center space-y-6">
          <h2 className="text-2xl md:text-3xl font-bold text-white">
            Ready to accelerate your research?
          </h2>
          <p className="text-[#a1a1a1]">
            Join millions of researchers using AI to understand papers faster and
            write better research.
          </p>
          <div className="flex flex-wrap items-center justify-center gap-4">
            <Link href="/chat-pdf">
              <Button className="bg-[#7c3aed] hover:bg-[#6d28d9] h-12 px-8">
                Upload Your First PDF
              </Button>
            </Link>
            <Link href="/search">
              <Button
                variant="outline"
                className="border-[#333333] hover:bg-[#262626] h-12 px-8"
              >
                Explore Papers
              </Button>
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
