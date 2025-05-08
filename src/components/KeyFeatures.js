import React, { useState } from 'react';

const KeyFeatures = () => {
  const [showFeatureDetails, setShowFeatureDetails] = useState({
    citation: false,
    logic: false,
    archive: false,
  });

  const toggleFeatureDetail = feature => {
    setShowFeatureDetails({
      ...showFeatureDetails,
      [feature]: !showFeatureDetails[feature],
    });
  };

  return (
    <section id="features" className="py-16 px-4 sm:px-6 lg:px-8 bg-white">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12 fade-in-section">
          <h2
            className="text-3xl font-semibold text-gray-900"
            style={{ fontFamily: 'IBM Plex Serif, serif' }}
          >
            The fact.rip solution
          </h2>
          <p className="mt-4 text-xl text-gray-600 max-w-3xl mx-auto">
            A comprehensive platform where AI governance ensures documentation integrity
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Citation Validation */}
          <div className="bg-white border border-gray-200 rounded-lg overflow-hidden shadow-lg transition-all duration-300 hover:shadow-xl fade-in-section">
            <div className="p-6 bg-blue-700 text-white">
              <div className="flex items-center justify-between">
                <h3 className="text-xl font-medium">Citation Validation</h3>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z" />
                </svg>
              </div>
            </div>
            <div className="p-6">
              <p className="text-gray-600 mb-4">
                Automatically verify citations against original sources to ensure accuracy and
                currency.
              </p>
              <div className="space-y-3 mb-4">
                <div className="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5 text-green-600 mr-2"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="text-sm">Content verification</span>
                </div>
                <div className="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5 text-green-600 mr-2"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="text-sm">Currency validation</span>
                </div>
                <div className="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5 text-green-600 mr-2"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="text-sm">Source reputation assessment</span>
                </div>
              </div>
              <button
                className="text-blue-700 font-medium text-sm hover:text-blue-800 flex items-center"
                onClick={() => toggleFeatureDetail('citation')}
              >
                {showFeatureDetails.citation ? 'Show less' : 'Learn more'}
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className={`h-4 w-4 ml-1 transition-transform ${showFeatureDetails.citation ? 'rotate-180' : ''}`}
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                    clipRule="evenodd"
                  />
                </svg>
              </button>

              {showFeatureDetails.citation && (
                <div className="mt-4 pt-4 border-t border-gray-100">
                  <p className="text-sm text-gray-600 mb-3">
                    Our AI engine compares citation content with original sources, detecting
                    discrepancies, outdated information, and contextual inaccuracies. It alerts you
                    to regulatory changes, updated statistics, and evolving industry standards.
                  </p>
                  <div className="bg-blue-50 p-3 rounded-md text-sm text-blue-800">
                    <div className="font-medium mb-1">Real impact:</div>
                    <p>
                      A financial services client avoided $1.2M in fines when fact.rip caught an
                      outdated regulatory citation before document publication.
                    </p>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Logic Verification */}
          <div className="bg-white border border-gray-200 rounded-lg overflow-hidden shadow-lg transition-all duration-300 hover:shadow-xl fade-in-section">
            <div className="p-6 bg-blue-700 text-white">
              <div className="flex items-center justify-between">
                <h3 className="text-xl font-medium">Logic Verification</h3>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>
            </div>
            <div className="p-6">
              <p className="text-gray-600 mb-4">
                Detect logical inconsistencies, contradictions, and flawed reasoning in your
                documentation.
              </p>
              <div className="space-y-3 mb-4">
                <div className="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5 text-green-600 mr-2"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="text-sm">Contradiction detection</span>
                </div>
                <div className="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5 text-green-600 mr-2"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="text-sm">Reasoning analysis</span>
                </div>
                <div className="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5 text-green-600 mr-2"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="text-sm">Fallacy identification</span>
                </div>
              </div>
              <button
                className="text-blue-700 font-medium text-sm hover:text-blue-800 flex items-center"
                onClick={() => toggleFeatureDetail('logic')}
              >
                {showFeatureDetails.logic ? 'Show less' : 'Learn more'}
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className={`h-4 w-4 ml-1 transition-transform ${showFeatureDetails.logic ? 'rotate-180' : ''}`}
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                    clipRule="evenodd"
                  />
                </svg>
              </button>

              {showFeatureDetails.logic && (
                <div className="mt-4 pt-4 border-t border-gray-100">
                  <p className="text-sm text-gray-600 mb-3">
                    Our logic engine analyzes the structure of arguments, identifies logical
                    fallacies, and detects contradictions between different sections of your
                    documentation. It ensures internal consistency and sound reasoning throughout
                    your content.
                  </p>
                  <div className="bg-blue-50 p-3 rounded-md text-sm text-blue-800">
                    <div className="font-medium mb-1">Real impact:</div>
                    <p>
                      A healthcare provider avoided implementing contradictory protocols when
                      fact.rip identified logical inconsistencies between their emergency procedures
                      and standard operating guidelines.
                    </p>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Source Archiving */}
          <div className="bg-white border border-gray-200 rounded-lg overflow-hidden shadow-lg transition-all duration-300 hover:shadow-xl fade-in-section">
            <div className="p-6 bg-blue-700 text-white">
              <div className="flex items-center justify-between">
                <h3 className="text-xl font-medium">Source Archiving</h3>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path d="M4 3a2 2 0 100 4h12a2 2 0 100-4H4z" />
                  <path
                    fillRule="evenodd"
                    d="M3 8h14v7a2 2 0 01-2 2H5a2 2 0 01-2-2V8zm5 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>
            </div>
            <div className="p-6">
              <p className="text-gray-600 mb-4">
                Permanently preserve original sources to ensure long-term verification and
                compliance.
              </p>
              <div className="space-y-3 mb-4">
                <div className="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5 text-green-600 mr-2"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="text-sm">Automatic preservation</span>
                </div>
                <div className="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5 text-green-600 mr-2"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="text-sm">Version history</span>
                </div>
                <div className="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5 text-green-600 mr-2"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="text-sm">Change tracking</span>
                </div>
              </div>
              <button
                className="text-blue-700 font-medium text-sm hover:text-blue-800 flex items-center"
                onClick={() => toggleFeatureDetail('archive')}
              >
                {showFeatureDetails.archive ? 'Show less' : 'Learn more'}
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className={`h-4 w-4 ml-1 transition-transform ${showFeatureDetails.archive ? 'rotate-180' : ''}`}
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                    clipRule="evenodd"
                  />
                </svg>
              </button>

              {showFeatureDetails.archive && (
                <div className="mt-4 pt-4 border-t border-gray-100">
                  <p className="text-sm text-gray-600 mb-3">
                    Our archiving system captures and preserves all source materials at the moment
                    of citation, creating a permanent record that protects against link rot and
                    content changes. Each archive is timestamped, creating an immutable record for
                    compliance and verification.
                  </p>
                  <div className="bg-blue-50 p-3 rounded-md text-sm text-blue-800">
                    <div className="font-medium mb-1">Real impact:</div>
                    <p>
                      A legal team successfully defended a contract dispute by providing archived
                      versions of regulatory guidance that had since been removed from government
                      websites.
                    </p>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default KeyFeatures;
