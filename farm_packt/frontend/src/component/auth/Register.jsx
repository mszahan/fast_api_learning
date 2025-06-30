import { useState } from "react";
import { useAuth } from "./useAuth";

const Register = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { register } = useAuth();

  const handleSubmit = (e) => {
    e.preventDefault();
    register(username, password);
    setUsername("");
    setPassword("");
  };

  return (
    <div className="m-4 p-5 border-2">
      <form onSubmit={handleSubmit} className="grid grid-rows-3 gap-2">
        <input
          type="text"
          placeholder="username"
          className="p-2"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="password"
          className="p-2"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit" className="bg-blue-500 text-white rounded">
          Register
        </button>
      </form>
    </div>
  );
};

export default Register;
