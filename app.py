from flask import Flask, render_template, render_template_string
import pandas as pd
from openpyxl import load_workbook

app = Flask(__name__)

@app.route('/')
def header():
    with open('templates/header.html', 'r') as header_file:
        header_html = header_file.read()

    with open('templates/introduccion.html', 'r') as intro_file:
        intro_html = intro_file.read()

    # Debes retornar algo aquí, como el encabezado y la introducción
    return render_template('header.html', header=header_html, intro=intro_html)

@app.route('/estructura')
def pagina_dos():
    # Lee el contenido de estructura.html
    with open('templates/estructura.html', 'r') as estructura_file:
        estructura_html = estructura_file.read()

    return render_template('estructura.html', estructura=estructura_html)

datos= pd.read_excel('30112023 Arquitectura Curricular - Proyecto de Formación.xlsx', sheet_name='TIME')
datos = datos.iloc[[1],[1]]

@app.route('/estructura')
def TimeFase1():
    # Extraer dos valores específicos de la hoja 'TIME'
    valor1 = datos.iloc[[1], [1]]  # Reemplaza 'fila' y 'columna' por los índices correspondientes
    valor2 = datos.iloc[[1], [4]]  # Otro valor que desees obtener

    # Renderizar la plantilla con los valores extraídos
    return render_template('templates/estructura.html', valor1=valor1, valor2=valor2)

@app.route('/fase1')
def fase1():
    # Lee el contenido de fase1.html
    with open('templates/fase1.html', 'r') as fase1_file:
        fase1_html = fase1_file.read()

    return render_template('fase1.html', fase1=fase1_html)

@app.route('/fase2')
def fase2():
    # Lee el contenido de fase2.html
    with open('templates/fase2.html', 'r') as fase2_file:
        fase2_html = fase2_file.read()

    return render_template('fase2.html', fase2=fase2_html)

@app.route('/fase3')
def fase3():
    # Lee el contenido de fase3.html
    with open('templates/fase3.html', 'r') as fase3_file:
        fase3_html = fase3_file.read()

    return render_template('fase3.html', fase3=fase3_html)

@app.route('/trimestre1')
def trimestre1():
    # Lee el contenido de trimestre1.html
    with open('templates/trimestre1.html', 'r') as trimestre1_file:
        trimestre1_html = trimestre1_file.read()

    return render_template('trimestre1.html', trimestre1=trimestre1_html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)

