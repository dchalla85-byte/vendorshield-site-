import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="p-8 text-center">
      <h2 className="text-4xl font-bold mb-4">Stop Hidden Vendor Price Hikes</h2>
      <p className="mb-6 text-gray-300">
        We scan your invoices, flag silent increases, and give you ready-to-send negotiation emails.
      </p>
      <Link to="/upload">
        <button className="bg-blue-600 px-6 py-3 rounded hover:bg-blue-700">
          Upload Invoice
        </button>
      </Link>
    </div>
  );
}

export default Home;
