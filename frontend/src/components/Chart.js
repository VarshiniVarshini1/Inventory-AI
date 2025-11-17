import React from "react";

export default function Chart({ data }) {
  return (
    <div>
      <h3>Forecast Chart</h3>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
