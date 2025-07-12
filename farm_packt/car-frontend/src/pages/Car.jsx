import { useLoaderData } from "react-router";
import CarCard from "../components/CarCard";

const Car = () => {
  const cars = useLoaderData();
  return (
    <div>
      <h1 className="text-3xl font-bold">Available cars</h1>
      <div className="md:grid md:grid-cols-3 sm:grid sm:grid-cols-2 gap-5">
        {cars.map((car) => (
          <CarCard key={car.id} car={car} />
        ))}
      </div>
    </div>
  );
};

export default Car;
