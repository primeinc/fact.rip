import React, { useState } from 'react';
import ContentCreatorsTab from './audience-tabs/ContentCreatorsTab';
import ComplianceOfficersTab from './audience-tabs/ComplianceOfficersTab';
import KnowledgeManagersTab from './audience-tabs/KnowledgeManagersTab';
import TechnicalWritersTab from './audience-tabs/TechnicalWritersTab';

const AudienceTabs = () => {
  const [activeTab, setActiveTab] = useState('contentCreators');

  return (
    <section id="audiences" className="py-16 px-4 sm:px-6 lg:px-8 bg-white">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12 fade-in-section">
          <h2
            className="text-3xl font-semibold text-gray-900"
            style={{ fontFamily: 'IBM Plex Serif, serif' }}
          >
            Who benefits from fact.rip?
          </h2>
          <p className="mt-4 text-xl text-gray-600 max-w-3xl mx-auto">
            Tailored solutions for different documentation stakeholders
          </p>
        </div>

        <div className="bg-white rounded-lg shadow-lg overflow-hidden fade-in-section">
          <div className="border-b border-gray-200">
            <nav className="flex">
              <button
                className={`px-6 py-4 text-center w-1/4 font-medium text-sm ${activeTab === 'contentCreators' ? 'border-b-2 border-blue-700 text-blue-700' : 'text-gray-500 hover:text-gray-700'}`}
                onClick={() => setActiveTab('contentCreators')}
              >
                Content Creators
              </button>
              <button
                className={`px-6 py-4 text-center w-1/4 font-medium text-sm ${activeTab === 'complianceOfficers' ? 'border-b-2 border-blue-700 text-blue-700' : 'text-gray-500 hover:text-gray-700'}`}
                onClick={() => setActiveTab('complianceOfficers')}
              >
                Compliance Officers
              </button>
              <button
                className={`px-6 py-4 text-center w-1/4 font-medium text-sm ${activeTab === 'knowledgeManagers' ? 'border-b-2 border-blue-700 text-blue-700' : 'text-gray-500 hover:text-gray-700'}`}
                onClick={() => setActiveTab('knowledgeManagers')}
              >
                Knowledge Managers
              </button>
              <button
                className={`px-6 py-4 text-center w-1/4 font-medium text-sm ${activeTab === 'technicalWriters' ? 'border-b-2 border-blue-700 text-blue-700' : 'text-gray-500 hover:text-gray-700'}`}
                onClick={() => setActiveTab('technicalWriters')}
              >
                Technical Writers
              </button>
            </nav>
          </div>

          <div className="p-8">
            {activeTab === 'contentCreators' && <ContentCreatorsTab />}
            {activeTab === 'complianceOfficers' && <ComplianceOfficersTab />}
            {activeTab === 'knowledgeManagers' && <KnowledgeManagersTab />}
            {activeTab === 'technicalWriters' && <TechnicalWritersTab />}
          </div>
        </div>
      </div>
    </section>
  );
};

export default AudienceTabs;
