import Link from "next/link";

const NotFound = () => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1>Page not found </h1>
      <p>
        Take a look at
        <Link href="/cars" className="text-blue-500">
          our cars list
        </Link>
      </p>
    </div>
  );
};

export default NotFound;
