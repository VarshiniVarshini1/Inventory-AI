import React, { useState } from "react";
import { apiPost } from "../api/api";

export default function AgentChat() {
  const [msg, setMsg] = useState("");
  const [resp, setResp] = useState("");

  async function ask() {
    const data = await apiPost("/agent", { query: msg });
    setResp(data.response);
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Agent Chat</h1>

      <textarea
        placeholder="Ask something..."
        onChange={e => setMsg(e.target.value)}
        style={{ width: "300px", height: "100px" }}
      />

      <br />
      <button onClick={ask}>Send</button>

      <div style={{
        border: "1px solid gray",
        marginTop: "20px",
        padding: "10px"
      }}>
        {resp}
      </div>
    </div>
  );
}
