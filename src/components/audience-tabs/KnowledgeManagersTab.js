import React from 'react';

const KnowledgeManagersTab = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div className="md:col-span-1">
        <h3 className="text-xl font-medium text-gray-900 mb-4">For Knowledge Managers</h3>
        <p className="text-gray-600 mb-4">Never lose critical sources with automatic archiving.</p>
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
              Link rot and disappearing sources
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
              Siloed knowledge across organization
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
              No system for tracking information quality
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
                    <path d="M5.5 16a3.5 3.5 0 01-.369-6.98 4 4 0 117.753-1.977A4.5 4.5 0 1113.5 16h-8z" />
                  </svg>
                </div>
                <div>
                  <h5 className="font-medium text-gray-900 mb-1">Permanent archiving</h5>
                  <p className="text-gray-600">
                    Automatically archives all referenced sources at the moment of citation,
                    creating a permanent record that protects against link rot and content changes.
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
                    <path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z" />
                  </svg>
                </div>
                <div>
                  <h5 className="font-medium text-gray-900 mb-1">Knowledge mapping</h5>
                  <p className="text-gray-600">
                    Creates a comprehensive map of citations and sources across your organization,
                    identifying knowledge connections and dependencies.
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
                    <path
                      fillRule="evenodd"
                      d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm5 6a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V8z"
                      clipRule="evenodd"
                    />
                  </svg>
                </div>
                <div>
                  <h5 className="font-medium text-gray-900 mb-1">Content governance metrics</h5>
                  <p className="text-gray-600">
                    Provides quantitative measures of documentation quality, helping you identify
                    areas for improvement and track progress over time.
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
                    "With fact.rip, we recovered critical historical information that would have
                    been lost due to website changes. The archiving feature alone has saved us
                    countless hours of research and reconstruction."
                  </div>
                  <div className="mt-2 text-sm font-medium">
                    Jennifer Taylor, Knowledge Management Director at Tech Innovations
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

export default KnowledgeManagersTab;
