import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import LoginModal from "../../modals/LoginModal";

const GetStarted = () => {
  const [showScrollPrompt, setShowScrollPrompt] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [cursorPos, setCursorPos] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleScroll = () => {
      setShowScrollPrompt(window.scrollY <= window.innerHeight);
    };

    const handleMouseMove = (e) => {
      setCursorPos({ x: e.clientX, y: e.clientY });
    };

    window.addEventListener("scroll", handleScroll);
    window.addEventListener("mousemove", handleMouseMove);

    return () => {
      window.removeEventListener("scroll", handleScroll);
      window.removeEventListener("mousemove", handleMouseMove);
    };
  }, []);

  return (
    <div className="relative min-h-[50vh] md:min-h-[40vh] flex flex-col items-center text-center p-6 text-gray-100 z-10 overflow-hidden">
      
      {/* Cursor-following blob */}
      <motion.div
        className="fixed top-0 left-0 w-96 h-96 rounded-full bg-gradient-to-r from-[#5973fa] via-[#de23e8] to-[#ff00f2] opacity-10 blur-3xl pointer-events-none -z-50"
        animate={{ x: cursorPos.x - 200, y: cursorPos.y - 200 }}
        transition={{ type: "spring", stiffness: 300, damping: 30 }}
      />

      <motion.h1
        className="text-[70px] sm:text-[80px] md:text-[100px] font-bold leading-tight mt-10"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
      >
        Search Made <br />
        <span className="bg-gradient-to-r from-[#5973fa] via-[#de23e8] to-[#ff00f2] text-transparent bg-clip-text transition-all duration-200 hover:drop-shadow-xl">
          Simple
        </span>
      </motion.h1>

      <motion.p
        className="mt-4 text-xl sm:text-2xl max-w-2xl text-[#f5f5f5]"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, ease: "easeOut", delay: 0.2 }}
      >
        Mimir helps you find the most relevant information effortlessly, using
        advanced AI-powered search and retrieval.
      </motion.p>

      <motion.button
        className="mt-14 px-6 py-4 bg-gray-100 text-black rounded-xl text-xl sm:text-2xl hover:bg-gray-300 transition"
        onClick={() => setIsModalOpen(true)}
      >
        Try Mimir
      </motion.button>

      {/* Modal */}
      <LoginModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
    </div>
  );
};

export default GetStarted;
