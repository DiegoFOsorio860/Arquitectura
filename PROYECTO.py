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
    valor_PROYECTO_19_3 = datos_PROYECTO.iloc[29,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_4 = datos_PROYECTO.iloc[29,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_5 = datos_PROYECTO.iloc[30,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_6 = datos_PROYECTO.iloc[30,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_7 = datos_PROYECTO.iloc[31,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_8 = datos_PROYECTO.iloc[31,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_9 = datos_PROYECTO.iloc[32,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_10 = datos_PROYECTO.iloc[32,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_11 = datos_PROYECTO.iloc[33,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_19_12 = datos_PROYECTO.iloc[33,3]  # Reemplaza con los índices correspondientes

    # 20 fila
    valor_PROYECTO_20_1 = datos_PROYECTO.iloc[34,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_2 = datos_PROYECTO.iloc[34,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_3 = datos_PROYECTO.iloc[34,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_4 = datos_PROYECTO.iloc[35,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_5 = datos_PROYECTO.iloc[35,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_6 = datos_PROYECTO.iloc[36,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_7 = datos_PROYECTO.iloc[36,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_8 = datos_PROYECTO.iloc[37,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_20_9 = datos_PROYECTO.iloc[37,3]  # Reemplaza con los índices correspondientes

    # 21 Fila
    valor_PROYECTO_21_1 = datos_PROYECTO.iloc[38,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_2 = datos_PROYECTO.iloc[39,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_3 = datos_PROYECTO.iloc[39,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_4 = datos_PROYECTO.iloc[39,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_5 = datos_PROYECTO.iloc[40,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_6 = datos_PROYECTO.iloc[40,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_7 = datos_PROYECTO.iloc[41,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_8 = datos_PROYECTO.iloc[41,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_9 = datos_PROYECTO.iloc[42,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_10 = datos_PROYECTO.iloc[42,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_11 = datos_PROYECTO.iloc[43,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_12 = datos_PROYECTO.iloc[43,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_13 = datos_PROYECTO.iloc[44,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_14 = datos_PROYECTO.iloc[44,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_15 = datos_PROYECTO.iloc[45,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_16 = datos_PROYECTO.iloc[45,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_17 = datos_PROYECTO.iloc[45,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_18 = datos_PROYECTO.iloc[46,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_19 = datos_PROYECTO.iloc[46,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_20 = datos_PROYECTO.iloc[47,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_21 = datos_PROYECTO.iloc[47,3]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_22 = datos_PROYECTO.iloc[48,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_21_23 = datos_PROYECTO.iloc[48,3]  # Reemplaza con los índices correspondientes

    # 22 Fila
    valor_PROYECTO_22_1 = datos_PROYECTO.iloc[49,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_22_2 = datos_PROYECTO.iloc[50,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_22_3 = datos_PROYECTO.iloc[51,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_22_4 = datos_PROYECTO.iloc[52,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_22_5 = datos_PROYECTO.iloc[53,1]  # Reemplaza con los índices correspondientes

    # 23 Fila - <!-- 2.6 Innovación/Gestión Tecnológica: -->
    valor_PROYECTO_23_1 = datos_PROYECTO.iloc[54,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_2 = datos_PROYECTO.iloc[55,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_3 = datos_PROYECTO.iloc[56,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_4 = datos_PROYECTO.iloc[57,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_5 = datos_PROYECTO.iloc[58,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_6 = datos_PROYECTO.iloc[59,1]  # Reemplaza con los índices correspondientes

    # 24 Fila -- 2.7 Valoración Productiva
    valor_PROYECTO_23_1 = datos_PROYECTO.iloc[60,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_2 = datos_PROYECTO.iloc[61,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_3 = datos_PROYECTO.iloc[61,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_4 = datos_PROYECTO.iloc[61,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_5 = datos_PROYECTO.iloc[62,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_6 = datos_PROYECTO.iloc[62,5]  # Reemplaza con los índices correspondientes

    valor_PROYECTO_23_7 = datos_PROYECTO.iloc[63,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_8 = datos_PROYECTO.iloc[63,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_9 = datos_PROYECTO.iloc[63,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_10 = datos_PROYECTO.iloc[64,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_11 = datos_PROYECTO.iloc[64,5]  # Reemplaza con los índices correspondientes

    valor_PROYECTO_23_12 = datos_PROYECTO.iloc[65,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_13 = datos_PROYECTO.iloc[65,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_14 = datos_PROYECTO.iloc[65,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_15 = datos_PROYECTO.iloc[66,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_16 = datos_PROYECTO.iloc[66,5]  # Reemplaza con los índices correspondientes

    valor_PROYECTO_23_17 = datos_PROYECTO.iloc[67,1]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_18 = datos_PROYECTO.iloc[67,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_19 = datos_PROYECTO.iloc[67,5]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_20 = datos_PROYECTO.iloc[68,2]  # Reemplaza con los índices correspondientes
    valor_PROYECTO_23_21 = datos_PROYECTO.iloc[68,5]  # Reemplaza con los índices correspondientes

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

                # 18 Fila
                'valor_PROYECTO_18_1':valor_PROYECTO_18_1, 
                # 19 Fila
                'valor_PROYECTO_19_1':valor_PROYECTO_19_1, 
                'valor_PROYECTO_19_2':valor_PROYECTO_19_2, 
                'valor_PROYECTO_19_3':valor_PROYECTO_19_3, 
                'valor_PROYECTO_19_4':valor_PROYECTO_19_4,
                'valor_PROYECTO_19_5':valor_PROYECTO_19_5, 
                'valor_PROYECTO_19_6':valor_PROYECTO_19_6, 
                'valor_PROYECTO_19_7':valor_PROYECTO_19_7, 
                'valor_PROYECTO_19_8':valor_PROYECTO_19_8,
                'valor_PROYECTO_19_9':valor_PROYECTO_19_9, 
                'valor_PROYECTO_19_10':valor_PROYECTO_19_10,
                'valor_PROYECTO_19_11':valor_PROYECTO_19_11, 
                'valor_PROYECTO_19_12':valor_PROYECTO_19_12,  
                

                 # 20 Fila
                'valor_PROYECTO_20_1':valor_PROYECTO_20_1, 
                'valor_PROYECTO_20_2':valor_PROYECTO_20_2, 
                'valor_PROYECTO_20_3':valor_PROYECTO_20_3, 
                'valor_PROYECTO_20_4':valor_PROYECTO_20_4,
                'valor_PROYECTO_20_5':valor_PROYECTO_20_5,
                'valor_PROYECTO_20_6':valor_PROYECTO_20_6, 
                'valor_PROYECTO_20_7':valor_PROYECTO_20_7, 
                'valor_PROYECTO_20_8':valor_PROYECTO_20_8,
                'valor_PROYECTO_20_9':valor_PROYECTO_20_9,

                # 21 Fila
                'valor_PROYECTO_21_1':valor_PROYECTO_21_1, 
                'valor_PROYECTO_21_2':valor_PROYECTO_21_2, 
                'valor_PROYECTO_21_3':valor_PROYECTO_21_3,
                'valor_PROYECTO_21_4':valor_PROYECTO_21_4, 
                'valor_PROYECTO_21_5':valor_PROYECTO_21_5, 
                'valor_PROYECTO_21_6':valor_PROYECTO_21_6, 
                'valor_PROYECTO_21_7':valor_PROYECTO_21_7,
                'valor_PROYECTO_21_8':valor_PROYECTO_21_8, 
                'valor_PROYECTO_21_9':valor_PROYECTO_21_9,
                'valor_PROYECTO_21_10':valor_PROYECTO_21_10, 
                'valor_PROYECTO_21_11':valor_PROYECTO_21_11,  
                'valor_PROYECTO_21_12':valor_PROYECTO_21_12,
                'valor_PROYECTO_21_13':valor_PROYECTO_21_13,  
                'valor_PROYECTO_21_14':valor_PROYECTO_21_14,
                'valor_PROYECTO_21_15':valor_PROYECTO_21_15, 
                'valor_PROYECTO_21_16':valor_PROYECTO_21_16,  
                'valor_PROYECTO_21_17':valor_PROYECTO_21_17,
                'valor_PROYECTO_21_18':valor_PROYECTO_21_18,  
                'valor_PROYECTO_21_19':valor_PROYECTO_21_19,
                'valor_PROYECTO_21_20':valor_PROYECTO_21_20,  
                'valor_PROYECTO_21_21':valor_PROYECTO_21_21,
                'valor_PROYECTO_21_22':valor_PROYECTO_21_22,  
                'valor_PROYECTO_21_23':valor_PROYECTO_21_23, 

                # 22 Fila
                'valor_PROYECTO_22_1':valor_PROYECTO_22_1, 
                'valor_PROYECTO_22_2':valor_PROYECTO_22_2, 
                'valor_PROYECTO_22_3':valor_PROYECTO_22_3,
                'valor_PROYECTO_22_4':valor_PROYECTO_22_4, 
                'valor_PROYECTO_22_5':valor_PROYECTO_22_5, 

                # 23 Fila
                'valor_PROYECTO_23_1':valor_PROYECTO_23_1, 
                'valor_PROYECTO_23_2':valor_PROYECTO_23_2, 
                'valor_PROYECTO_23_3':valor_PROYECTO_23_3,
                'valor_PROYECTO_23_4':valor_PROYECTO_23_4, 
                'valor_PROYECTO_23_5':valor_PROYECTO_23_5,
                'valor_PROYECTO_23_6':valor_PROYECTO_23_6,
                'valor_PROYECTO_23_7':valor_PROYECTO_23_7, 
                'valor_PROYECTO_23_8':valor_PROYECTO_23_8, 
                'valor_PROYECTO_23_9':valor_PROYECTO_23_9,
                'valor_PROYECTO_23_10':valor_PROYECTO_23_10, 
                'valor_PROYECTO_23_11':valor_PROYECTO_23_11,
                'valor_PROYECTO_23_12':valor_PROYECTO_23_12,
                'valor_PROYECTO_23_13':valor_PROYECTO_23_13, 
                'valor_PROYECTO_23_14':valor_PROYECTO_23_14,
                'valor_PROYECTO_23_15':valor_PROYECTO_23_15,
                'valor_PROYECTO_23_16':valor_PROYECTO_23_16, 
                'valor_PROYECTO_23_17':valor_PROYECTO_23_17,
                'valor_PROYECTO_23_18':valor_PROYECTO_23_18,
                'valor_PROYECTO_23_19':valor_PROYECTO_23_19, 
                'valor_PROYECTO_23_20':valor_PROYECTO_23_20,
                'valor_PROYECTO_23_21':valor_PROYECTO_23_21,        
    }