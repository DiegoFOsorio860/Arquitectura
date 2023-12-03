from flask import Flask, render_template, render_template_string
import pandas as pd
from openpyxl import load_workbook

app = Flask(__name__)

datos= pd.read_excel('02122023 Arquitectura Curricular - Proyecto de Formación.xlsx', sheet_name='TIME')

@app.route('/')
def header():
    with open('templates/header.html', 'r') as header_file:
        header_html = header_file.read()

    with open('templates/introduccion.html', 'r') as intro_file:
        intro_html = intro_file.read()

    # Debes retornar algo aquí, como el encabezado y la introducción
    return render_template('header.html', header=header_html, intro=intro_html)

@app.route('/estructura')
def mostrar_estructura():
    # Lee el contenido de estructura.html
    with open('templates/estructura.html', 'r') as estructura_file:
        estructura_html = estructura_file.read()

    # Suponiendo que 'datos' es un DataFrame que contiene la información necesaria
    valor1 = datos.iloc[245,2]  # Reemplaza con los índices correspondientes
    valor2 = datos.iloc[245,3]  # Reemplaza con los índices correspondientes
    valor2 = round(valor2, 2)*100  # Redondear a 2 decimales
    valor3 = datos.iloc[245,4]  # Reemplaza con los índices correspondientes
    valor4 = datos.iloc[245,5]  # Reemplaza con los índices correspondientes
    valor4 = round(valor4, 2)*100  # Redondear a 2 decimales
    valor5 = datos.iloc[245,6]  # Reemplaza con los índices correspondientes
    valor6 = datos.iloc[194,2]  # Reemplaza con los índices correspondientes
    valor7 = datos.iloc[194,3]  # Reemplaza con los índices correspondientes
    valor7 = round(valor7,2)*100
    valor8 = datos.iloc[194,4]  # Reemplaza con los índices correspondientes
    valor9 = datos.iloc[194,5]  # Reemplaza con los índices correspondientes
    valor9 = round(valor9,2)*100
    valor10 = datos.iloc[223,2]  # Reemplaza con los índices correspondientes
    valor11 = datos.iloc[223,3]  # Reemplaza con los índices correspondientes
    valor11 = round(valor11,2)*100
    valor12 = datos.iloc[223,4]  # Reemplaza con los índices correspondientes
    valor13 = datos.iloc[223,5]  # Reemplaza con los índices correspondientes
    valor13 = round(valor13,2)*100
    # Renderizar la plantilla con los valores extraídos y el contenido de la estructuraaa
    return render_template('estructura.html', valor1=valor1, valor2=valor2, valor3=valor3, 
                           valor4=valor4,valor5=valor5, valor6=valor6, 
                           valor7 = valor7, valor8 = valor8, valor9 = valor9, 
                           valor10 = valor10, valor11 = valor11, valor12=valor12, valor13=valor13, estructura=estructura_html)

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
    app.run(debug=True, host='0.0.0.0', port=5001)