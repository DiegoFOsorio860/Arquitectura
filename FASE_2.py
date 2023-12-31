
import pandas as pd
import numpy as np


def FUNCTION_FASE_2(datos_TIME):
    # Leer el contenido de FASES.html

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
    return {   'valor_TIME_T1_1':valor_TIME_T1_1, 
                'valor_TIME_T1_2':valor_TIME_T1_2, 
                'valor_TIME_T1_3':valor_TIME_T1_3, 
                'valor_TIME_T1_4':valor_TIME_T1_4,
                
                'valor_TIME_T2_1':valor_TIME_T2_1, 
                'valor_TIME_T2_2':valor_TIME_T2_2, 
                'valor_TIME_T2_3':valor_TIME_T2_3, 
                'valor_TIME_T2_4':valor_TIME_T2_4,

                'valor_TIME_F1_1':valor_TIME_F1_1, 
                'valor_TIME_F1_2':valor_TIME_F1_2, 
                'valor_TIME_F1_3':valor_TIME_F1_3, 
                'valor_TIME_F1_4':valor_TIME_F1_4,
    }