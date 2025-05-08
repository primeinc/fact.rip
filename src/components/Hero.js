import React from 'react';

const Hero = () => {
  return (
    <header className="pt-24 pb-16 px-4 sm:px-6 lg:px-8 bg-gradient-to-r from-blue-50 to-blue-100">
      <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <div className="fade-in-section">
          <h1
            className="text-4xl sm:text-5xl font-semibold leading-tight"
            style={{ fontFamily: 'IBM Plex Serif, serif', color: '#0F52BA' }}
          >
            The truth engine for documentation
          </h1>
          <p className="mt-6 text-xl text-gray-700 leading-relaxed">
            The first documentation platform that ensures trust through AI-powered validation of
            citations, logic, and content governance while automatically archiving original sources.
          </p>
          <div className="mt-8 flex space-x-4">
            <button className="bg-blue-700 hover:bg-blue-800 text-white font-medium py-3 px-6 rounded-md">
              Request Demo
            </button>
            <button className="border border-blue-700 text-blue-700 hover:bg-blue-50 font-medium py-3 px-6 rounded-md">
              Learn More
            </button>
          </div>
          <div className="mt-6 flex items-center">
            <span className="inline-flex rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-800 mr-3">
              <span className="mr-1">✓</span> Validated Technology
            </span>
            <span className="text-sm text-gray-600">
              $1.6-2.3 trillion projected DaaS market by 2032
            </span>
          </div>
        </div>
        <div className="fade-in-section">
          <div className="relative">
            <div className="absolute inset-0 bg-gradient-to-br from-blue-200 via-transparent to-green-100 opacity-50 rounded-xl -m-1"></div>
            <div className="bg-white rounded-lg shadow-xl overflow-hidden relative z-10">
              <div className="px-6 py-4 bg-blue-700 text-white flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 mr-2"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm3 1h6v4H7V5zm8 8v2h1v1H4v-1h1v-2a3 3 0 013-3h4a3 3 0 013 3zM9 13a1 1 0 102 0 1 1 0 00-2 0z"
                    clipRule="evenodd"
                  />
                </svg>
                <div>Documentation Validation Report</div>
              </div>
              <div className="p-6">
                <div className="flex justify-between items-center mb-4">
                  <div className="font-medium">Strategic Planning Doc</div>
                  <div className="flex items-center bg-green-100 text-green-800 text-xs px-2 py-1 rounded">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      className="h-4 w-4 mr-1"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        fillRule="evenodd"
                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                        clipRule="evenodd"
                      />
                    </svg>
                    Fully Verified
                  </div>
                </div>

                <div className="space-y-3">
                  <div className="flex items-center">
                    <div className="h-6 w-6 bg-green-100 text-green-800 rounded-full flex items-center justify-center mr-3">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-4 w-4"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                      >
                        <path
                          fillRule="evenodd"
                          d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                          clipRule="evenodd"
                        />
                      </svg>
                    </div>
                    <div>
                      <div className="text-sm text-gray-700">18 Citations Validated</div>
                    </div>
                  </div>

                  <div className="flex items-center">
                    <div className="h-6 w-6 bg-green-100 text-green-800 rounded-full flex items-center justify-center mr-3">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-4 w-4"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                      >
                        <path
                          fillRule="evenodd"
                          d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                          clipRule="evenodd"
                        />
                      </svg>
                    </div>
                    <div>
                      <div className="text-sm text-gray-700">Logic Consistency Verified</div>
                    </div>
                  </div>

                  <div className="flex items-center">
                    <div className="h-6 w-6 bg-green-100 text-green-800 rounded-full flex items-center justify-center mr-3">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-4 w-4"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                      >
                        <path
                          fillRule="evenodd"
                          d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                          clipRule="evenodd"
                        />
                      </svg>
                    </div>
                    <div>
                      <div className="text-sm text-gray-700">18 Sources Archived</div>
                    </div>
                  </div>

                  <div className="flex items-center">
                    <div className="h-6 w-6 bg-amber-100 text-amber-800 rounded-full flex items-center justify-center mr-3">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-4 w-4"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                      >
                        <path
                          fillRule="evenodd"
                          d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z"
                          clipRule="evenodd"
                        />
                      </svg>
                    </div>
                    <div>
                      <div className="text-sm text-gray-700">1 Regulatory Update Detected</div>
                    </div>
                  </div>
                </div>

                <div className="border-t border-gray-200 mt-4 pt-4">
                  <div className="text-sm text-gray-600 mb-2">Last validated: 2 hours ago</div>
                  <div className="text-sm font-medium text-blue-700 cursor-pointer hover:text-blue-800">
                    View full validation report →
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Hero;
