import Navigation from "@/components/Navigation";
import Hero from "@/components/Hero";
import FeatureCards from "@/components/FeatureCards";
import EnterpriseTabs from "@/components/EnterpriseTabs";
import TestimonialCarousel from "@/components/TestimonialCarousel";
import CTABanner from "@/components/CTABanner";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <>
      <Navigation />
      <Hero />
      <FeatureCards />
      <EnterpriseTabs />
      <TestimonialCarousel />
      <CTABanner />
      <Footer />
    </>
  );
}
