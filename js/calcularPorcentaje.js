    // Función para calcular el porcentaje acumulado
    function calcularPorcentaje() {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');

        let totalChecked = 0;
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                totalChecked++;
            }
        });

        const porcentajeAcumulado = (totalChecked / checkboxes.length) * 100;

        // Actualizar el valor en el lugar deseado, por ejemplo, una celda en tu tabla
        document.getElementById('porcentajeAcumulado').innerText = `Porcentaje Acumulado: ${porcentajeAcumulado}%`;
    }