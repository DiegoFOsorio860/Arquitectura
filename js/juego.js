function checkAnswer(button) {
    const selectedAnswer = button.textContent.trim();
    const feedback = button.parentElement.querySelector('.feedback');
    const correctAnswer = 'París'; // Respuesta correcta

    if (selectedAnswer === correctAnswer) {
        feedback.style.color = 'green';
        feedback.textContent = '¡Respuesta correcta!';
    } else {
        feedback.style.color = 'red';
        feedback.textContent = 'Respuesta incorrecta. Intenta de nuevo.';
    }

    feedback.style.display = 'block';
}

