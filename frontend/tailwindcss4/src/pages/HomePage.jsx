import React from 'react';
import { WelcomeSection } from '../components/WelcomeSection';
import { ChatInterface } from '../components/ChatInterface';
import { Header } from '../components/Header';
import { Footer } from '../components/Footer';
export function HomePage() {
  return <main className="flex-grow flex flex-col items-center px-4 py-10 max-w-6xl mx-auto w-full">
      
      <WelcomeSection />
      <ChatInterface />
      
    </main>;
}