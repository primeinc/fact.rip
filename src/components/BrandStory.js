import React from 'react';

const BrandStory = () => {
  return (
    <section
      id="story"
      className="py-16 px-4 sm:px-6 lg:px-8 bg-gradient-to-r from-blue-50 to-blue-100"
    >
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12 fade-in-section">
          <h2
            className="text-3xl font-semibold text-gray-900"
            style={{ fontFamily: 'IBM Plex Serif, serif' }}
          >
            Our Story
          </h2>
          <p className="mt-4 text-xl text-gray-600 max-w-3xl mx-auto">
            Born from a fundamental insight: business decisions are only as good as the
            documentation they're based on
          </p>
        </div>

        <div className="bg-white rounded-lg shadow-lg overflow-hidden fade-in-section">
          <div className="p-8">
            <div className="flex flex-col md:flex-row items-center md:items-start gap-8">
              <div className="w-full md:w-1/3 flex-shrink-0">
                <div className="relative">
                  <div className="absolute inset-0 bg-gradient-to-br from-blue-200 via-transparent to-green-100 opacity-50 rounded-lg -m-1"></div>
                  <div className="bg-blue-700 rounded-lg p-1 relative z-10">
                    <div className="bg-white rounded-lg overflow-hidden">
                      <div className="aspect-w-1 aspect-h-1 bg-gray-200 flex items-center justify-center">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          className="h-32 w-32 text-blue-700"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                        >
                          <path
                            fillRule="evenodd"
                            d="M10 2a1 1 0 00-1 1v1.323l3.954 1.582 1.599-.8a1 1 0 01.894 1.79l-1.233.616 1.738 5.42a1 1 0 01-.285 1.05A3.989 3.989 0 0115 15a3.989 3.989 0 01-2.667-1.019 1 1 0 01-.285-1.05l1.715-5.349L11 6.477V16h2a1 1 0 110 2H7a1 1 0 110-2h2V6.477L6.237 7.582l1.715 5.349a1 1 0 01-.285 1.05A3.989 3.989 0 015 15a3.989 3.989 0 01-2.667-1.019 1 1 0 01-.285-1.05l1.738-5.42-1.233-.617a1 1 0 01.894-1.788l1.599.799L9 4.323V3a1 1 0 011-1z"
                            clipRule="evenodd"
                          />
                        </svg>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div className="w-full md:w-2/3">
                <p className="text-gray-700 mb-6">
                  Our founder experienced the critical need for documentation validation firsthand
                  while working at a major financial institution. A{' '}
                  <strong>
                    single unvalidated citation in a compliance document led to a $1.2 million
                    regulatory fine
                  </strong>
                  . The documentation platform had failed to verify that the cited regulation had
                  been updated six months earlier.
                </p>

                <p className="text-gray-700 mb-6">
                  This experience revealed a fundamental gap in the documentation landscape: no
                  platform was making validation, not just creation, the core of documentation
                  governance.
                </p>

                <p className="text-gray-700 mb-6">
                  fact.rip was born from this insight — creating a documentation system that could
                  automatically validate information integrity while preserving the original
                  sources. By combining citation validation, logic verification, and source
                  archiving in a single platform, we've created a new standard for documentation
                  reliability.
                </p>

                <h3
                  className="text-xl font-medium text-gray-900 mb-3"
                  style={{ fontFamily: 'IBM Plex Serif, serif' }}
                >
                  Our Purpose
                </h3>

                <p className="text-gray-700">
                  fact.rip exists to create a more trustworthy information ecosystem where
                  documentation can be relied upon without question. We believe that by validating
                  citations, verifying logic, and preserving original sources, we can dramatically
                  reduce the costs and risks of misinformation while elevating the standard for
                  business communication.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default BrandStory;
