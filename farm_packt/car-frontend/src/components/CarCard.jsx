const CarCard = ({ car }) => {
  return (
    <div
      className="flex flex-col p-3 text-black bg-white 
    rounded-xl overflow-hidden shadow-md hover:scale-105 
    transition-transform duration-200"
    >
      <div>
        {car.brand} {car.make} {car.year} {car.cm3} {car.price} {car.km}
      </div>
      <img
        src={car.picture_url}
        alt={car.make}
        className="w-full h-64 object-cover object-center"
      />
    </div>
  );
};

export default CarCard;
