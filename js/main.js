// main.js
document.addEventListener("DOMContentLoaded", function () {
    const fase1 = document.getElementById("fase1");
    const proyecto1 = document.getElementById("proyecto1");
    
    fase1.addEventListener("mouseover", function () {
        // Tu lógica aquí cuando se pasa el ratón sobre Fase 1
        console.log("Pasaste el ratón sobre Fase 1");
        // Puedes agregar acciones que se desencadenen al pasar el ratón sobre Fase 1
        // Por ejemplo, cambiar el color del texto, mostrar un mensaje, etc.
    });

    proyecto1.addEventListener("mouseover", function () {
        // Tu lógica aquí cuando se pasa el ratón sobre Objetivo Proyecto 1
        console.log("Pasaste el ratón sobre Objetivo Proyecto 1");
    });

    // Otros eventos y lógica para otros elementos si es necesario...
});
