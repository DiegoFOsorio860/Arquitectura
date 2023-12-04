function changeColor(selectElement) {
    var selectedValue = selectElement.value;
    var backgroundColor = "";
    var textColor = "";
    var fontWeight = "";

    switch (selectedValue) {
      case "CC":
        backgroundColor = "#00FF00";
        textColor = "#0000FF"; // Color del texto en selección CC
        fontWeight = "bold"; // Texto en negrita en selección CC
        break;
      case "TI":
        backgroundColor = "#00FF00";
        textColor = "#0000FF"; // Color del texto en selección CC
        fontWeight = "bold"; // Texto en negrita en selección CC
        break;
      case "Cédula de Extranjería":
        backgroundColor = "#00FF00";
        textColor = "#0000FF"; // Color del texto en selección CC
        fontWeight = "bold"; // Texto en negrita en selección CC
        break;
      default:
        backgroundColor = "#00FF00";
        textColor = "#0000FF"; // Color del texto en selección CC
        fontWeight = "bold"; // Texto en negrita en selección CC
        break;
    }

    selectElement.style.backgroundColor = backgroundColor;
    selectElement.style.color = textColor;
    selectElement.style.fontWeight = fontWeight;
    }