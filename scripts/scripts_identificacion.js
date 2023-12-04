// Obtener el elemento select
var selectElement = document.getElementById("tipoIdentificacion");

// Asociar el evento change a la función changeColor
selectElement.addEventListener("change", function() {
  changeColor(this);
});

function changeColor(selectElement) {
  var selectedOption = selectElement.options[selectElement.selectedIndex];
  selectedOption.style.backgroundColor = "#00FF00"; // Cambiar a tu color deseado
}

