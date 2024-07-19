import { useState, useEffect } from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import api from "../api";
import { toast } from "react-toastify";
import Spinner from "./Spinner";

const ChartComponent = () => {
  const [chartData, setChartData] = useState(null);
  ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
  );

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get("/api/generate_chart/");
        setChartData(JSON.parse(response.data.chart_json));
      } catch (error) {
        toast.error("Failed to fetch chart data");
      }
    };

    fetchData();
  }, []);

  return (
    <div className="lg:h-96 md:h-50">
      {chartData ? (
        <Bar data={chartData}
          options={{
            maintainAspectRatio: true,
            responsive: true,
            scales: {
              y: {
                beginAtZero: true,
                title: {
                  display: true,
                  text: "Amount ($)",
                },
              },
              x: {
                title: {
                  display: true,
                  text: "Category",
                },
              },
            },
          }}
        />
      ) : (
        <div>
          <Spinner />
        </div>
      )}
    </div>
  );
};

export default ChartComponent;
