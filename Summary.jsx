import React from "react";

const Summary = () => {
  return (
    <div className="w-3/5 mx-auto bg-white rounded-lg shadow-lg p-8 border border-gray-300 mt-3 h-5/6 pb-4">
      <h2 className="text-2xl font-semibold text-left text-gray-800 mb-6">
        Extracted Summary
      </h2>
      <div className="p-8 border border-gray-200 rounded-md mb-6 h-40">
        <p className="text-gray-700">This section contains the extracted summary details.</p>
      </div>
      <h2 className="text-2xl font-semibold text-left text-gray-800 mb-6">
        Quotation Calculations
      </h2>
      <div className="p-8 border border-gray-200 rounded-md h-40 mb-6">
        <p className="text-gray-700">This section will contain the quotation calculations.</p>
      </div>
      <div className="text-center">
        <button className="px-6 py-3 bg-blue-600 text-white rounded-md hover:bg-blue-700">
          Download Excel Sheet
        </button>
      </div>
    </div>
  );
};

export default Summary;
