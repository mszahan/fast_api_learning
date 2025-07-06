import { createContext, useEffect, useState } from "react";

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [jwt, setJwt] = useState(null);
  const [message, setMessage] = useState(null);

  useEffect(() => {
    const storedJwt = localStorage.getItem("jwt");

    if (storedJwt) {
      setJwt(storedJwt);
      fetch("http://localhost:8000/users/me", {
        headers: {
          Authorization: `Bearer ${storedJwt}`,
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.username) {
            setUser({ username: data.username });
            setMessage(`Welcome back ${data.username}`);
          }
        })
        .catch(() => {
          localStorage.removeItem("jwt");
        });
    }
  }, []);

  const register = async (username, password) => {
    try {
      const resposen = await fetch("http://localhost:8000/users/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
        }),
      });
      if (resposen.ok) {
        const data = await resposen.json();
        setMessage(`Registration successful: user ${data.username}`);
      } else {
        const data = await resposen.json();
        setMessage(`Registration failed: ${JSON.stringify(data)}`);
      }
    } catch (error) {
      setMessage(`Registration failed: ${JSON.stringify(error)}`);
    }
  };

  const logout = () => {
    setUser(null);
    setJwt("");
    localStorage.removeItem("jwt");
    setMessage("Logout successful");
  };

  const login = async (username, password) => {
    setJwt(null);
    const response = await fetch("http://localhost:8000/users/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });
    if (response.ok) {
      const data = await response.json();
      setJwt(data.token);
      localStorage.setItem("jwt", data.token);
      setUser({ username });
      setMessage(
        `login successful : token ${data.token.slice(
          0,
          10
        )}... user ${username}`
      );
    } else {
      const data = await response.json();
      setMessage("login failed" + data.detail);
      setUser({ username: null });
    }
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        jwt,
        register,
        login,
        logout,
        message,
        setMessage,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
