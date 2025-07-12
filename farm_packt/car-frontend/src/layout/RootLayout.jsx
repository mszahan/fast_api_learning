import { Outlet, NavLink } from "react-router";
const RootLayout = () => {
  return (
    <div>
      <header className="p-2 w-full bg-slate-700 text-white">
        <nav className="flex flex-row justify-between">
          <div className="flex flex-row space-x-3 gap-4">
            <NavLink to="/">Home</NavLink> <NavLink to="/cars">Cars</NavLink>
            <NavLink to="/login">Login</NavLink>{" "}
            <NavLink to="/new-car">New Car</NavLink>
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
