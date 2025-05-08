import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/logo.jpg'; // Adjust path as needed

export function Header() {
  return (
    <header className="w-full bg-gradient-to-r from-green-600 to-green-400 text-white p-4">
      <div className="max-w-6xl mx-auto flex justify-between items-center">
        <div className="flex items-center">
          <div className="bg-green-800 rounded-full p-2 mr-2">
            <img
              src={logo}
              alt="Logo"
              className="w-10 h-10 object-contain rounded-full"
            />
          </div>
          <span className="text-2xl font-extrabold text-white tracking-wide drop-shadow-sm">
            Trip <span className="text-yellow-300">Pisso</span>
          </span>
        </div>
        <nav>
          <ul className="flex space-x-6">
            <li>
              <Link to="/" className="bg-green-500/30 hover:bg-green-500/40 px-4 py-2 rounded-md">
                Home
              </Link>
            </li>
            <li>
              <Link to="/about" className="bg-green-500/30 hover:bg-green-500/40 px-4 py-2 rounded-md">
                About
              </Link>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
}
