import React from "react";
import { HashRouter, Routes, Route } from "react-router-dom";
import Navbar from "./Navbar";
import Home from "./Home";
import Upload from "./Upload";
import History from "./History";
import Support from "./Support";

function App() {
  return (
    <HashRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/history" element={<History />} />
        <Route path="/support" element={<Support />} />
      </Routes>
    </HashRouter>
  );
}

export default App;
