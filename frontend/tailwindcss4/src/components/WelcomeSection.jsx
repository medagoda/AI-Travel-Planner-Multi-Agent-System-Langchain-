import React from 'react';
import { MessageSquareIcon, CalendarIcon, MapIcon } from 'lucide-react';

export function WelcomeSection() {
  return (
    <div className="text-center mb-10 w-full mt-10">
      <h1 className="text-3xl font-bold mb-2 text-gray-800">
        ආයුබෝවන් 🙏🌴🇱🇰✨ ...
      </h1>
      <p className="text-gray-700 text-lg md:text-xl font-medium mb-10 font-sans">
  🧳 Your smart travel companion for exploring Sri Lanka
</p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto">
  <FeatureItem 
    icon={<MessageSquareIcon className="w-8 h-8 text-white" />} 
    textClassName="text-black font-semibold text-lg" 
    text="Tell us where you want to go" 
  />
  <FeatureItem 
    icon={<CalendarIcon className="w-8 h-8 text-white" />} 
    textClassName="text-black font-semibold text-lg" 
    text="Provide your travel dates" 
  />
  <FeatureItem 
    icon={<MapIcon className="w-8 h-8 text-white" />} 
    textClassName="text-black font-semibold text-lg" 
    text="Get complete itinerary" 
  />
</div>

    </div>
  );
}

function FeatureItem({ icon, text }) {
  return (
    <div className="flex flex-col items-center">
      <div className="bg-green-500 p-4 rounded-full mb-4">
        {icon}
      </div>
      <p className="text-black font-semibold text-lg text-center">
        {text}
      </p>
    </div>
  );
}
