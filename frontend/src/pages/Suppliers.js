import React, { useEffect, useState } from "react";
import { apiGet, apiPost } from "../api/api";

export default function Suppliers() {
  const [suppliers, setSuppliers] = useState([]);

  async function load() {
    setSuppliers(await apiGet("/supplier"));
  }

  async function rate() {
    await apiPost("/supplier/rate", {});
    load();
  }

  useEffect(() => {
    load();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Suppliers</h1>
      <button onClick={rate}>Recalculate Ratings</button>

      <table border="1" cellPadding="10" style={{ marginTop: "20px" }}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Rating</th>
            <th>Cost</th>
            <th>Speed</th>
          </tr>
        </thead>
        <tbody>
          {suppliers.map(s => (
            <tr key={s.id}>
              <td>{s.name}</td>
              <td>{s.rating}</td>
              <td>{s.cost_score}</td>
              <td>{s.delivery_speed}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
