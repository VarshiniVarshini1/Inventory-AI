import React, { useEffect, useState } from "react";
import { apiGet, apiPost } from "../api/api";

export default function Inventory() {
  const [items, setItems] = useState([]);

  async function loadData() {
    const res = await apiGet("/inventory");
    setItems(res);
  }

  async function recalc() {
    await apiPost("/inventory/recalculate", {});
    loadData();
  }

  useEffect(() => {
    loadData();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Inventory</h1>
      <button onClick={recalc}>Recalculate Levels</button>

      <table border="1" cellPadding="10" style={{ marginTop: "20px" }}>
        <thead>
          <tr>
            <th>SKU</th>
            <th>Name</th>
            <th>Qty</th>
            <th>Reorder</th>
            <th>Safety</th>
          </tr>
        </thead>
        <tbody>
          {items.map(i => (
            <tr key={i.id}>
              <td>{i.sku}</td>
              <td>{i.product_name}</td>
              <td>{i.quantity}</td>
              <td>{i.reorder_level}</td>
              <td>{i.safety_stock}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
