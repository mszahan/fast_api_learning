const carsLoader = async () => {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/cars?limit=30`);
  if (!res.ok) {
    throw new Error("Failed to fetch cars");
  }
  const response = await res.json();
  return response["cars"];
};

export default carsLoader;
