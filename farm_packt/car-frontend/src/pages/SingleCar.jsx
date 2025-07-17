import { useLoaderData } from "react-router";
import CarCard from "../components/CarCard";

const SingleCar = () => {
  const { car } = useLoaderData();
  return (
    <div>
      <CarCard car={car} />
    </div>
  );
};

export default SingleCar;
