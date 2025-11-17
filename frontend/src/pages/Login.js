import React, { useState } from "react";
import { apiPost } from "../api/api";

export default function Login({ setLoggedIn }) {
  const [username, setUser] = useState("");
  const [password, setPass] = useState("");

  async function login() {
    const res = await apiPost("/auth/login", { username, password });
    if (res.access_token) {
      setLoggedIn(true);
    }
  }

  return (
    <div style={{ padding: "50px", textAlign: "center" }}>
      <h1>Login</h1>

      <input placeholder="Username"
        onChange={e => setUser(e.target.value)}
        style={{ padding: "10px", margin: "10px" }}
      />

      <input placeholder="Password" type="password"
        onChange={e => setPass(e.target.value)}
        style={{ padding: "10px", margin: "10px" }}
      />

      <button onClick={login}
        style={{
          padding: "10px 20px",
          marginTop: "20px",
          cursor: "pointer"
        }}
      >
        Login
      </button>
    </div>
  );
}
