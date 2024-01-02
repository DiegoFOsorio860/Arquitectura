import pandas as pd
import numpy as np


def FUNCTION_T1(datos_TIME):
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

    valor_TIME_T1_COMP_ESP = datos_TIME.iloc[250,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMP_CLV = datos_TIME.iloc[251,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMP_COMP = datos_TIME.iloc[251,2]  # Reemplaza con los índices correspondientes

    return{ 
            'valor_TIME_T1_HIDRAULICA_1':valor_TIME_T1_HIDRAULICA_1, 
            'valor_TIME_T1_HIDRAULICA_2': valor_TIME_T1_HIDRAULICA_2, 
            'valor_TIME_T1_HIDRAULICA_3': valor_TIME_T1_HIDRAULICA_3, 
            'valor_TIME_T1_HIDRAULICA_4': valor_TIME_T1_HIDRAULICA_4,

            'valor_TIME_T1_REC_MUESTRAS_1':valor_TIME_T1_REC_MUESTRAS_1, 
            'valor_TIME_T1_REC_MUESTRAS_2': valor_TIME_T1_REC_MUESTRAS_2, 
            'valor_TIME_T1_REC_MUESTRAS_3': valor_TIME_T1_REC_MUESTRAS_3, 
            'valor_TIME_T1_REC_MUESTRAS_4': valor_TIME_T1_REC_MUESTRAS_4,

            'valor_TIME_T1_INGLES_1': valor_TIME_T1_INGLES_1, 
            'valor_TIME_T1_INGLES_2': valor_TIME_T1_INGLES_2, 
            'valor_TIME_T1_INGLES_3': valor_TIME_T1_INGLES_3, 
            'valor_TIME_T1_INGLES_4': valor_TIME_T1_INGLES_4,

            'valor_TIME_T1_MATEMATICAS_1': valor_TIME_T1_MATEMATICAS_1, 
            'valor_TIME_T1_MATEMATICAS_2': valor_TIME_T1_MATEMATICAS_2, 
            'valor_TIME_T1_MATEMATICAS_3': valor_TIME_T1_MATEMATICAS_3, 
            'valor_TIME_T1_MATEMATICAS_4': valor_TIME_T1_MATEMATICAS_4,

            'valor_TIME_T1_BIOLOGIA_1': valor_TIME_T1_BIOLOGIA_1, 
            'valor_TIME_T1_BIOLOGIA_2': valor_TIME_T1_BIOLOGIA_2, 
            'valor_TIME_T1_BIOLOGIA_3': valor_TIME_T1_BIOLOGIA_3, 
            'valor_TIME_T1_BIOLOGIA_4': valor_TIME_T1_BIOLOGIA_4,

            'valor_TIME_T1_COMUNICACION_1': valor_TIME_T1_COMUNICACION_1, 
            'valor_TIME_T1_COMUNICACION_2': valor_TIME_T1_COMUNICACION_2, 
            'valor_TIME_T1_COMUNICACION_3': valor_TIME_T1_COMUNICACION_3, 
            'valor_TIME_T1_COMUNICACION_4': valor_TIME_T1_COMUNICACION_4,

            'valor_TIME_T1_LOGISTICA_1': valor_TIME_T1_LOGISTICA_1, 
            'valor_TIME_T1_LOGISTICA_2': valor_TIME_T1_LOGISTICA_2, 
            'valor_TIME_T1_LOGISTICA_3': valor_TIME_T1_LOGISTICA_3, 
            'valor_TIME_T1_LOGISTICA_4': valor_TIME_T1_LOGISTICA_4,
    }