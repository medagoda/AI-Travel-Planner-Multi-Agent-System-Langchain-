import { useState } from 'react'
import './App.css'
import { ChatInterface } from './components/ChatInterface'
import { Header } from './components/Header'
import { WelcomeSection } from './components/WelcomeSection'
import { Footer } from './components/Footer'
import { HomePage } from './pages/HomePage'
import { AboutPage } from './pages/AboutPage'
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  const [count, setCount] = useState(0)

  return <BrowserRouter>
      <div className="flex flex-col min-h-screen w-full bg-gradient-to-b from-green-100 to-white">
        <Header />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
        </Routes>
        <Footer />
      </div>
    </BrowserRouter>;
}

export default App
