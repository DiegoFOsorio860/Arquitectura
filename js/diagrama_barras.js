// Datos para el gráfico de barras
const dataBar = {
    labels: ['A', 'B', 'C', 'D'],
    datasets: [{
      label: 'Ejemplo de Datos para Barras',
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
  
  // Configuración para el gráfico de barras
  const configBar = {
    type: 'bar',
    data: dataBar,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  };
  
  // Dibujar gráfico de barras
  const ctxBar = document.getElementById('barras').getContext('2d');
  new Chart(ctxBar, configBar);
  
  // Datos para el gráfico de pastel
  const dataPie = {
    labels: ['Red', 'Blue', 'Yellow', 'Green'],
    datasets: [{
      label: 'Ejemplo de Datos para Pastel',
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
  
  // Configuración para el gráfico de pastel
  const configPie = {
    type: 'pie',
    data: dataPie
  };
  
  // Dibujar gráfico de pastel
  const ctxPie = document.getElementById('pastel').getContext('2d');
  new Chart(ctxPie, configPie);
  