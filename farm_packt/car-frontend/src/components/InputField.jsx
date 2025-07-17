const InputField = ({ props }) => {
  const { name, type, error } = props;
  return (
    <div className="mb-4">
      <label htmlFor={name} className="block text-gray-700 text-sm mb-2">
        {name}
      </label>
      <input
        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadowoutline"
        id={name}
        name={name}
        type={type}
        placeholder={name}
        {...props}
      />
      {error && <p className="text-red-500 text-xs italic">{error.message}</p>}
    </div>
  );
};

export default InputField;
