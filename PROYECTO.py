import pandas as pd
import numpy as np


def FUNCTION_PROYECTO(datos_PROYECTO):
    # Leer el contenido de FASES.html

    # Suponiendo que 'datos_PROYECTO' es un DataFrame que contiene la información necesaria
    # Primera fila
    valor_PROYECTO_1_1 = datos_PROYECTO.iloc[4,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_1_2 = datos_PROYECTO.iloc[4,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_1_3 = datos_PROYECTO.iloc[4,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_1_4 = datos_PROYECTO.iloc[4,4]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_1_5 = datos_PROYECTO.iloc[4,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_1_6 = datos_PROYECTO.iloc[4,6]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_1_7 = datos_PROYECTO.iloc[4,7]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_1_8 = datos_PROYECTO.iloc[4,8]  # Reemplaza con los índices correspondientes

    # Segunda Fila
    valor_PROYECTO_2_1 = datos_PROYECTO.iloc[6,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_2_2 = datos_PROYECTO.iloc[6,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_2_3 = datos_PROYECTO.iloc[6,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_2_4 = datos_PROYECTO.iloc[6,6]  # Reemplaza con los índices correspondientes

    # Tercera Fila
    valor_PROYECTO_3_1 = datos_PROYECTO.iloc[8,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_3_2 = datos_PROYECTO.iloc[8,2]  # Reemplaza con los índices correspondientes

    # Cuarta Fila
    valor_PROYECTO_4_1 = datos_PROYECTO.iloc[9,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_4_2 = datos_PROYECTO.iloc[9,2]  # Reemplaza con los índices correspondientes

     # Quinta Fila
    valor_PROYECTO_5_1 = datos_PROYECTO.iloc[10,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_5_2 = datos_PROYECTO.iloc[10,2]  # Reemplaza con los índices correspondientes

    # Sexta Fila
    valor_PROYECTO_6_1 = datos_PROYECTO.iloc[11,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_6_2 = datos_PROYECTO.iloc[11,2]  # Reemplaza con los índices correspondientes

    # Septima fila
    valor_PROYECTO_7_1 = datos_PROYECTO.iloc[12,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_7_2 = datos_PROYECTO.iloc[12,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_7_3 = datos_PROYECTO.iloc[12,4]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_7_4 = datos_PROYECTO.iloc[12,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_7_5 = datos_PROYECTO.iloc[12,7]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_7_6 = datos_PROYECTO.iloc[13,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_7_7 = datos_PROYECTO.iloc[13,7]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_7_8 = datos_PROYECTO.iloc[14,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_7_9 = datos_PROYECTO.iloc[14,7]  # Reemplaza con los índices correspondientes

    # Octava Fila
    valor_PROYECTO_8_1 = datos_PROYECTO.iloc[17,1]  # Reemplaza con los índices correspondientes
    # Novena Fila
    valor_PROYECTO_9_1 = datos_PROYECTO.iloc[18,1]  # Reemplaza con los índices correspondientes

    # Décima Fila
    valor_PROYECTO_10_1 = datos_PROYECTO.iloc[19,1]  # Reemplaza con los índices correspondientes
    # once Fila
    valor_PROYECTO_11_1 = datos_PROYECTO.iloc[20,1]  # Reemplaza con los índices correspondientes

    # Doce Fila
    valor_PROYECTO_12_1 = datos_PROYECTO.iloc[21,1]  # Reemplaza con los índices correspondientes
    # Trece Fila
    valor_PROYECTO_13_1 = datos_PROYECTO.iloc[22,1]  # Reemplaza con los índices correspondientes

    # 14 Fila
    valor_PROYECTO_14_1 = datos_PROYECTO.iloc[23,1]  # Reemplaza con los índices correspondientes
    # 15 Fila
    valor_PROYECTO_15_1 = datos_PROYECTO.iloc[24,1]  # Reemplaza con los índices correspondientes
    # 16 Fila
    valor_PROYECTO_16_1 = datos_PROYECTO.iloc[25,1]  # Reemplaza con los índices correspondientes
    # 17 Fila
    valor_PROYECTO_17_1 = datos_PROYECTO.iloc[26,1]  # Reemplaza con los índices correspondientes

    # 18 Fila
    valor_PROYECTO_18_1 = datos_PROYECTO.iloc[27,1]  # Reemplaza con los índices correspondientes
    # 19 Fila
    valor_PROYECTO_19_1 = datos_PROYECTO.iloc[28,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_2 = datos_PROYECTO.iloc[28,2]  # Reemplaza con los índices correspondientes

    # 20 fila
    valor_PROYECTO_20_1 = datos_PROYECTO.iloc[29,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_2 = datos_PROYECTO.iloc[29,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_3 = datos_PROYECTO.iloc[29,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_4 = datos_PROYECTO.iloc[30,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_5 = datos_PROYECTO.iloc[30,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_6 = datos_PROYECTO.iloc[31,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_7 = datos_PROYECTO.iloc[31,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_8 = datos_PROYECTO.iloc[14,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_9 = datos_PROYECTO.iloc[14,7]  # Reemplaza con los índices correspondientes

    # Renderizar la plantilla con los valor_TIME_T1_es extraídos y el contenido de la estructuraaa
    return {   
                # Primera Fila
                'valor_PROYECTO_1_1':valor_PROYECTO_1_1, 
                'valor_PROYECTO_1_2':valor_PROYECTO_1_2, 
                'valor_PROYECTO_1_3':valor_PROYECTO_1_3, 
                'valor_PROYECTO_1_4':valor_PROYECTO_1_4,
                'valor_PROYECTO_1_5':valor_PROYECTO_1_5,
                'valor_PROYECTO_1_6':valor_PROYECTO_1_6,
                'valor_PROYECTO_1_7':valor_PROYECTO_1_7,
                'valor_PROYECTO_1_8':valor_PROYECTO_1_8,

                # Segunda Fila
                'valor_PROYECTO_2_1':valor_PROYECTO_2_1,
                'valor_PROYECTO_2_2':valor_PROYECTO_2_2,
                'valor_PROYECTO_2_3':valor_PROYECTO_2_3,
                'valor_PROYECTO_2_4':valor_PROYECTO_2_4,

                # Tercera Fila
                'valor_PROYECTO_3_1':valor_PROYECTO_3_1,
                'valor_PROYECTO_3_2':valor_PROYECTO_3_2,

                # Cuarta Fila
                'valor_PROYECTO_4_1':valor_PROYECTO_4_1,
                'valor_PROYECTO_4_2':valor_PROYECTO_4_2,

                # Quinta Fila
                'valor_PROYECTO_5_1':valor_PROYECTO_5_1,
                'valor_PROYECTO_5_2':valor_PROYECTO_5_2,

                # Sexta Fila
                'valor_PROYECTO_6_1':valor_PROYECTO_6_1,
                'valor_PROYECTO_6_2':valor_PROYECTO_6_2,

                # Séptima Fila
                'valor_PROYECTO_7_1':valor_PROYECTO_7_1, 
                'valor_PROYECTO_7_2':valor_PROYECTO_7_2, 
                'valor_PROYECTO_7_3':valor_PROYECTO_7_3, 
                'valor_PROYECTO_7_4':valor_PROYECTO_7_4,
                'valor_PROYECTO_7_5':valor_PROYECTO_7_5,
                'valor_PROYECTO_7_6':valor_PROYECTO_7_6,
                'valor_PROYECTO_7_7':valor_PROYECTO_7_7,
                'valor_PROYECTO_7_8':valor_PROYECTO_7_8,
                'valor_PROYECTO_7_9':valor_PROYECTO_7_9,

                # Octaba Fila
                'valor_PROYECTO_8_1':valor_PROYECTO_8_1, 
                # Novena Fila
                'valor_PROYECTO_9_1':valor_PROYECTO_9_1, 

                # Décima Fila
                'valor_PROYECTO_10_1':valor_PROYECTO_10_1, 
                # Ocnce Fila
                'valor_PROYECTO_11_1':valor_PROYECTO_11_1, 

                # Doce Fila
                'valor_PROYECTO_12_1':valor_PROYECTO_12_1, 
                # Trece Fila
                'valor_PROYECTO_13_1':valor_PROYECTO_13_1, 

                # Catorce Fila
                'valor_PROYECTO_14_1':valor_PROYECTO_14_1, 
                # Quince Fila
                'valor_PROYECTO_15_1':valor_PROYECTO_15_1, 
                # 16 Fila
                'valor_PROYECTO_16_1':valor_PROYECTO_16_1, 
                # 17 Fila
                'valor_PROYECTO_17_1':valor_PROYECTO_17_1, 

                # 16 Fila
                'valor_PROYECTO_18_1':valor_PROYECTO_18_1, 
                # 17 Fila
                'valor_PROYECTO_19_1':valor_PROYECTO_19_1, 
                'valor_PROYECTO_19_2':valor_PROYECTO_19_2, 

                 # Séptima Fila
                'valor_PROYECTO_20_1':valor_PROYECTO_20_1, 
                'valor_PROYECTO_20_2':valor_PROYECTO_20_2, 
                'valor_PROYECTO_20_3':valor_PROYECTO_20_3, 
                'valor_PROYECTO_20_4':valor_PROYECTO_20_4,
                'valor_PROYECTO_20_5':valor_PROYECTO_20_5,
    }