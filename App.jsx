import { useState } from "react";
import Login from "./pages/Login";
import Chat from "./pages/Chat";

export default function App() {
  const [token, setToken] = useState(null);

  if (!token) {
    return <Login aoLogar={setToken} />;
  }
  return <Chat token={token} />;
}
