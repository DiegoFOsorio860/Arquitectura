// Aquí va tu código de Chart.js para generar los gráficos

document.addEventListener('DOMContentLoaded', function () {
    // Datos para el primer gráfico de barras
    const dataBar1 = {
        labels: ['A', 'B', 'C', 'D'],
        datasets: [{
            label: 'Ejemplo de Datos para Barras 1',
            data: [12, 19, 3, 5],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    };

    // Configuración para el primer gráfico de barras
    const configBar1 = {
        type: 'bar',
        data: dataBar1,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Formación Directa' // Título del gráfico de barras 1
                }
            }
        }
    };

    // Dibujar el primer gráfico de barras
    const ctxBar1 = document.getElementById('barras1').getContext('2d');
    new Chart(ctxBar1, configBar1);
});
