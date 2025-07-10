import { NavLink } from "react-router";

const NavBar = () => {
  return (
    <div className="bg-slate-700 p-2 mb-2">
      <header className="p-2 w-full">
        <nav className="flex flex-row gap-5 text-xl text-white">
          <NavLink to="/">Home</NavLink>
          <NavLink to="/cars">Cars</NavLink>
          <NavLink to="/new-car">New Car</NavLink>
          <NavLink to="/login">Login</NavLink>
        </nav>
      </header>
    </div>
  );
};

export default NavBar;
