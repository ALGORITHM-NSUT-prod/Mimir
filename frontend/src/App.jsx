import React from 'react'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from './pages/LandingPage'
import ChatPage from './pages/ChatPage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage /> } />
        <Route path="/new" element={<ChatPage /> } />


      </Routes>
      

    </Router>
  )
}

export default App