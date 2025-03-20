import React, { useEffect, useRef, useState } from "react";

const Modal = ({ buttonText }) => {
  const [modalOpen, setModalOpen] = useState(false);
  const [files, setFiles] = useState([]);
  const trigger = useRef(null);
  const modal = useRef(null);

  useEffect(() => {
    const clickHandler = (event) => {
      if (
        modal.current &&
        !modal.current.contains(event.target) &&
        trigger.current &&
        !trigger.current.contains(event.target)
      ) {
        setModalOpen(false);
      }
    };
    document.addEventListener("mousedown", clickHandler);
    return () => document.removeEventListener("mousedown", clickHandler);
  }, [modalOpen]);

  useEffect(() => {
    const keyHandler = (event) => {
      if (event.key === "Escape") {
        setModalOpen(false);
      }
    };
    document.addEventListener("keydown", keyHandler);
    return () => document.removeEventListener("keydown", keyHandler);
  }, [modalOpen]);

  const handleFileChange = (event) => {
    setFiles([...files, ...event.target.files]);
  };

  const removeFile = (index) => {
    setFiles(files.filter((_, i) => i !== index));
  };

  return (
    <>
      <button
        ref={trigger}
        onClick={() => setModalOpen(true)}
        className="rounded-md border border-gray-300 bg-gray-100 px-6 py-3 text-base font-medium text-navy"
      >
        {buttonText || "Open Modal"}
      </button>

      {modalOpen && (
        <div className="fixed inset-0 flex items-center justify-center bg-opacity-30 backdrop-blur-md px-4 py-5 z-50">
          <div
            ref={modal}
            className="w-full max-w-lg rounded-lg bg-white px-8 py-12 text-center shadow-lg border border-gray-300"
          >
            <h3 className="pb-4 text-xl font-semibold text-gray-800 sm:text-2xl">
              Upload Your File
            </h3>
            <span className="mx-auto mb-6 block h-1 w-24 rounded bg-primary"></span>
            <p className="mb-6 text-base text-gray-600">
              Choose a file to upload and submit.
            </p>
            <form className="space-y-4">
              <div>
                <label className="block text-sm font-bold text-gray-600">
                  Attach Document
                </label>
                <div className="flex items-center justify-center w-full">
                  <label className="flex flex-col items-center justify-center w-full h-40 border-2 border-dashed border-gray-300 rounded-lg p-4 cursor-pointer hover:border-indigo-500">
                    <img
                      className="h-24 object-contain"
                      src="https://img.freepik.com/free-vector/image-upload-concept-landing-page_52683-27130.jpg?size=338&ext=jpg"
                      alt="Upload illustration"
                    />
                    <p className="mt-2 text-gray-500">
                      Drag & drop files here or{' '}
                      <span className="text-blue-600 hover:underline">browse</span>
                    </p>
                    <input
                      type="file"
                      className="hidden"
                      multiple
                      onChange={handleFileChange}
                    />
                  </label>
                </div>
                <p className="text-sm text-gray-400 mt-2">
                  Supported file types: pdf
                </p>
                <div className="mt-4 text-left">
                  {files.map((file, index) => (
                    <div key={index} className="flex justify-between items-center bg-gray-100 p-2 rounded-md mt-2">
                      <span className="text-sm text-gray-700">{file.name}</span>
                      <button
                        className="text-red-500 text-sm"
                        onClick={() => removeFile(index)}
                      >
                        Remove
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            </form>
            <div className="mt-6 flex justify-center space-x-4">
              <button
                onClick={() => setModalOpen(false)}
                className="rounded-md border border-red-600 bg-red-600 text-white p-3 text-center text-base font-medium transition hover:bg-red-700"
              >
                Cancel
              </button>
              <button
                className="rounded-md border border-green-600 bg-green-600 text-white p-3 text-center text-base font-medium transition hover:bg-green-700"
              >
                Submit
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

const FormBody = () => {
  return (
    <div className="justify-center flex items-center bg-gray-100 ">
      <div className="w-[60%] h-[70%] bg-white rounded-2xl shadow-lg p-8 border border-gray-300">
        <div className="mb-6 border-b border-gray-300 pb-4">
          <h3 className="text-lg font-medium text-gray-700 mb-2">Upload Proposal Form</h3>
          <Modal buttonText="Upload" />
        </div>
        <div className="border-b border-gray-300 pb-4">
          <h3 className="text-lg font-medium text-gray-700 mb-2">Upload Audited Financial Statements</h3>
          <Modal buttonText="Upload" />
        </div>
      </div>
    </div>
  );
};

const App = () => {
  return <FormBody />;
};

export default App;
