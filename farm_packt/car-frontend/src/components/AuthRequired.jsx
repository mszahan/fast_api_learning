import { Outlet, Navigate } from "react-router";
import { useAuth } from "../hooks/useAuth";

const AuthRequired = () => {
  const { jwt } = useAuth();

  return (
    <div>
      <h1>Auth Required</h1>
      {jwt ? <Outlet /> : <Navigate to="/login" />}
    </div>
  );
};

export default AuthRequired;
