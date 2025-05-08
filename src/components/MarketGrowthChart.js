import React from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from 'recharts';

// Market growth data
const marketGrowthData = [
  { year: 2022, value: 400 },
  { year: 2023, value: 550 },
  { year: 2024, value: 750 },
  { year: 2025, value: 1050 },
  { year: 2026, value: 1450 },
  { year: 2027, value: 1950 },
  { year: 2028, value: 2650 },
  { year: 2029, value: 3600 },
  { year: 2030, value: 4900 },
  { year: 2031, value: 6700 },
  { year: 2032, value: 9200 },
];

// Constants for brand colors
const COLORS = {
  truthBlue: '#0F52BA',
};

const MarketGrowthChart = () => {
  return (
    <section className="py-16 px-4 sm:px-6 lg:px-8 bg-gray-50">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8 fade-in-section">
          <h2
            className="text-3xl font-semibold text-gray-900"
            style={{ fontFamily: 'IBM Plex Serif, serif' }}
          >
            Explosive Growth in Documentation-as-a-Service
          </h2>
          <p className="mt-4 text-xl text-gray-600 max-w-3xl mx-auto">
            35-40% CAGR through 2032 as organizations recognize documentation as a critical business
            asset
          </p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg h-80 fade-in-section">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart
              data={marketGrowthData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis
                label={{ value: 'Market Size (Billions USD)', angle: -90, position: 'insideLeft' }}
              />
              <Tooltip formatter={value => [`$${value}B`, 'Market Size']} />
              <Line
                type="monotone"
                dataKey="value"
                stroke={COLORS.truthBlue}
                strokeWidth={3}
                dot={{ r: 4, fill: COLORS.truthBlue }}
                activeDot={{ r: 6 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </section>
  );
};

export default MarketGrowthChart;
