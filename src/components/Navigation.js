import React from 'react';

const Navigation = () => {
  return (
    <nav className="fixed top-0 w-full bg-white shadow-md z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex-shrink-0 flex items-center">
            {/* Logo */}
            <div className="flex items-center">
              <div className="h-8 w-8 bg-blue-700 rounded mr-2 flex items-center justify-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 text-white"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>
              <span
                className="text-xl font-semibold"
                style={{ fontFamily: 'IBM Plex Serif, serif', color: '#0F52BA' }}
              >
                fact.rip
              </span>
            </div>
          </div>
          <div className="flex items-center space-x-6">
            <a href="#features" className="font-medium px-3 py-2 text-sm">
              Features
            </a>
            <a href="#audiences" className="font-medium px-3 py-2 text-sm">
              Use Cases
            </a>
            <a href="#story" className="font-medium px-3 py-2 text-sm">
              Our Story
            </a>
            <a href="#faq" className="font-medium px-3 py-2 text-sm">
              FAQ
            </a>
            <button className="bg-blue-700 hover:bg-blue-800 text-white font-medium py-2 px-4 rounded-md text-sm">
              Get Started
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
