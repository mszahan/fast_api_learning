import { Outlet, NavLink } from "react-router";
import { useAuth } from "../hooks/useAuth";

const RootLayout = () => {
  const { user, message, logout } = useAuth();

  return (
    <div>
      <header className="p-2 w-full bg-slate-700 text-white">
        <nav className="flex flex-row justify-between mx-5">
          <div className="flex flex-row space-x-3 gap-4">
            <NavLink to="/">Home</NavLink>
            <NavLink to="/cars">Cars</NavLink>
            {user && <NavLink to="/new-car">New Car</NavLink>}
          </div>
          <div>
            {user ? (
              <>
                <p>{user}</p>
                <button onClick={logout}>Logout</button>
              </>
            ) : (
              <NavLink to="/login">Login</NavLink>
            )}
          </div>
        </nav>
      </header>
      <main className="p-8 flex flex-col flex-1 bg-white ">
        <Outlet />
      </main>
    </div>
  );
};
export default RootLayout;
