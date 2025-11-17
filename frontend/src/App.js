import React, { useState } from "react";
import Login from "./pages/Login";
import Sidebar from "./components/Sidebar";
import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import Inventory from "./pages/Inventory";
import Suppliers from "./pages/Suppliers";
import Forecast from "./pages/Forecast";
import AgentChat from "./pages/AgentChat";

export default function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [page, setPage] = useState("Dashboard");

  if (!loggedIn) return <Login setLoggedIn={setLoggedIn} />;

  return (
    <div style={{ display: "flex" }}>
      <Sidebar setPage={setPage} />
      <div style={{ flex: 1 }}>
        <Navbar />

        {page === "Dashboard" && <Dashboard />}
        {page === "Inventory" && <Inventory />}
        {page === "Suppliers" && <Suppliers />}
        {page === "Forecast" && <Forecast />}
        {page === "AI Agent" && <AgentChat />}
      </div>
    </div>
  );
}
