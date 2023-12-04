from flask import Flask, render_template
import pandas as pd
from flask import Flask, render_template, request, redirect  # Importa la función 'redirect'
import subprocess
import csv
import numpy as np
import pickle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Cargar datos_TIME desde el archivo Excel
datos_TIME = pd.read_excel('02122023 Arquitectura Curricular - Proyecto de Formación.xlsx', sheet_name='TIME')
# Cargar datos_TIME desde el archivo Excel
datos_ARQUITECTURA = pd.read_excel('02122023 Arquitectura Curricular - Proyecto de Formación.xlsx', sheet_name='ARQUITECTURA')


@app.route('/')
def header():
    # Renderizar el encabezado y la introducción
    with open('templates/header.html', 'r') as header_file:
        header_html = header_file.read()

    with open('templates/introduccion.html', 'r') as intro_file:
        intro_html = intro_file.read()

    return render_template('header.html', header=header_html, intro=intro_html)

@app.route('/estructura')
def mostrar_estructura():
    # Leer el contenido de estructura.html
    with open('templates/estructura.html', 'r') as estructura_file:
        estructura_html = estructura_file.read()

    # Suponiendo que 'datos_TIME' es un DataFrame que contiene la información necesaria
    valor_TIME_T1_1 = datos_TIME.iloc[194,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_2 = datos_TIME.iloc[194,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_2 = round(valor_TIME_T1_2,2)*100
    valor_TIME_T1_3 = datos_TIME.iloc[194,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_4 = datos_TIME.iloc[194,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_4 = round(valor_TIME_T1_4,2)*100

    valor_TIME_T2_1 = datos_TIME.iloc[223,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T2_2 = datos_TIME.iloc[223,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T2_2 = round(valor_TIME_T2_2,2)*100
    valor_TIME_T2_3 = datos_TIME.iloc[223,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T2_4 = datos_TIME.iloc[223,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T2_4 = round(valor_TIME_T2_4,2)*100

    valor_TIME_F1_1 = datos_TIME.iloc[245,2]  # Reemplaza con los índices correspondientes
    valor_TIME_F1_2 = datos_TIME.iloc[245,3]  # Reemplaza con los índices correspondientes
    valor_TIME_F1_2 = round(valor_TIME_F1_2, 2)*100  # Redondear a 2 decimales
    valor_TIME_F1_3 = datos_TIME.iloc[245,4]  # Reemplaza con los índices correspondientes
    valor_TIME_F1_4 = datos_TIME.iloc[245,5]  # Reemplaza con los índices correspondientes
    valor_TIME_F1_4 = round(valor_TIME_F1_4, 2)*100  # Redondear a 2 decimales
    

    # Renderizar la plantilla con los valor_TIME_T1_es extraídos y el contenido de la estructuraaa
    return render_template('estructura.html', 
                           valor_TIME_T1_1=valor_TIME_T1_1, 
                           valor_TIME_T1_2=valor_TIME_T1_2, 
                           valor_TIME_T1_3=valor_TIME_T1_3, 
                           valor_TIME_T1_4=valor_TIME_T1_4,
                            
                           valor_TIME_T2_1=valor_TIME_T2_1, 
                           valor_TIME_T2_2=valor_TIME_T2_2, 
                           valor_TIME_T2_3=valor_TIME_T2_3, 
                           valor_TIME_T2_4=valor_TIME_T2_4,

                           valor_TIME_F1_1=valor_TIME_F1_1, 
                           valor_TIME_F1_2=valor_TIME_F1_2, 
                           valor_TIME_F1_3=valor_TIME_F1_3, 
                           valor_TIME_F1_4=valor_TIME_F1_4,
  
                           estructura=estructura_html)

@app.route('/fase1')
def fase1():
    """
    Muestra la información correspondiente a la fase 1.
    Lee el contenido de fase1.html y lo renderiza en la plantilla 'fase1.html'.
    """
    with open('templates/fase1.html', 'r') as fase1_file:
        fase1_html = fase1_file.read()

    return render_template('fase1.html', fase1=fase1_html)

@app.route('/fase2')
def fase2():
    """
    Muestra la información correspondiente a la fase 2.
    Lee el contenido de fase2.html y lo renderiza en la plantilla 'fase2.html'.
    """
    with open('templates/fase2.html', 'r') as fase2_file:
        fase2_html = fase2_file.read()

    return render_template('fase2.html', fase2=fase2_html)

@app.route('/fase3')
def fase3():
    """
    Muestra la información correspondiente a la fase 3.
    Lee el contenido de fase3.html y lo renderiza en la plantilla 'fase3.html'.
    """
    with open('templates/fase3.html', 'r') as fase3_file:
        fase3_html = fase3_file.read()

    return render_template('fase3.html', fase3=fase3_html)

@app.route('/trimestre1')
def trimestre1():
    """
    Muestra la información correspondiente al trimestre 1.
    Lee el contenido de trimestre1.html y lo renderiza en la plantilla 'trimestre1.html'.
    """
    with open('templates/trimestre1.html', 'r') as trimestre1_file:
        trimestre1_html = trimestre1_file.read()

         # Suponiendo que 'datos_TIME' es un DataFrame que contiene la información necesaria
    valor_TIME_T1_HIDRAULICA_1 = datos_TIME.iloc[187,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_HIDRAULICA_2 = datos_TIME.iloc[187,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_HIDRAULICA_2 = round(valor_TIME_T1_HIDRAULICA_2, 2)*100  # Redondear a 2 decimales
    valor_TIME_T1_HIDRAULICA_3 = datos_TIME.iloc[187,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_HIDRAULICA_4 = datos_TIME.iloc[187,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_HIDRAULICA_4 = round(valor_TIME_T1_HIDRAULICA_4, 2)*100  # Redondear a 2 decimales

    # Suponiendo que 'datos_TIME' es un DataFrame que contiene la información necesaria
    valor_TIME_T1_REC_MUESTRAS_1 = datos_TIME.iloc[188,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_REC_MUESTRAS_2 = datos_TIME.iloc[188,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_REC_MUESTRAS_2 = round(valor_TIME_T1_REC_MUESTRAS_2, 2)*100  # Redondear a 2 decimales
    valor_TIME_T1_REC_MUESTRAS_3 = datos_TIME.iloc[188,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_REC_MUESTRAS_4 = datos_TIME.iloc[188,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_REC_MUESTRAS_4 = round(valor_TIME_T1_REC_MUESTRAS_4, 2)*100  # Redondear a 2 decimales

        # Suponiendo que 'datos_TIME' es un DataFrame que contiene la información necesaria
    valor_TIME_T1_INGLES_1 = datos_TIME.iloc[189,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_INGLES_2 = datos_TIME.iloc[189,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_INGLES_2 = round(valor_TIME_T1_INGLES_2, 2)*100  # Redondear a 2 decimales
    valor_TIME_T1_INGLES_3 = datos_TIME.iloc[189,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_INGLES_4 = datos_TIME.iloc[189,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_INGLES_4 = round(valor_TIME_T1_INGLES_4, 2)*100  # Redondear a 2 decimales

            # Suponiendo que 'datos_TIME' es un DataFrame que contiene la información necesaria
    valor_TIME_T1_MATEMATICAS_1 = datos_TIME.iloc[190,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_MATEMATICAS_2 = datos_TIME.iloc[190,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_MATEMATICAS_2 = round(valor_TIME_T1_MATEMATICAS_2, 2)*100  # Redondear a 2 decimales
    valor_TIME_T1_MATEMATICAS_3 = datos_TIME.iloc[190,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_MATEMATICAS_4 = datos_TIME.iloc[190,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_MATEMATICAS_4 = round(valor_TIME_T1_MATEMATICAS_4, 2)*100  # Redondear a 2 decimales

                # Suponiendo que 'datos_TIME' es un DataFrame que contiene la información necesaria
    valor_TIME_T1_BIOLOGIA_1 = datos_TIME.iloc[191,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_BIOLOGIA_2 = (datos_TIME.iloc[191,3])*100  # Reemplaza con los índices correspondientes
    valor_TIME_T1_BIOLOGIA_2 = "{:.3}".format(valor_TIME_T1_BIOLOGIA_2)  # Redondear a 2 decimales
    valor_TIME_T1_BIOLOGIA_3 = datos_TIME.iloc[191,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_BIOLOGIA_4 = datos_TIME.iloc[191,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_BIOLOGIA_4 = round(valor_TIME_T1_BIOLOGIA_4, 2)*100  # Redondear a 2 decimales

                    # Suponiendo que 'datos_TIME' es un DataFrame que contiene la información necesaria
    valor_TIME_T1_COMUNICACION_1 = datos_TIME.iloc[192,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMUNICACION_2 = datos_TIME.iloc[192,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMUNICACION_2 = round(valor_TIME_T1_COMUNICACION_2, 2)*100  # Redondear a 2 decimales
    valor_TIME_T1_COMUNICACION_3 = datos_TIME.iloc[192,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMUNICACION_4 = datos_TIME.iloc[192,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMUNICACION_4 = round(valor_TIME_T1_COMUNICACION_4, 2)*100  # Redondear a 2 decimales

                        # Suponiendo que 'datos_TIME' es un DataFrame que contiene la información necesaria
    valor_TIME_T1_LOGISTICA_1 = datos_TIME.iloc[193,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_LOGISTICA_2 = datos_TIME.iloc[193,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_LOGISTICA_2 = round(valor_TIME_T1_LOGISTICA_2, 2)*100  # Redondear a 2 decimales
    valor_TIME_T1_LOGISTICA_3 = datos_TIME.iloc[193,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_LOGISTICA_4 = datos_TIME.iloc[193,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_LOGISTICA_4 = round(valor_TIME_T1_LOGISTICA_4, 2)*100  # Redondear a 2 decimales

    return render_template('trimestre1.html', 
                            valor_TIME_T1_HIDRAULICA_1=valor_TIME_T1_HIDRAULICA_1, 
                           valor_TIME_T1_HIDRAULICA_2= valor_TIME_T1_HIDRAULICA_2, 
                           valor_TIME_T1_HIDRAULICA_3= valor_TIME_T1_HIDRAULICA_3, 
                           valor_TIME_T1_HIDRAULICA_4= valor_TIME_T1_HIDRAULICA_4,

                           valor_TIME_T1_REC_MUESTRAS_1=valor_TIME_T1_REC_MUESTRAS_1, 
                           valor_TIME_T1_REC_MUESTRAS_2= valor_TIME_T1_REC_MUESTRAS_2, 
                           valor_TIME_T1_REC_MUESTRAS_3= valor_TIME_T1_REC_MUESTRAS_3, 
                           valor_TIME_T1_REC_MUESTRAS_4= valor_TIME_T1_REC_MUESTRAS_4,

                           valor_TIME_T1_INGLES_1= valor_TIME_T1_INGLES_1, 
                           valor_TIME_T1_INGLES_2= valor_TIME_T1_INGLES_2, 
                           valor_TIME_T1_INGLES_3= valor_TIME_T1_INGLES_3, 
                           valor_TIME_T1_INGLES_4= valor_TIME_T1_INGLES_4,

                           valor_TIME_T1_MATEMATICAS_1= valor_TIME_T1_MATEMATICAS_1, 
                           valor_TIME_T1_MATEMATICAS_2= valor_TIME_T1_MATEMATICAS_2, 
                           valor_TIME_T1_MATEMATICAS_3= valor_TIME_T1_MATEMATICAS_3, 
                           valor_TIME_T1_MATEMATICAS_4= valor_TIME_T1_MATEMATICAS_4,

                           valor_TIME_T1_BIOLOGIA_1= valor_TIME_T1_BIOLOGIA_1, 
                           valor_TIME_T1_BIOLOGIA_2= valor_TIME_T1_BIOLOGIA_2, 
                           valor_TIME_T1_BIOLOGIA_3= valor_TIME_T1_BIOLOGIA_3, 
                           valor_TIME_T1_BIOLOGIA_4= valor_TIME_T1_BIOLOGIA_4,

                           valor_TIME_T1_COMUNICACION_1= valor_TIME_T1_COMUNICACION_1, 
                           valor_TIME_T1_COMUNICACION_2= valor_TIME_T1_COMUNICACION_2, 
                           valor_TIME_T1_COMUNICACION_3= valor_TIME_T1_COMUNICACION_3, 
                           valor_TIME_T1_COMUNICACION_4= valor_TIME_T1_COMUNICACION_4,

                           valor_TIME_T1_LOGISTICA_1= valor_TIME_T1_LOGISTICA_1, 
                           valor_TIME_T1_LOGISTICA_2= valor_TIME_T1_LOGISTICA_2, 
                           valor_TIME_T1_LOGISTICA_3= valor_TIME_T1_LOGISTICA_3, 
                           valor_TIME_T1_LOGISTICA_4= valor_TIME_T1_LOGISTICA_4,


                           trimestre1=trimestre1_html)

@app.route('/T1_RecoleccionMuestras')
def recoleccion_muestras_T1():
    """
    Muestra la información correspondiente a la fase 3.
    Lee el contenido de T1_RecoleccionMuestras.html y lo renderiza en la plantilla 'T1_RecoleccionMuestras.html'.
    """
    with open('templates/T1_RecoleccionMuestras.html', 'r') as T1_RecoleccionMuestras_file:
        T1_RecoleccionMuestras_html = T1_RecoleccionMuestras_file.read()

    return render_template('T1_RecoleccionMuestras.html', T1_RecoleccionMuestras=T1_RecoleccionMuestras_html)

@app.route('/T1_Hidraulica')
def T1_Hidraulica():
    """
    Muestra la información correspondiente a la fase 3.
    Lee el contenido de T1_Hidraulica.html y lo renderiza en la plantilla 'T1_Hidraulica.html'.
    """
    with open('templates/T1_Hidraulica.html', 'r') as T1_Hidraulica_file:
        T1_Hidraulica_html = T1_Hidraulica_file.read()

    return render_template('T1_Hidraulica.html', T1_Hidraulica=T1_Hidraulica_html)

###############################################################################################
###############################################################################################
############################ MODELO DE INTELIGENCIA ARTIFICIAL ################################
###############################################################################################
###############################################################################################



@app.route('/objetivos')
def mostrar_objetivos():
    # Leer el contenido de objetivos.html
    with open('templates/objetivos.html', 'r') as objetivos_file:
        objetivos_html = objetivos_file.read()
    
    return render_template('objetivos.html', objetivos=objetivos_html)

def load_weights_biases(filename):
    with open(filename, 'rb') as f:
        weights_biases = pickle.load(f)
    return weights_biases['W1'], weights_biases['b1'], weights_biases['W2'], weights_biases['b2'], weights_biases['W3'], weights_biases['b3']

# Especifica la ruta y nombre de tu archivo .pkl
filename = 'weights_biases_20_elu.pkl'

# Cargar los pesos y sesgos
W1, b1, W2, b2, W3, b3 = load_weights_biases(filename)

def elu(self, x):
    '''
    Esta función aplica la función de activación ELU a la entrada x, devolviendo una matriz del mismo tamaño que x. 
    La función ELU se define como x si x > 0 y 0.5*(exp(x)-1) en caso contrario.
    '''
    return np.where(x <= 0, 0.5*(np.exp(x) - 1), x)

def dElu(self, x):
    '''
    Esta función calcula la derivada de la función ELU para una entrada x, que es 1 si x > 0 y 0.5*exp(x) en caso contrario.
    '''
    return np.where(x <= 0, 0.5*np.exp(x), 1)

def selu(x, alpha=1.67326, scale=1.0507):
    """Implementación de la función SELU"""
    condition = x > 0
    return scale * (alpha * (np.exp(x) - 1) * condition + x * (1 - condition))

# Hacer algo con los pesos y sesgos cargados
# Por ejemplo, imprimirlos en la consola
print("Pesos W1:")
print(W1)
print("Sesgos b1:")
print(b1)
print("Pesos W2:")
print(W2)
print("Sesgos b2:")
print(b2)
print("Pesos W3:")
print(W3)
print("Sesgos b3:")
print(b3)



@app.route('/formulario')
def formulario():
    return render_template('formulario_5.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Obtener los datos_TIME del formulario
    nombre = request.form['nombre']
    tipo_identificacion = request.form['tipoIdentificacion']
    numero = request.form['numero']
    correo = request.form['correo']
    ficha = request.form['ficha']
    nivel = request.form['nivel']
    programa = request.form['programa']
    telefono = request.form['telefono']
    pregunta1 = request.form['pregunta1']
    pregunta2 = request.form['pregunta2']
    pregunta3 = request.form['pregunta3']
    pregunta4 = request.form['pregunta4']
    pregunta5 = request.form['pregunta5']
    pregunta6 = request.form['pregunta6']
    pregunta7 = request.form['pregunta7']
    pregunta8 = request.form['pregunta8']
    pregunta9 = request.form['pregunta9']
    pregunta10 = request.form['pregunta10']
    pregunta11 = request.form['pregunta11']
    pregunta12 = request.form['pregunta12']
    pregunta13 = request.form['pregunta13']
    pregunta14 = request.form['pregunta14']
    pregunta15 = request.form['pregunta15']
    pregunta16 = request.form['pregunta16']
    pregunta17 = request.form['pregunta17']
    pregunta18 = request.form['pregunta18']
    pregunta19 = request.form['pregunta19']
    pregunta20 = request.form['pregunta20']

    # Organizar las respuestas en una lista
    respuestas = [nombre, tipo_identificacion, correo, ficha, nivel, programa, telefono, pregunta1, pregunta2, pregunta3,
                  pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, pregunta10,
                  pregunta11, pregunta12, pregunta13, pregunta14, pregunta15, pregunta16, pregunta17,
                  pregunta18, pregunta19, pregunta20]

    # Guardar las respuestas en un archivo CSV
    with open('respuestas.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        
        # Verificar si el archivo está vacío
        if file.tell() == 0:
            etiquetas = ['Nombre completo', 'Tipo de identificación', 'Correo electrónico', 'Ficha de caracterización','nivel'
                         'progama',
                         'Teléfono celular', 'Estado civil', 'Edad', 'Genero', 'Departamento de residencia', 
                         'Salud', 'Consumido Drogas', 'Tipo de Sustancia', 'Consumido el ultimo ano',
                         'consumido el ultimo trimestre', 'Ingresos', 'Estrato',]
            writer.writerow(etiquetas)
        
        # Escribir las respuestas en una nueva fila
        writer.writerow(respuestas)

   # Validar que las preguntas no estén vacías
    if pregunta1 == '' or pregunta2 == '' or pregunta3 == '' or pregunta4 == '' or pregunta5 == '' or pregunta6 == '' or pregunta7 == '' or pregunta8 == '' or pregunta9 == '' or pregunta10 == '' or pregunta11 == '' or pregunta12 == '' or pregunta13 == '' or pregunta14 == '' or pregunta15 == '' or pregunta16 == '' or pregunta17 == '' or pregunta18 == '' or pregunta19 == '' or pregunta20 == '':
        # Mostrar un mensaje de error en el formulario
        return render_template('formulario_5.html', error_message='Por favor, responda todas las preguntas.')

    try:
        # Convertir las preguntas a números de punto flotante
        preguntas = np.array([[float(pregunta1), float(pregunta2), float(pregunta3), float(pregunta4), float(pregunta5), float(pregunta6), float(pregunta7), float(pregunta8), float(pregunta9), float(pregunta10),
                               float(pregunta11), float(pregunta12), float(pregunta13), float(pregunta14), float(pregunta15), float(pregunta16), float(pregunta17), float(pregunta18), float(pregunta19), float(pregunta20)]])
    except ValueError:
        # Mostrar un mensaje de error en el formulario
        return render_template('formulario_5.html', error_message='Por favor, ingrese números válidos en las preguntas.')
    
    z1 = np.dot(preguntas, W1) + b1
    z2 = np.dot(z1, W2) + b2
    z3 = np.dot(z2, W3) + b3
    prediccion = 1 / (1 + np.exp(-z3))
    # Imprimir la predicción en la consola
    print("La predicción es:", prediccion)

    # Obtener el género del estudiante del formulario
    genero_estudiante = pregunta3


    # Definir el pronombre basado en el género del estudiante
    if genero_estudiante == "Masculino":
        pronombre = "el"
    elif genero_estudiante == "Femenino":
        pronombre = "la"
    else:
        pronombre = "el o la"

    # Modificar la respuesta de la predicción basada en el género del estudiante
    if prediccion[0][0] > 0.5:
        resultado = f"Según el modelo neuronal predice que, ...en prueba"
    else:
        resultado = f"Según el modelo neuronal, predice que, ...en prueba"

    # Redirigir al usuario a la ruta '/resultado' con el parámetro 'resultado'
    return redirect('/resultado?resultado=' + resultado + '&prediccion=' + str(prediccion[0][0]))

    '''
    # Modificar la respuesta de la predicción basada en el género del estudiante
    if prediccion[0][0] > 0.5:
        resultado = f"Según el modelo neuronal predice que, {nombre} tiene probabilidad de DESERCION en el programa de formación."
    else:
        resultado = f"Según el modelo neuronal, predice que, {nombre} tiene probabilidad de GRADUARSE en el programa de formación."
    '''


    
@app.route('/resultado')
def resultado():
    # Obtener el resultado y la prediccion del parámetro de consulta 'resultado' y 'prediccion'
    resultado = request.args.get('resultado')
    prediccion = request.args.get('prediccion')

    # Devolver una respuesta al usuario
    return render_template('resultado.html', resultado=resultado, prediccion=prediccion)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)