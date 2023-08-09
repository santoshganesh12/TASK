const taskChartDiv = document.getElementById('task-chart');
const employeeCountDiv = document.getElementById('employee-count');

// Fetch data and update the dashboard UI
// You can use libraries like Chart.js for charts

// Example:
const taskData = [
    { label: 'Pending', value: 5 },
    { label: 'Completed', value: 3 },
];

// Create a pie chart using Chart.js
const taskChart = new Chart(taskChartDiv, {
    type: 'pie',
    data: {
        labels: taskData.map(item => item.label),
        datasets: [{
            data: taskData.map(item => item.value),
            backgroundColor: ['red', 'green'],
        }],
    },
});

// Fetch employee count and update UI
// Example:
const employeeCount = 10;
employeeCountDiv.textContent = `Total Employees: ${employeeCount}`;
