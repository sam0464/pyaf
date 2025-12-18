
import { useState } from "react";
import axios from "axios";

export default function App() {
  const [msg, setMsg] = useState("");
  const [reply, setReply] = useState("");

  const send = async () => {
    const res = await axios.post("http://localhost:8000/chat", { message: msg });
    setReply(res.data.response);
  };

  return (
    <div style={{ padding: 40, fontFamily: "sans-serif" }}>
      <h1>🌦️ SanchAI Weather Assistant</h1>
      <input
        value={msg}
        onChange={(e) => setMsg(e.target.value)}
        placeholder="Ask weather of any city..."
        style={{ width: "70%", padding: 10 }}
      />
      <button onClick={send} style={{ marginLeft: 10, padding: 10 }}>
        Send
      </button>
      <p style={{ marginTop: 20 }}>{reply}</p>
    </div>
  );
}
