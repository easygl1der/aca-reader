"use client";

import { motion } from "framer-motion";
import { Infinity, Quote, Shield } from "lucide-react";

const features = [
  {
    icon: Infinity,
    title: "Infinite Content",
    description:
      "Curate custom AI workspaces with as many content sources as you want, with zero friction.",
  },
  {
    icon: Quote,
    title: "100% Cited",
    description:
      "All answers are sourced directly from your connected content, not generic AI training data.",
  },
  {
    icon: Shield,
    title: "Private and Secure",
    description:
      "Your data is isolated, protected, and never used to train any model.",
  },
];

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

export default function FeatureCards() {
  return (
    <section id="features" className="py-20 lg:py-32 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          variants={containerVariants}
          className="text-center mb-16"
        >
          <motion.h2
            variants={itemVariants}
            className="font-sans text-3xl lg:text-4xl font-bold text-gray-900"
          >
            Zero friction. Infinite content.
          </motion.h2>
          <motion.p
            variants={itemVariants}
            className="mt-4 text-lg text-gray-600 max-w-2xl mx-auto"
          >
            Implicit enables anyone to create their own knowledge base and LLM.
            Learn, share, and deliver expertise through unique AI Navigators.
          </motion.p>
        </motion.div>

        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          variants={containerVariants}
          className="grid md:grid-cols-3 gap-8"
        >
          {features.map((feature, index) => (
            <motion.div
              key={feature.title}
              variants={itemVariants}
              className="bg-white rounded-2xl p-8 border border-gray-100 card-hover"
            >
              <div className="w-14 h-14 rounded-xl bg-primary/10 flex items-center justify-center mb-6">
                <feature.icon className="w-7 h-7 text-primary" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                {feature.title}
              </h3>
              <p className="text-gray-600 leading-relaxed">
                {feature.description}
              </p>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
