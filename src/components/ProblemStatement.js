import React from 'react';

const ProblemStatement = () => {
  return (
    <section className="py-16 px-4 sm:px-6 lg:px-8 bg-white">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12 fade-in-section">
          <h2
            className="text-3xl font-semibold text-gray-900"
            style={{ fontFamily: 'IBM Plex Serif, serif' }}
          >
            The urgent need for verified documentation
          </h2>
          <p className="mt-4 text-xl text-gray-600 max-w-3xl mx-auto">
            In today's information ecosystem, organizations face a crisis of documentation
            reliability.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 fade-in-section">
          <div className="bg-gray-50 p-6 rounded-lg">
            <div className="h-12 w-12 bg-red-100 rounded-lg flex items-center justify-center mb-4">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6 text-red-700"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fillRule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clipRule="evenodd"
                />
              </svg>
            </div>
            <h3 className="text-lg font-medium text-gray-900 mb-2">Invalid Citations</h3>
            <p className="text-gray-600">
              Outdated references and broken links undermine the reliability of critical business
              information.
            </p>
          </div>

          <div className="bg-gray-50 p-6 rounded-lg">
            <div className="h-12 w-12 bg-amber-100 rounded-lg flex items-center justify-center mb-4">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6 text-amber-700"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fillRule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clipRule="evenodd"
                />
              </svg>
            </div>
            <h3 className="text-lg font-medium text-gray-900 mb-2">Logical Inconsistencies</h3>
            <p className="text-gray-600">
              Faulty reasoning and contradictions lead to flawed decision-making and strategic
              errors.
            </p>
          </div>

          <div className="bg-gray-50 p-6 rounded-lg">
            <div className="h-12 w-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6 text-blue-700"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fillRule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z"
                  clipRule="evenodd"
                />
              </svg>
            </div>
            <h3 className="text-lg font-medium text-gray-900 mb-2">Link Rot</h3>
            <p className="text-gray-600">
              Critical sources disappear over time, making it impossible to verify the foundation of
              important decisions.
            </p>
          </div>
        </div>

        <div className="mt-12 bg-gray-50 p-6 rounded-lg fade-in-section">
          <div className="flex items-start">
            <div className="h-10 w-10 bg-red-100 rounded-full flex items-center justify-center mr-4 mt-1 flex-shrink-0">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5 text-red-700"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fillRule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clipRule="evenodd"
                />
              </svg>
            </div>
            <div>
              <h3 className="text-lg font-medium text-gray-900 mb-2">Real-world impact</h3>
              <p className="text-gray-600">
                Our founder experienced this firsthand at a major financial institution where a{' '}
                <strong>
                  single unvalidated citation in a compliance document led to a $1.2 million
                  regulatory fine
                </strong>
                . The documentation platform had failed to verify that the cited regulation had been
                updated six months earlier.
              </p>
            </div>
          </div>
        </div>

        <div className="mt-12 text-center fade-in-section">
          <p className="text-xl font-medium text-blue-700">
            Despite the $1.6-2.3 trillion projected Documentation-as-a-Service market by 2032,{' '}
            <br />
            <span className="font-semibold">
              no platform currently offers integrated citation validation, logic verification, and
              source archiving.
            </span>
          </p>
        </div>
      </div>
    </section>
  );
};

export default ProblemStatement;
