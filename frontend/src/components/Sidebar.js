import React from "react";

export default function Sidebar({ setPage }) {
  const menu = [
    "Dashboard",
    "Inventory",
    "Suppliers",
    "Forecast",
    "AI Agent"
  ];

  return (
    <div style={{
      background: "#222",
      width: "200px",
      height: "100vh",
      color: "white",
      padding: "20px"
    }}>
      {menu.map(m => (
        <div
          key={m}
          style={{ margin: "20px 0", cursor: "pointer" }}
          onClick={() => setPage(m)}
        >
          {m}
        </div>
      ))}
    </div>
  );
}
