import { useState } from "react";
import { toast } from "react-toastify";
import Spinner from "../components/Spinner";
import api from "../api";

const UploadPage = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    setLoading(true);

    try {
      // create a Form Data object
      const formData = new FormData();
      formData.append("file", file);

      // Send post request
      const response = await api.post("/api/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      toast.success(response.data.message);
    } catch (error) {
      if (error.response && error.response.status === 500) {
        toast.error(
          "Invalid File Uploaded, ensure valid CSV file with correct fields"
        );
      } else {
        toast.error("An error occurred while uploading the file.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container m-auto max-w-2xl py-24">
      <h1 className="text-3xl text-center font-semibold mb-6">
        Upload CSV File
      </h1>
      <input
        type="file"
        onChange={handleFileChange}
        className="border rounded w-full py-2 px-3"
      />
      {loading && <Spinner />}
      <button
        onClick={handleUpload}
        disabled={!file || loading}
        className="bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-full w-full focus:outline-none focus:shadow-outline mt-4"
      >
        Upload
      </button>
    </div>
  );
};

export default UploadPage;
