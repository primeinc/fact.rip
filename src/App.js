import React, { useEffect } from 'react';

// Import components
import Navigation from './components/Navigation';
import Hero from './components/Hero';
import ProblemStatement from './components/ProblemStatement';
import MarketGrowthChart from './components/MarketGrowthChart';
import KeyFeatures from './components/KeyFeatures';
import TruthCascade from './components/TruthCascade';
import AudienceTabs from './components/AudienceTabs';
import BrandStory from './components/BrandStory';
import Values from './components/Values';
import FAQ from './components/FAQ';
import CallToAction from './components/CallToAction';
import Footer from './components/Footer';

const App = () => {
  // Animation on scroll effect
  useEffect(() => {
    const handleScroll = () => {
      const elements = document.querySelectorAll('.fade-in-section');
      elements.forEach(element => {
        const position = element.getBoundingClientRect();
        if (position.top < window.innerHeight) {
          element.classList.add('visible');
        }
      });
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll();

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div className="font-sans antialiased bg-white text-gray-900">
      <Navigation />
      <Hero />
      <ProblemStatement />
      <MarketGrowthChart />
      <KeyFeatures />
      <TruthCascade />
      <AudienceTabs />
      <BrandStory />
      <Values />
      <FAQ />
      <CallToAction />
      <Footer />
    </div>
  );
};

export default App;
