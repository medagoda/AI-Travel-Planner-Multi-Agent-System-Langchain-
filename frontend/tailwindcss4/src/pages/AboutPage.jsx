import React from 'react';
import { RocketIcon, HeartIcon, SparklesIcon } from 'lucide-react';
export function AboutPage() {
  return <main className="flex-grow flex flex-col items-center px-4 py-10 max-w-6xl mx-auto w-full">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">
          About <span className="text-6xl font-extrabold text-white tracking-wide drop-shadow-sm">
            Trip <span className="text-yellow-300">Pisso</span>
          </span>
        </h1>
        <p className="text-xl text-gray-600 max-w-2xl mx-auto">
          Your AI-powered travel companion that makes planning your next
          adventure effortless and exciting.
        </p>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16 w-full">
        <FeatureCard icon={<RocketIcon className="w-8 h-8 text-green-600" />} title="Smart Planning" description="Our AI technology creates personalized itineraries based on your preferences and travel style." />
        <FeatureCard icon={<HeartIcon className="w-8 h-8 text-green-600" />} title="Tailored Experience" description="Every suggestion is customized to match your interests, budget, and schedule." />
        <FeatureCard icon={<SparklesIcon className="w-8 h-8 text-green-600" />} title="Real-Time Updates" description="Get instant recommendations and adjustments as your travel needs change." />
      </div>
      <div className="bg-green-50 rounded-2xl p-8 w-full mb-16">
        <h2 className="text-3xl font-bold text-gray-800 mb-6 text-center">
          Our Mission
        </h2>
        <p className="text-gray-600 text-lg text-center max-w-3xl mx-auto">
          At TravelGenie, we believe everyone deserves extraordinary travel
          experiences. Our mission is to combine artificial intelligence with
          human insight to make travel planning seamless, enjoyable, and
          accessible to all.
        </p>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-2xl font-bold text-gray-800 mb-4">
            How It Works
          </h3>
          <ul className="space-y-4 text-gray-600">
            <li className="flex items-start gap-2">
              <span className="font-bold text-green-600">1.</span>
              Tell us your destination and travel dates
            </li>
            <li className="flex items-start gap-2">
              <span className="font-bold text-green-600">2.</span>
              Share your preferences and interests
            </li>
            <li className="flex items-start gap-2">
              <span className="font-bold text-green-600">3.</span>
              Get a personalized travel itinerary
            </li>
            <li className="flex items-start gap-2">
              <span className="font-bold text-green-600">4.</span>
              Refine and adjust until it's perfect
            </li>
          </ul>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-2xl font-bold text-gray-800 mb-4">
            Why Choose Us
          </h3>
          <ul className="space-y-4 text-gray-600">
            <li>✨ AI-powered personalization</li>
            <li>🎯 Precise recommendations</li>
            <li>⚡ Real-time updates</li>
            <li>🤝 24/7 travel assistance</li>
            <li>💡 Smart suggestions</li>
          </ul>
        </div>
      </div>
    </main>;
}
function FeatureCard({
  icon,
  title,
  description
}) {
  return <div className="bg-white p-6 rounded-lg shadow-md text-center">
      <div className="inline-block p-3 bg-green-50 rounded-full mb-4">
        {icon}
      </div>
      <h3 className="text-xl font-semibold text-gray-800 mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>;
}