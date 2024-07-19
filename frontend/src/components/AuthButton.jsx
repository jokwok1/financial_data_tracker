import { NavLink, useNavigate, useLocation } from "react-router-dom";
import { useState, useEffect } from "react";
import { ACCESS_TOKEN } from "../constants";

const AuthButton = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    setIsAuthenticated(!!token);
  }, [location]);

  function handleLogout() {
    localStorage.clear();
    setIsAuthenticated(false);
    navigate("/login");
  }

  return (
    <>
      {isAuthenticated ? (
        <>
          <span className="text-white py-2">Welome! :</span>
          <button
            onClick={handleLogout}
            className="text-white hover:bg-gray-900 hover:text-white rounded-md px-1 py-2"
          >
            Logout
          </button>
        </>
      ) : (
        <>
          <NavLink
            to="/login"
            className="text-white hover:bg-gray-900 hover:text-white rounded-md px-3 py-2"
          >
            Login
          </NavLink>
          <NavLink
            to="/register"
            className="text-white hover:bg-gray-900 hover:text-white rounded-md px-3 py-2"
          >
            Register
          </NavLink>
        </>
      )}
    </>
  );
};

export default AuthButton;
