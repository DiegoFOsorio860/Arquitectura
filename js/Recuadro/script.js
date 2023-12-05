// Contenido dinámico para la cita
const cita = {
    frase: "El agua es el recurso más esencial para la vida.",
    autor: "Jacques-Yves Cousteau"
};

// Actualización del contenido en el recuadro
document.getElementById("frase").innerText = cita.frase;
document.getElementById("autor").innerText = `- ${cita.autor}`;
