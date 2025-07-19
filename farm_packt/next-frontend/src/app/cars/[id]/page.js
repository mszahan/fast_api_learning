const CarDetails = ({ params }) => {
  const { id } = params;

  return (
    <div>
      <h1>Car Details for ID: {id}</h1>
      {/* Additional car details can be displayed here */}
    </div>
  );
};

export default CarDetails;
