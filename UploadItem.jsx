import { TrashIcon, CheckCircleIcon, ArrowPathIcon } from "@heroicons/react/24/outline";

function UploadItem({ file }) {
  const getProgressColor = () => {
    if (file.progress === 100) return "bg-green-500";
    if (file.status === "error") return "bg-red-500";
    return "bg-blue-500";
  };

  return (
    <div className="p-4 bg-white rounded-xl shadow-md flex items-center space-x-4 border">
      {/* File Icon */}
      <div className={`w-10 h-10 flex items-center justify-center rounded-full ${
        file.status === "error" ? "bg-red-100 text-red-500" : "bg-purple-100 text-purple-500"
      }`}>
        📂
      </div>

      {/* File Info */}
      <div className="flex-1">
        <p className="text-gray-800 font-medium">{file.name}</p>
        {file.status === "error" ? (
          <p className="text-red-500 text-sm">Upload failed! Please try again.</p>
        ) : (
          <p className="text-gray-500 text-sm">{file.size} {file.progress < 100 ? `(${file.progress}%)` : "Upload Successful!"}</p>
        )}
        {/* Progress Bar */}
        <div className="w-full bg-gray-200 rounded-full h-2 mt-2">
          <div className={`h-2 rounded-full ${getProgressColor()}`} style={{ width: `${file.progress}%` }}></div>
        </div>
      </div>

      {/* Status Icons */}
      {file.progress === 100 ? (
        <CheckCircleIcon className="h-6 w-6 text-green-500" />
      ) : file.status === "error" ? (
        <ArrowPathIcon className="h-6 w-6 text-blue-500 cursor-pointer" />
      ) : (
        <TrashIcon className="h-6 w-6 text-gray-500 cursor-pointer" />
      )}
    </div>
  );
}

export default UploadItem;
