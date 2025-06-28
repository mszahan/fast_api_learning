import { useState, useEffect } from "react";

const Users = () => {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    fetUsers();
  }, []);

  const fetUsers = () => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((data) => setUsers(data));
  };

  return (
    <div className="users">
      <h2>List of the users</h2>

      <div className="grid grid-cols-3 gap-4">
        <ol>
          {users.map((user) => (
            <li key={user.id}>{user.name}</li>
          ))}
        </ol>
      </div>
    </div>
  );
};

export default Users;
