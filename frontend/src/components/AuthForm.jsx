import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import { toast } from "react-toastify";
import Spinner from "./Spinner";

const AuthForm = ({ route, method }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const name = method === "login" ? "Login" : "Register";

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault(); //prevent default behavior of reloading page
    try {
      const res = await api.post(route, { username, password });
      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
        navigate("/");
      } else {
        localStorage.clear();
        toast.success("Successfully registered! Please log in.");
        navigate("/login");
      }
    } catch (error) {
      if (error.response && error.response.status === 401) {
        toast.error("Invalid username or password. Please try again.");
      } else {
        alert(error); // Handle other errors
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="container m-auto max-w-2xl py-24">
      <h1 className="text-3xl text-center font-semibold mb-6">{name}</h1>
      <input
        className="border rounded w-full py-2 px-3"
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        className="border rounded w-full py-2 px-3"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      {loading && <Spinner />}
      <button
        className="bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-full w-full focus:outline-none focus:shadow-outline"
        type="submit"
      >
        {name}
      </button>
    </form>
  );
};

export default AuthForm;
