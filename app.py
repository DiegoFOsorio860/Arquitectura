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

###############################################################################################
######################################## FUNCIONES  #########################################
###############################################################################################
from FASES import FUNCTION_FASES
from T1_Trimestre import FUNCTION_T1
from T1_RecoleccionMuestras import FUNCTION_T1_REC_MUESTRAS
from T1_Hidraulica import FUNCTION_T1_HIDRAULICA
from PROYECTO import FUNCTION_PROYECTO
from FASE_1 import FUNCTION_FASE_1
from FASE_2 import FUNCTION_FASE_2
from FASE_3 import FUNCTION_FASE_3
from T1_Trimestre_graficos import FUNCTION_GRAPH_1
from T1_Trimestre_graficos import FUNCTION_GRAPH_2


app = Flask(__name__)

# Cargar datos_TIME desde el archivo Excel
datos_TIME = pd.read_excel('30122023 Arquitectura Curricular - Proyecto de Formación.xlsx', sheet_name='TIME')
# Cargar datos_TIME desde el archivo Excel
datos_ARQUITECTURA = pd.read_excel('30122023 Arquitectura Curricular - Proyecto de Formación.xlsx', sheet_name='ARQUITECTURA')

datos_PROYECTO = pd.read_excel('30122023 Arquitectura Curricular - Proyecto de Formación.xlsx', sheet_name='PROYECTO_FORMACION')

@app.route('/')
def header():
    # Renderizar el encabezado y la introducción
    with open('templates/header.html', 'r', encoding='utf-8-sig') as header_file:
        header_html = header_file.read()

    with open('templates/introduccion.html', 'r', encoding='utf-8-sig') as intro_file:
        intro_html = intro_file.read()

    return render_template('header.html', header=header_html, intro=intro_html)


###############################################################################################
######################################## PROYECTO  #########################################
###############################################################################################

@app.route('/PROYECTO')
def mostrar_PROYECTO():
    """
    Muestra la información correspondiente a la fase 1.
    Lee el contenido de fase1.html y lo renderiza en la plantilla 'fase1.html'.
    """
    datos = FUNCTION_PROYECTO(datos_PROYECTO)

    return render_template('PROYECTO.html', **datos)

###############################################################################################
######################################## FASES  #########################################
###############################################################################################

@app.route('/FASES')
def mostrar_FASES():
    """
    Muestra la información correspondiente a la fase 1.
    Lee el contenido de fase1.html y lo renderiza en la plantilla 'fase1.html'.
    """
    datos =  FUNCTION_FASES(datos_TIME)

    return render_template('FASES.html', **datos)

###############################################################################################
######################################## FASE 1  ##############################################
###############################################################################################

@app.route('/FASE_1')
def mostrar_FASE_1():
    """
    Muestra la información correspondiente a la fase 1.
    Lee el contenido de fase1.html y lo renderiza en la plantilla 'fase1.html'.
    """
    datos =  FUNCTION_FASE_1(datos_TIME)

    return render_template('FASE_1.html', **datos)
    
###############################################################################################
######################################## FASE 2  ##############################################
###############################################################################################

@app.route('/FASE_2')
def mostrar_FASE_2():
    """
    Muestra la información correspondiente a la fase 1.
    Lee el contenido de fase1.html y lo renderiza en la plantilla 'fase1.html'.
    """
    datos =  FUNCTION_FASE_2(datos_TIME)

    return render_template('FASE_2.html', **datos)

###############################################################################################
######################################## FASE 2  ##############################################
###############################################################################################

@app.route('/FASE_3')
def mostrar_FASE_3():
    """
    Muestra la información correspondiente a la fase 1.
    Lee el contenido de fase1.html y lo renderiza en la plantilla 'fase1.html'.
    """
    datos =  FUNCTION_FASE_3(datos_TIME)

    return render_template('FASE_3.html', **datos)

###############################################################################################
######################################## FASE 1 - T1  #########################################
###############################################################################################

@app.route('/T1_Trimestre')
def ARQ_T1():
    """
    Muestra la información correspondiente a la fase 3.
    Lee el contenido de T1_Hidraulica.html y lo renderiza en la plantilla 'T1_Hidraulica.html'.
    """
    # Suponiendo que datos_TIME está disponible aquí
    # Llamada a la función importada para obtener datos

    datos = FUNCTION_T1(datos_TIME)

    # Renderiza la plantilla 'T1_Trimestre.html' con los datos obtenidos
    # Agregamos la función FUNCTION_GRAPH_1() a la plantilla

    datos['diagrama_barras'] = FUNCTION_GRAPH_1(datos_TIME)
    datos['diagrama_pie'] = FUNCTION_GRAPH_2(datos_TIME)
    
    return render_template('T1_Trimestre.html', **datos)

###############################################################################################
################################## FASE 1 - T1 - HIDRAULICA ##################################
###############################################################################################

@app.route('/T1_Hidraulica')
def ARQ_T1_HIDRAULICA():
    """
    Muestra la información correspondiente a la fase 3.
    Lee el contenido de T1_Hidraulica.html y lo renderiza en la plantilla 'T1_Hidraulica.html'.
    """
    # Suponiendo que datos_ARQUITECTURA está disponible aquí
    # Llamada a la función importada para obtener datos
    datos = FUNCTION_T1_HIDRAULICA(datos_ARQUITECTURA)

    # Renderiza la plantilla 'T1_Hidraulica.html' con los datos obtenidos
    return render_template('T1_Hidraulica.html', **datos)

###############################################################################################
############################# FASE 1 - T1 - REC DE MUESTRAS ##################################
###############################################################################################

# Definición de la ruta para '/T1_RecoleccionMuestras'
@app.route('/T1_RecoleccionMuestras')
def ARQ_T1_REC_MUESTRAS():
    """
    Muestra la información correspondiente a la fase 3.
    Lee el contenido de T1_Hidraulica.html y lo renderiza en la plantilla 'T1_Hidraulica.html'.
    """
    # Suponiendo que datos_ARQUITECTURA está disponible aquí
    # Llamada a la función importada para obtener datos
    datos = FUNCTION_T1_REC_MUESTRAS(datos_ARQUITECTURA)

    # Renderiza la plantilla 'T1_RecoleccionMuestras.html' con los datos obtenidos
    return render_template('T1_RecoleccionMuestras.html', **datos)


###############################################################################################
###############################################################################################
############################ MODELO DE INTELIGENCIA ARTIFICIAL ################################
###############################################################################################
###############################################################################################

def load_weights_biases(filename):
    with open(filename, 'rb') as f:
        weights_biases = pickle.load(f)
    return weights_biases['W1'], weights_biases['b1'], weights_biases['W2'], weights_biases['b2'], weights_biases['W3'], weights_biases['b3']

# Especifica la ruta y nombre de tu archivo .pkl
filename = 'weights_biases_20_elu.pkl'

# Cargar los pesos y sesgos
W1, b1, W2, b2, W3, b3 = load_weights_biases(filename)


def sigmoid(x):
    """Función sigmoidal."""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Derivada de la función sigmoidal."""
    sig = sigmoid(x)
    return sig * (1 - sig)

def relu(x):
    '''
    Función de activación ReLU.
    '''
    return np.maximum(0, x)

def dRelu(x):
    '''
    Derivada de la función de activación ReLU.
    '''
    return np.where(x <= 0, 0, 1)

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


@app.route('/objetivos')
def mostrar_objetivos():
    # Leer el contenido de objetivos.html
    with open('templates/objetivos.html', 'r',  encoding='utf-8') as objetivos_file:
        objetivos_html = objetivos_file.read()
    
    return render_template('objetivos.html', objetivos=objetivos_html)


# Hacer algo con los pesos y sesgos cargados
# Por ejemplo, imprimirlos en la consola
@app.route('/formulario')
def formulario():
    return render_template('formulario_5.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Obtener los datos del formulario
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
    
    def softmax(x):
    #Implementación de la función Softmax
        e_x = np.exp(x - np.max(x))
        return e_x / np.sum(e_x, axis=1, keepdims=True)
    
    z1 = np.dot(preguntas, W1) + b1
    a1 = np.tanh(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = selu(z2)
    z3 = np.dot(a2, W3) + b3
    prediccion = 1 / (1 + np.exp(-z3))
    # Imprimir la predicción en la consola
    print("La predicción es:", prediccion)


# Modificar la respuesta de la predicción
    if prediccion[0][0] > 0.5:
        resultado = f'Aprendiz {nombre} tiene probabilidad de GRADUARSE en el programa de formación.'
    else:
        resultado = f'Aprendiz {nombre} tiene probabilidad de DESERCION en el programa de formación.'


    # Mostrar la predicción en la consola
    print("Predicción:", prediccion)

    # Redirigir al usuario a la ruta '/resultado' con el parámetro 'resultado'
    return redirect('/resultado?resultado=' + resultado + '&prediccion=' + str(prediccion[0][0]))


@app.route('/resultado')
def resultado():
    # Obtener el resultado y la prediccion del parámetro de consulta 'resultado' y 'prediccion'
    resultado = request.args.get('resultado')
    prediccion = request.args.get('prediccion')

    # Devolver una respuesta al usuario
    return render_template('resultado.html', resultado=resultado, prediccion=prediccion)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)