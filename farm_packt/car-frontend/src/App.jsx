import "./App.css";
import {
  createBrowserRouter,
  Route,
  createRoutesFromElements,
  RouterProvider,
} from "react-router";

import RootLayout from "./layout/RootLayout.jsx";

import Home from "./pages/Home.jsx";
import Car from "./pages/Car.jsx";
import NewCar from "./pages/NewCar.jsx";
import NotFound from "./pages/NotFound.jsx";
import SingleCar from "./pages/SingleCar.jsx";
import carsLoader from "./components/carsLoader.js";
import Login from "./pages/Login.jsx";
import { AuthProvider } from "./context/AuthContext.jsx";
import AuthRequired from "./components/AuthRequired.jsx";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>
      <Route index element={<Home />} />
      <Route path="cars" element={<Car />} loader={carsLoader} />
      <Route path="login" element={<Login />} />
      {/* <Route element={<AuthRequired />}>
        <Route path="new-car" element={<NewCar />} />
      </Route> */}
      <Route path="new-car" element={<NewCar />} />
      <Route path="cars/:id" element={<SingleCar />} />
      <Route path="*" element={<NotFound />} />
    </Route>
  )
);

export default function App() {
  return (
    <AuthProvider>
      <RouterProvider router={router} />;
    </AuthProvider>
  );
}
