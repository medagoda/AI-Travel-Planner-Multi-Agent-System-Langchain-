import React from 'react';
import { MapIcon, PlaneIcon, PhoneIcon } from 'lucide-react';
export function Footer() {
  return <footer className="w-full bg-gradient-to-b from-green-50 to-green-100 mt-10">
      <div className="max-w-6xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
          <div>
            <h3 className="text-lg font-semibold text-green-800 mb-4">
              TravelGenie
            </h3>
            <p className="text-gray-600">
              Your AI-powered travel companion for creating perfect travel
              itineraries.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-green-800 mb-4">
              Quick Links
            </h3>
            <ul className="space-y-2">
              <li>
                <a href="#" className="text-gray-600 hover:text-green-600 flex items-center gap-2">
                  <MapIcon className="w-4 h-4" />
                  Destinations
                </a>
              </li>
              <li>
                <a href="#" className="text-gray-600 hover:text-green-600 flex items-center gap-2">
                  <PlaneIcon className="w-4 h-4" />
                  Trip Planning
                </a>
              </li>
              <li>
                <a href="#" className="text-gray-600 hover:text-green-600 flex items-center gap-2">
                  <PhoneIcon className="w-4 h-4" />
                  Support
                </a>
              </li>
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-green-800 mb-4">
              Newsletter
            </h3>
            <p className="text-gray-600 mb-4">
              Subscribe for travel tips and updates.
            </p>
            <div className="flex">
              <input type="email" placeholder="Enter your email" className="flex-grow px-4 py-2 rounded-l-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500" />
              <button className="bg-green-500 text-white px-4 py-2 rounded-r-lg hover:bg-green-600">
                Subscribe
              </button>
            </div>
          </div>
        </div>
        <div className="border-t border-green-200 pt-4">
          <p className="text-center text-gray-600">
            © 2024 ආයුබෝවන් 🙏🌴🇱🇰✨. All rights reserved.
          </p>
        </div>
      </div>
    </footer>;
}