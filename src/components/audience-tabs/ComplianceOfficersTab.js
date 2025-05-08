import React from 'react';

const ComplianceOfficersTab = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div className="md:col-span-1">
        <h3 className="text-xl font-medium text-gray-900 mb-4">For Compliance Officers</h3>
        <p className="text-gray-600 mb-4">
          Ensure compliance with automatic validation of regulatory citations.
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
              Risk of outdated or incorrect information
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
              Difficulty tracking regulatory changes
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
              No clear audit trail for regulatory citations
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
                      d="M10 1.944A11.954 11.954 0 012.166 5C2.056 5.649 2 6.319 2 7c0 5.225 3.34 9.67 8 11.317C14.66 16.67 18 12.225 18 7c0-.682-.057-1.35-.166-2.001A11.954 11.954 0 0110 1.944zM11 14a1 1 0 11-2 0 1 1 0 012 0zm0-7a1 1 0 10-2 0v3a1 1 0 102 0V7z"
                      clipRule="evenodd"
                    />
                  </svg>
                </div>
                <div>
                  <h5 className="font-medium text-gray-900 mb-1">Regulatory change detection</h5>
                  <p className="text-gray-600">
                    Automatically monitors for updates to regulations and standards cited in your
                    documentation, alerting you to changes that may affect compliance.
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
                      d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
                      clipRule="evenodd"
                    />
                  </svg>
                </div>
                <div>
                  <h5 className="font-medium text-gray-900 mb-1">Comprehensive audit trails</h5>
                  <p className="text-gray-600">
                    Maintains immutable records of all validations, changes, and verifications,
                    creating a defensible compliance history for auditors and regulators.
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
                    <path d="M15 8a3 3 0 10-2.977-2.63l-4.94 2.47a3 3 0 100 4.319l4.94 2.47a3 3 0 10.895-1.789l-4.94-2.47a3.027 3.027 0 000-.74l4.94-2.47C13.456 7.68 14.19 8 15 8z" />
                  </svg>
                </div>
                <div>
                  <h5 className="font-medium text-gray-900 mb-1">Compliance documentation</h5>
                  <p className="text-gray-600">
                    Generates verification reports for internal and external audits, showing all
                    validation steps and archiving key regulatory sources.
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
                    "fact.rip prevented a potential regulatory fine by alerting us to a critical
                    update in financial reporting requirements that our previous system missed. The
                    ROI was immediate."
                  </div>
                  <div className="mt-2 text-sm font-medium">
                    Michael Rodriguez, Chief Compliance Officer at Global Financial
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

export default ComplianceOfficersTab;
