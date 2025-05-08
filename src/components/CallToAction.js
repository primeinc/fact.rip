import React from 'react';

const CallToAction = () => {
  return (
    <>
      {/* CTA Section */}
      <section className="py-16 px-4 sm:px-6 lg:px-8 bg-blue-700">
        <div className="max-w-5xl mx-auto text-center">
          <div className="fade-in-section">
            <h2
              className="text-3xl font-semibold text-white"
              style={{ fontFamily: 'IBM Plex Serif, serif' }}
            >
              Ready to transform your documentation?
            </h2>
            <p className="mt-4 text-xl text-blue-100 max-w-3xl mx-auto">
              Join the organizations building trust through validated information
            </p>

            <div className="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
              <button className="bg-white text-blue-700 hover:bg-blue-50 font-medium py-3 px-6 rounded-md shadow-lg">
                Request Demo
              </button>
              <button className="bg-blue-600 text-white border border-blue-400 hover:bg-blue-800 font-medium py-3 px-6 rounded-md shadow-lg">
                Start Free Trial
              </button>
            </div>

            <div className="mt-10 flex justify-center space-x-8">
              <div className="flex flex-col items-center">
                <div className="text-3xl font-bold text-white">97%</div>
                <div className="text-sm text-blue-100">Citation Accuracy</div>
              </div>

              <div className="flex flex-col items-center">
                <div className="text-3xl font-bold text-white">83%</div>
                <div className="text-sm text-blue-100">Time Saved</div>
              </div>

              <div className="flex flex-col items-center">
                <div className="text-3xl font-bold text-white">100%</div>
                <div className="text-sm text-blue-100">Source Preservation</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Validation Badge */}
      <section className="py-12 px-4 sm:px-6 lg:px-8 bg-white border-t border-gray-200">
        <div className="max-w-7xl mx-auto fade-in-section">
          <div className="flex flex-col md:flex-row items-center justify-between gap-6">
            <div className="flex items-center">
              <div className="h-10 w-10 bg-green-100 rounded-full flex items-center justify-center mr-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6 text-green-700"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>
              <div>
                <div className="text-lg font-medium text-gray-900">Validation Badge Program</div>
                <div className="text-sm text-gray-600">
                  Display your commitment to information integrity
                </div>
              </div>
            </div>

            <div className="text-gray-600 max-w-2xl">
              Add the fact.rip validation badge to your website or documentation to show your
              commitment to information integrity. Our badges dynamically display the validation
              status of your content, building trust with your audience.
            </div>

            <button className="bg-blue-700 hover:bg-blue-800 text-white font-medium py-2 px-4 rounded-md text-sm whitespace-nowrap">
              Learn More
            </button>
          </div>
        </div>
      </section>
    </>
  );
};

export default CallToAction;
