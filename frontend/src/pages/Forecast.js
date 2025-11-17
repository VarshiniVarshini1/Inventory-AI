import React, { useState } from "react";
import { apiGet } from "../api/api";
import Chart from "../components/Chart";

export default function Forecast() {
  const [sku, setSku] = useState("");
  const [data, setData] = useState(null);

  async function fetchForecast() {
    const res = await apiGet(`/forecast/${sku}`);
    setData(res.forecast);
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Forecast</h1>

      <input placeholder="SKU"
        onChange={e => setSku(e.target.value)}
      />

      <button onClick={fetchForecast}>Forecast</button>

      {data && <Chart data={data} />}
    </div>
  );
}
