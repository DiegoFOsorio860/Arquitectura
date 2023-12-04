var numeroInput = document.getElementById("numero");

numeroInput.addEventListener("input", function() {
  var inputValue = this.value;
  var backgroundColor = "";

  // Define las condiciones para cambiar el color de fondo
  if (inputValue.length >= 0) {
    backgroundColor = "#00FF00"; // Color verde si la longitud del valor es mayor o igual a 2
  } else {
    backgroundColor = "#FFFFFF"; // Color blanco si la longitud del valor es menor a 2
  }

  this.style.backgroundColor = backgroundColor;
});
