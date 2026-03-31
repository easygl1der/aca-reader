import Hero from "@/components/Hero";
import FeatureCards from "@/components/FeatureCards";
import EnterpriseTabs from "@/components/EnterpriseTabs";
import TestimonialCarousel from "@/components/TestimonialCarousel";
import CTABanner from "@/components/CTABanner";

export default function Home() {
  return (
    <>
      <Hero />
      <FeatureCards />
      <EnterpriseTabs />
      <TestimonialCarousel />
      <CTABanner />
    </>
  );
}
