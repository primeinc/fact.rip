import React from 'react';

const TruthCascade = () => {
  return (
    <section className="py-16 px-4 sm:px-6 lg:px-8 bg-gradient-to-r from-blue-50 to-blue-100">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12 fade-in-section">
          <h2
            className="text-3xl font-semibold text-gray-900"
            style={{ fontFamily: 'IBM Plex Serif, serif' }}
          >
            The Truth Cascade
          </h2>
          <p className="mt-4 text-xl text-gray-600 max-w-3xl mx-auto">
            Validated information creates exponential downstream value while misinformation creates
            exponential costs
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center fade-in-section">
          <div className="bg-white p-6 rounded-lg shadow-lg">
            <h3 className="text-lg font-medium text-green-700 mb-3">Validated Information Path</h3>
            <div className="space-y-4">
              <div className="flex items-start">
                <div className="h-8 w-8 bg-green-100 rounded-full flex items-center justify-center mr-3 mt-1 flex-shrink-0">
                  <span className="font-medium text-green-800">1</span>
                </div>
                <div>
                  <h4 className="font-medium text-gray-900">Initial Documentation Validation</h4>
                  <p className="text-gray-600 text-sm">
                    All citations verified, logic checked, sources archived
                  </p>
                </div>
              </div>

              <div className="pl-11">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 text-green-600 mx-auto"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>

              <div className="flex items-start">
                <div className="h-8 w-8 bg-green-100 rounded-full flex items-center justify-center mr-3 mt-1 flex-shrink-0">
                  <span className="font-medium text-green-800">2</span>
                </div>
                <div>
                  <h4 className="font-medium text-gray-900">Confident Decision Making</h4>
                  <p className="text-gray-600 text-sm">
                    Leaders trust information and make sound decisions
                  </p>
                </div>
              </div>

              <div className="pl-11">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 text-green-600 mx-auto"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>

              <div className="flex items-start">
                <div className="h-8 w-8 bg-green-100 rounded-full flex items-center justify-center mr-3 mt-1 flex-shrink-0">
                  <span className="font-medium text-green-800">3</span>
                </div>
                <div>
                  <h4 className="font-medium text-gray-900">Reduced Risk Exposure</h4>
                  <p className="text-gray-600 text-sm">
                    Compliance maintained, risks identified early
                  </p>
                </div>
              </div>

              <div className="pl-11">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 text-green-600 mx-auto"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>

              <div className="flex items-start">
                <div className="h-8 w-8 bg-green-100 rounded-full flex items-center justify-center mr-3 mt-1 flex-shrink-0">
                  <span className="font-medium text-green-800">✓</span>
                </div>
                <div>
                  <h4 className="font-medium text-gray-900">Positive Business Outcomes</h4>
                  <p className="text-gray-600 text-sm">
                    Increased efficiency, reduced costs, better decisions
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-white p-6 rounded-lg shadow-lg">
            <h3 className="text-lg font-medium text-red-700 mb-3">Misinformation Path</h3>
            <div className="space-y-4">
              <div className="flex items-start">
                <div className="h-8 w-8 bg-red-100 rounded-full flex items-center justify-center mr-3 mt-1 flex-shrink-0">
                  <span className="font-medium text-red-800">1</span>
                </div>
                <div>
                  <h4 className="font-medium text-gray-900">Unvalidated Documentation</h4>
                  <p className="text-gray-600 text-sm">
                    Invalid citations, logical errors, missing sources
                  </p>
                </div>
              </div>

              <div className="pl-11">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 text-red-600 mx-auto"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>

              <div className="flex items-start">
                <div className="h-8 w-8 bg-red-100 rounded-full flex items-center justify-center mr-3 mt-1 flex-shrink-0">
                  <span className="font-medium text-red-800">2</span>
                </div>
                <div>
                  <h4 className="font-medium text-gray-900">Flawed Decision Making</h4>
                  <p className="text-gray-600 text-sm">
                    Decisions based on incorrect or outdated information
                  </p>
                </div>
              </div>

              <div className="pl-11">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 text-red-600 mx-auto"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>

              <div className="flex items-start">
                <div className="h-8 w-8 bg-red-100 rounded-full flex items-center justify-center mr-3 mt-1 flex-shrink-0">
                  <span className="font-medium text-red-800">3</span>
                </div>
                <div>
                  <h4 className="font-medium text-gray-900">Increased Risk Exposure</h4>
                  <p className="text-gray-600 text-sm">
                    Compliance violations, operational issues, strategic errors
                  </p>
                </div>
              </div>

              <div className="pl-11">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 text-red-600 mx-auto"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>

              <div className="flex items-start">
                <div className="h-8 w-8 bg-red-100 rounded-full flex items-center justify-center mr-3 mt-1 flex-shrink-0">
                  <span className="font-medium text-red-800">✕</span>
                </div>
                <div>
                  <h4 className="font-medium text-gray-900">Negative Business Outcomes</h4>
                  <p className="text-gray-600 text-sm">
                    Fines, lost time, damaged reputation, remediation costs
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default TruthCascade;
