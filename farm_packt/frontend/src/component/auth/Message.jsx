import { useAuth } from "./useAuth";

const Message = () => {
  const { message } = useAuth();

  return (
    <div className="p-2 my-2">
      <p> {message} </p>
    </div>
  );
};

export default Message;
