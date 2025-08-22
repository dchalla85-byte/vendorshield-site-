import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-gray-800 p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">InvoiceGuard AI</h1>
      <div className="space-x-4">
        <Link to="/" className="hover:text-blue-400">Home</Link>
        <Link to="/upload" className="hover:text-blue-400">Scan</Link>
        <Link to="/history" className="hover:text-blue-400">History</Link>
        <Link to="/support" className="hover:text-blue-400">Support</Link>
      </div>
    </nav>
  );
}

export default Navbar;
