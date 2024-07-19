import React from "react";
import ChartComponent from "../components/ChartComponent";

const HomePage = () => {
  return (
    <div className="container m-auto max-w-2xl py-24">
      <h1 className="text-3xl text-left font-semibold mb-6">Home Page</h1>
      <h2 className="text-3xl text-center font-semibold mb-6">
        View your Financial data
      </h2>
      <ChartComponent />
    </div>
  );
};

export default HomePage;
