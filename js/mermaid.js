document.addEventListener("DOMContentLoaded", function() {
    // Coordenadas de los bloques
    const block1 = document.getElementById("block1");
    const block2 = document.getElementById("block2");
    const block3 = document.getElementById("block3");
  
    // Crear un SVG para las flechas
    const arrows = document.getElementById("arrows");
  
    // Función para dibujar flechas
    function drawArrow(startX, startY, endX, endY) {
      const arrow = document.createElementNS("http://www.w3.org/2000/svg", "line");
      arrow.setAttribute("x1", startX);
      arrow.setAttribute("y1", startY);
      arrow.setAttribute("x2", endX);
      arrow.setAttribute("y2", endY);
      arrow.setAttribute("stroke", "black");
      arrow.setAttribute("marker-end", "url(#arrowhead)");
  
      arrows.appendChild(arrow);
    }
  
    // Dibujar flechas entre bloques
    drawArrow(block1.offsetLeft + block1.offsetWidth, block1.offsetTop + block1.offsetHeight / 2, block2.offsetLeft, block2.offsetTop + block2.offsetHeight / 2);
    drawArrow(block2.offsetLeft + block2.offsetWidth, block2.offsetTop + block2.offsetHeight / 2, block3.offsetLeft, block3.offsetTop + block3.offsetHeight / 2);
  });
  