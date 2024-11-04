// Get data for the chart from hidden elements
const labels = JSON.parse(document.getElementById('chartLabels').textContent);
const dataPoints = JSON.parse(document.getElementById('chartDataPoints').textContent);
const symbol = document.getElementById('chartSymbol').textContent;

// Configure Chart.js
const ctx = document.getElementById('priceChart').getContext('2d');
const priceChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: `${symbol} Price (USD)`,
            data: dataPoints,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 2,
            fill: true,
        }]
    },
    options: {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Date'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Price (USD)'
                }
            }
        },
        responsive: true,
    }
});
