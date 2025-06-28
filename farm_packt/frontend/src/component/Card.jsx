const Card = ({ car: { name, year, model, price } }) => {
  return (
    <div className="bg-slate-300 rounded p-4 m-4 shadow-lg">
      <h1 className="text-2xl">{name}</h1>
      <p className="text-sm">
        {year} - {model}
      </p>
      <p className="text-lg"> {price} </p>
    </div>
  );
};

export default Card;
