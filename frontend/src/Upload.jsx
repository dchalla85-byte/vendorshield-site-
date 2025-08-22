import React, { useState } from "react";
import axios from "axios";

function Upload() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:8000/scan", formData);
    setResult(res.data);
  };

  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold mb-4">Upload Invoice</h2>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <br />
      <button onClick={handleUpload} className="bg-blue-600 px-4 py-2 rounded">
        Scan
      </button>

      {result && (
        <div className="mt-6 bg-gray-800 p-4 rounded">
          <h3 className="font-bold text-lg">Scan Result</h3>
          <p>{result.summary}</p>
          <ul className="mt-2 list-disc list-inside">
            {result.flags.map((flag, i) => (
              <li key={i}>{flag.line} — {flag.reason}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default Upload;
