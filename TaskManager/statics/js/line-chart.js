const lineChartDiv = document.getElementById('task-line-chart');

// Fetch data and update the line chart UI
// Example:
const taskProgressData = [
    { date: '2023-08-01', completed: 5, pending: 3 },
    { date: '2023-08-02', completed: 7, pending: 1 },
    // ... more data ...
];

// Extract labels and datasets from the data
const labels = taskProgressData.map(entry => entry.date);
const completedData = taskProgressData.map(entry => entry.completed);
const pendingData = taskProgressData.map(entry => entry.pending);

// Create a line chart using Chart.js
const lineChart = new Chart(lineChartDiv, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'Completed Tasks',
                data: completedData,
                borderColor: 'green',
                fill: false,
            },
            {
                label: 'Pending Tasks',
                data: pendingData,
                borderColor: 'red',
                fill: false,
            },
        ],
    },
});
