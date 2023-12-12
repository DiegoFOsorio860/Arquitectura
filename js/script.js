function checkAnswer() {
  const answer = document.querySelector('input[name="respuesta"]:checked');
  const result = document.getElementById('resultado');

  if (answer) {
    if (answer.value === 'Aguas subterráneas') {
      result.textContent = '¡Respuesta correcta! Las aguas subterráneas son la principal fuente de agua potable para la mayoría de las personas en el mundo.';
    } else {
      result.textContent = 'Respuesta incorrecta. Las aguas subterráneas son la principal fuente de agua potable para la mayoría de las personas en el mundo.';
    }
    result.style.display = 'block'; // Mostrar la respuesta
  } else {
    result.textContent = 'Por favor, selecciona una respuesta.';
  }
}
