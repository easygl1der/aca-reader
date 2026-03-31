"use client";

import { motion } from "framer-motion";
import Link from "next/link";

export default function CTABanner() {
  return (
    <section className="py-20 lg:py-32">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
          className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-gray-900 via-gray-900 to-primary/20 px-8 py-16 lg:px-16 lg:py-20 text-center"
        >
          {/* Background decoration */}
          <div className="absolute inset-0 overflow-hidden">
            <div className="absolute -top-1/2 -right-1/4 w-96 h-96 bg-primary/20 rounded-full blur-3xl" />
            <div className="absolute -bottom-1/2 -left-1/4 w-96 h-96 bg-accent/10 rounded-full blur-3xl" />
          </div>

          <div className="relative z-10">
            <h2 className="font-sans text-3xl lg:text-5xl font-bold text-white mb-6">
              Ready to transform your knowledge?
            </h2>
            <p className="text-lg lg:text-xl text-gray-300 max-w-2xl mx-auto mb-10">
              Join thousands of people using Implicit to teach and train better,
              learn faster, and deliver more.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                href="#"
                className="px-8 py-4 bg-white hover:bg-gray-100 text-gray-900 font-semibold rounded-lg transition-all"
              >
                Start Free Trial
              </Link>
              <Link
                href="#"
                className="px-8 py-4 bg-primary/20 hover:bg-primary/30 text-white font-semibold rounded-lg border border-white/20 transition-all"
              >
                Schedule Demo
              </Link>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
