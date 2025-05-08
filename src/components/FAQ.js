import React, { useState } from 'react';

const FAQ = () => {
  const [activeFaq, setActiveFaq] = useState(null);

  const toggleFaq = index => {
    setActiveFaq(activeFaq === index ? null : index);
  };

  return (
    <section id="faq" className="py-16 px-4 sm:px-6 lg:px-8 bg-gray-50">
      <div className="max-w-3xl mx-auto">
        <div className="text-center mb-12 fade-in-section">
          <h2
            className="text-3xl font-semibold text-gray-900"
            style={{ fontFamily: 'IBM Plex Serif, serif' }}
          >
            Frequently Asked Questions
          </h2>
          <p className="mt-4 text-xl text-gray-600">Common questions about fact.rip</p>
        </div>

        <div className="space-y-4 fade-in-section">
          <div className="bg-white rounded-lg shadow-sm overflow-hidden">
            <button
              className="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
              onClick={() => toggleFaq(0)}
            >
              <span className="font-medium text-gray-900">
                How does fact.rip validate citations?
              </span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className={`h-5 w-5 text-gray-500 transition-transform ${activeFaq === 0 ? 'transform rotate-180' : ''}`}
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

            {activeFaq === 0 && (
              <div className="px-6 py-4 border-t border-gray-100">
                <p className="text-gray-600">
                  fact.rip uses a proprietary AI system to validate citations against their original
                  sources. The system checks for content accuracy, currency, and contextual
                  relevance. It can detect when a citation no longer matches its source due to
                  updates, when information is taken out of context, and when logical
                  inconsistencies exist between citations and claims.
                </p>
              </div>
            )}
          </div>

          <div className="bg-white rounded-lg shadow-sm overflow-hidden">
            <button
              className="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
              onClick={() => toggleFaq(1)}
            >
              <span className="font-medium text-gray-900">
                How does fact.rip's source archiving work?
              </span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className={`h-5 w-5 text-gray-500 transition-transform ${activeFaq === 1 ? 'transform rotate-180' : ''}`}
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

            {activeFaq === 1 && (
              <div className="px-6 py-4 border-t border-gray-100">
                <p className="text-gray-600">
                  When a citation is created, fact.rip automatically archives the original source
                  content in its secure repository. This creates a permanent record of the source at
                  the time of citation, protecting against link rot, content changes, or source
                  removal. The archive is timestamped and preserved indefinitely, allowing for
                  verification even years after the original citation was created.
                </p>
              </div>
            )}
          </div>

          <div className="bg-white rounded-lg shadow-sm overflow-hidden">
            <button
              className="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
              onClick={() => toggleFaq(2)}
            >
              <span className="font-medium text-gray-900">
                Can fact.rip integrate with our existing documentation system?
              </span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className={`h-5 w-5 text-gray-500 transition-transform ${activeFaq === 2 ? 'transform rotate-180' : ''}`}
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

            {activeFaq === 2 && (
              <div className="px-6 py-4 border-t border-gray-100">
                <p className="text-gray-600">
                  Yes, fact.rip is designed to integrate with popular documentation systems through
                  our API. We offer direct integrations with major platforms like Confluence,
                  SharePoint, Google Docs, and specialized documentation tools. For custom systems,
                  our developer-friendly API allows for seamless integration, bringing validation
                  capabilities to your existing workflow without disruption.
                </p>
              </div>
            )}
          </div>

          <div className="bg-white rounded-lg shadow-sm overflow-hidden">
            <button
              className="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
              onClick={() => toggleFaq(3)}
            >
              <span className="font-medium text-gray-900">
                How does fact.rip handle different types of sources?
              </span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className={`h-5 w-5 text-gray-500 transition-transform ${activeFaq === 3 ? 'transform rotate-180' : ''}`}
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

            {activeFaq === 3 && (
              <div className="px-6 py-4 border-t border-gray-100">
                <p className="text-gray-600">
                  fact.rip supports a wide range of source types including web pages, PDFs, academic
                  journals, internal documents, regulatory filings, and specialized databases. Our
                  system adapts its validation approach based on the source type, applying different
                  verification methods for regulatory documents versus news articles, for example.
                  We also provide source reliability assessments based on authoritativeness,
                  currency, and historical accuracy.
                </p>
              </div>
            )}
          </div>

          <div className="bg-white rounded-lg shadow-sm overflow-hidden">
            <button
              className="w-full px-6 py-4 text-left flex justify-between items-center focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
              onClick={() => toggleFaq(4)}
            >
              <span className="font-medium text-gray-900">
                What about sensitive or confidential information?
              </span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className={`h-5 w-5 text-gray-500 transition-transform ${activeFaq === 4 ? 'transform rotate-180' : ''}`}
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

            {activeFaq === 4 && (
              <div className="px-6 py-4 border-t border-gray-100">
                <p className="text-gray-600">
                  fact.rip prioritizes security for sensitive information. We offer private cloud
                  and on-premises deployment options for organizations with strict data handling
                  requirements. Our platform uses enterprise-grade encryption, role-based access
                  controls, and detailed audit logs to protect confidential content while still
                  providing validation benefits.
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
};

export default FAQ;
