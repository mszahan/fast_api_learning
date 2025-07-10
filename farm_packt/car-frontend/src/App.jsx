import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router";
import Home from "./pages/Home.jsx";
import Car from "./pages/Car.jsx";
import NewCar from "./pages/NewCar.jsx";
import NotFound from "./pages/NotFound.jsx";
import SingleCar from "./pages/SingleCar.jsx";
import Login from "./pages/Login.jsx";
import NavBar from "./pages/NavBar.jsx";

function App() {
  return (
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route index element={<Home />} />
        <Route path="cars" element={<Car />} />
        <Route path="login" element={<Login />} />
        <Route path="new-car" element={<NewCar />} />
        <Route path="cars/:id" element={<SingleCar />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
