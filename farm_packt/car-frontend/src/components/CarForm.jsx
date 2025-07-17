import { useForm } from "react-hook-form";
import z from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useNavigate } from "react-router";
import { useAuth } from "../hooks/useAuth";
import InputField from "./InputField";

const schema = z.object({
  brand: z
    .string()
    .min(2, "Brand must contain at leas two letters")
    .max(20, "Brand cannot exceed 20 character"),

  make: z
    .string()
    .min(1, "Make must contain at least one letter")
    .max(20, "Make cannot exceed 20 characters"),
  year: z.coerce
    .number()
    .gte(1950, "Should not be earlier than 1950")
    .lte(new Date().getFullYear(), "Should not be later than the current year"),
  price: z.coerce
    .number()
    .gte(100, "Price should be at least 100")
    .lte(1000000, "Price should not exceed 1,000,000"),
  km: z.coerce
    .number()
    .gte(0, "Kilometers should be at least 0")
    .lte(500000, "Kilometers should not exceed 5,00,000"),
  cm3: z.coerce
    .number()
    .gte(0, "Engine capacity should be at least 0")
    .lte(5000, "Engine capacity should not exceed 5,000"),
  picture: z
    .any()
    .refine((file) => file[0] && file[0].type.startsWith("image/"), {
      message: "Please upload a valid image file",
    })
    .refine((file) => file[0] && file[0].size <= 1024 * 1024, {
      message: "Image size should not exceed 1MB",
    }),
});

const CarForm = () => {
  const navigate = useNavigate();
  const { jwt, setMessage } = useAuth();
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm({
    resolver: zodResolver(schema),
    mode: "all",
  });

  let formArray = [
    {
      name: "brand",
      type: "text",
      error: errors.brand,
    },
    {
      name: "make",
      type: "text",
      error: errors.make,
    },
    {
      name: "year",
      type: "number",
      error: errors.year,
    },
    {
      name: "price",
      type: "number",
      error: errors.price,
    },
    {
      name: "km",
      type: "number",
      error: errors.km,
    },
    {
      name: "cm3",
      type: "number",
      error: errors.cm3,
    },
    {
      name: "picture",
      type: "file",
      error: errors.picture,
    },
  ];

  const onSubmit = async (data) => {
    const formData = new FormData();
    formArray.forEach((field) => {
      if (field == "picture") {
        formData.append(field, data[field][0]);
      } else {
        formData.append(field.name, data[field.name]);
      }
    });

    const result = await fetch(`${import.meta.env.VITE_API_URL}/cars`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${jwt}`,
      },
      body: formData,
    });

    const json = await result.json();
    if (result.ok) {
      navigate("/cars");
    } else if (json.detail) {
      setMessage(JSON.stringify(json));
      navigate("/");
    }
  };

  return (
    <div className="flex items-center justify-center">
      <div className="w-full max-w-xs">
        <form
          className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
          encType="multipart/form-data"
          onSubmit={handleSubmit(onSubmit)}
        >
          <h2 className="text-center text-2xl font-bold mb-6">
            Insert new car data
          </h2>

          {formArray.map((item, index) => (
            <InputField
              key={index}
              props={{
                name: item.name,
                type: item.type,
                error: item.error,
                ...register(item.name),
              }}
            />
          ))}
          <div className="flex items-center justify-between">
            <button
              className="bg-gray-900 hover:bg-gray-700 text-white w-full font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="submit"
              disabled={isSubmitting}
            >
              {isSubmitting ? "Saving..." : "Save"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CarForm;
