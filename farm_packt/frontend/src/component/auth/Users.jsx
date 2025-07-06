import { useEffect, useState } from "react";
import { useAuth } from "./useAuth";

const Users = () => {
  const { jwt, logout } = useAuth();
  const [users, setUsers] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      const response = await fetch("http://localhost:8000/users/list", {
        headers: {
          Authorization: `Bearer ${jwt}`,
        },
      });
      //   console.log(jwt);
      const data = await response.json();
      if (!response.ok) {
        setError(data.detail);
      }
      setUsers(data.users);
    };
    if (jwt) {
      fetchUser();
    }
  }, [jwt]);

  if (!jwt) return <div>Please login to see user list</div>;

  return (
    <div>
      {users ? (
        <div className="flex flex-col">
          <h1>The list of users</h1>
          <ol>
            {users.map((user) => (
              <li key={user.id}> {user.username} </li>
            ))}
          </ol>
          <button onClick={logout} className="bg-blue-500 text-white rounded">
            Logout
          </button>
        </div>
      ) : (
        <p>{error}</p>
      )}
    </div>
  );
};

export default Users;
