import React from 'react';
import { SendIcon } from 'lucide-react';
import logo from '../assets/logo.jpg'; 
export function ChatInterface() {
  return <div className="w-full max-w-4xl bg-white rounded-lg shadow-lg overflow-hidden m-auto mt-10">
      <div className="bg-gradient-to-r from-green-600 to-green-400 text-white p-3">
        <h2 className="font-semibold">TripAdvisor Assistant</h2>
      </div>
      <div className="p-4 min-h-[300px] bg-gray-50">
        <div className="flex mb-4">
          <div className="bg-green-500 rounded-full p-2 mr-3">
          <img
              src={logo}
              alt="Logo"
              className="w-10 h-10 object-contain rounded-full"
            />
          </div>
          <div className="bg-white p-3 rounded-lg shadow-sm max-w-[80%]">
            <p>
              👋 Hi! I'm Your TripAdvisor. Tell me about your trip and I'll build
              your itinerary!
            </p>
          </div>
        </div>
      </div>
      <div className="border-t p-3 flex">
        <input type="text" placeholder="Type your message..." className="flex-grow border rounded-l-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-green-500" />
        <button className="bg-green-500 text-white px-4 py-2 rounded-r-lg hover:bg-green-600">
          <SendIcon className="w-5 h-5" />
        </button>
      </div>
    </div>;
}