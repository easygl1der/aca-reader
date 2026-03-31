"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import AnimatedGraph from "./AnimatedGraph";

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.15,
      delayChildren: 0.2,
    },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: "easeOut" },
  },
};

export default function Hero() {
  return (
    <section className="pt-32 lg:pt-40 pb-20 lg:pb-32 overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
          {/* Left Content */}
          <motion.div
            variants={containerVariants}
            initial="hidden"
            animate="visible"
            className="text-center lg:text-left"
          >
            <motion.h1
              variants={itemVariants}
              className="font-sans text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight"
            >
              Your AI Knowledge and{" "}
              <span className="gradient-text">Learning Engine</span>
            </motion.h1>

            <motion.p
              variants={itemVariants}
              className="mt-6 text-lg lg:text-xl text-gray-600 max-w-xl mx-auto lg:mx-0"
            >
              Experience AI Experts Built From Real Knowledge. These AI experts
              are built from real knowledge sources. Ask questions and get
              answers grounded in real sources, not generic AI training data.
            </motion.p>

            <motion.div
              variants={itemVariants}
              className="mt-8 flex flex-col sm:flex-row gap-4 justify-center lg:justify-start"
            >
              <Link
                href="#demo"
                className="px-8 py-4 bg-primary hover:bg-primary-light text-white font-semibold rounded-lg transition-all btn-glow"
              >
                Try Demo Navigator
              </Link>
              <Link
                href="#"
                className="px-8 py-4 bg-white hover:bg-gray-50 text-gray-900 font-semibold rounded-lg border border-gray-200 transition-all"
              >
                Start Free
              </Link>
            </motion.div>

            <motion.p
              variants={itemVariants}
              className="mt-6 text-sm text-gray-500"
            >
              No account required. Try instantly.
            </motion.p>
          </motion.div>

          {/* Right - Animated Graph Demo */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="relative"
          >
            <div className="relative bg-gradient-to-br from-gray-50 to-white rounded-2xl border border-gray-200 p-6 lg:p-8 shadow-xl">
              {/* Demo Header */}
              <div className="flex items-center gap-2 mb-6">
                <div className="flex gap-1.5">
                  <div className="w-3 h-3 rounded-full bg-red-400" />
                  <div className="w-3 h-3 rounded-full bg-yellow-400" />
                  <div className="w-3 h-3 rounded-full bg-green-400" />
                </div>
                <span className="text-sm text-gray-500 ml-2">
                  implicit.cloud
                </span>
              </div>

              {/* Animated Graph */}
              <AnimatedGraph />

              {/* Demo Text */}
              <div className="mt-6 p-4 bg-white rounded-lg border border-gray-100">
                <p className="text-sm text-gray-600">
                  Knowledge is everywhere, but often scattered.{" "}
                  <span className="text-primary font-medium">
                    Implicit unifies it all.
                  </span>
                </p>
              </div>
            </div>

            {/* Decorative Elements */}
            <div className="absolute -top-4 -right-4 w-24 h-24 bg-primary/10 rounded-full blur-2xl" />
            <div className="absolute -bottom-4 -left-4 w-32 h-32 bg-accent/10 rounded-full blur-2xl" />
          </motion.div>
        </div>
      </div>
    </section>
  );
}
