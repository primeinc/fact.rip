import React from 'react';

const TechnicalWritersTab = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div className="md:col-span-1">
        <h3 className="text-xl font-medium text-gray-900 mb-4">For Technical Writers</h3>
        <p className="text-gray-600 mb-4">
          Catch logical errors before they become published mistakes.
        </p>
        <div className="bg-blue-50 p-4 rounded-lg">
          <div className="font-medium text-gray-900 mb-2">Pain Points:</div>
          <ul className="space-y-2 text-gray-700">
            <li className="flex items-start">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5 text-red-500 mr-2 flex-shrink-0 mt-0.5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fillRule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clipRule="evenodd"
                />
              </svg>
              Logical inconsistencies in documentation
            </li>
            <li className="flex items-start">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5 text-red-500 mr-2 flex-shrink-0 mt-0.5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fillRule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clipRule="evenodd"
                />
              </svg>
              Time-consuming technical reviews
            </li>
            <li className="flex items-start">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5 text-red-500 mr-2 flex-shrink-0 mt-0.5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fillRule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clipRule="evenodd"
                />
              </svg>
              Difficulty maintaining accuracy across document versions
            </li>
          </ul>
        </div>
      </div>

      <div className="md:col-span-2">
        <div className="bg-white border border-gray-200 rounded-lg overflow-hidden h-full">
          <div className="p-6">
            <h4 className="font-medium text-gray-900 mb-4">How fact.rip helps</h4>
            <div className="space-y-6">
              <div className="flex items-start">
                <div className="h-10 w-10 bg-green-100 rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6 text-green-700"
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
                  <h5 className="font-medium text-gray-900 mb-1">Logic verification</h5>
                  <p className="text-gray-600">
                    Identifies logical inconsistencies, contradictions, and procedural errors in
                    technical documentation before publication.
                  </p>
                </div>
              </div>

              <div className="flex items-start">
                <div className="h-10 w-10 bg-green-100 rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6 text-green-700"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
                  </svg>
                </div>
                <div>
                  <h5 className="font-medium text-gray-900 mb-1">Streamlined review workflows</h5>
                  <p className="text-gray-600">
                    Automates technical review processes by validating content against established
                    standards and previous versions.
                  </p>
                </div>
              </div>

              <div className="flex items-start">
                <div className="h-10 w-10 bg-green-100 rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6 text-green-700"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path d="M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM2 11a2 2 0 012-2h12a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4z" />
                  </svg>
                </div>
                <div>
                  <h5 className="font-medium text-gray-900 mb-1">Cross-document consistency</h5>
                  <p className="text-gray-600">
                    Ensures terminology, procedures, and technical details remain consistent across
                    documentation sets and product versions.
                  </p>
                </div>
              </div>
            </div>

            <div className="mt-6 border-t border-gray-200 pt-6">
              <div className="flex items-start">
                <div className="flex-shrink-0 mr-4">
                  <div className="h-10 w-10 rounded-full bg-blue-100 overflow-hidden flex items-center justify-center">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      className="h-6 w-6 text-blue-700"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        fillRule="evenodd"
                        d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </div>
                </div>
                <div>
                  <div className="text-sm italic text-gray-600">
                    "fact.rip identified three critical logical errors in our API documentation that
                    multiple human reviewers missed. It's like having an extra team member who never
                    gets tired or distracted."
                  </div>
                  <div className="mt-2 text-sm font-medium">
                    David Park, Technical Documentation Manager at CloudSoft
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TechnicalWritersTab;
