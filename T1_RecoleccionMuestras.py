
import pandas as pd
import numpy as np


def FUNCTION_T1_REC_MUESTRAS(datos_ARQUITECTURA):
    """
    Esta función procesa los datos de ARQUITECTURA y extrae valores específicos 
    basados en índices predefinidos.

    Args:
    - datos_ARQUITECTURA (pandas.DataFrame): DataFrame con los datos de ARQUITECTURA.

    Returns:
    Un diccionario con los valores correspondientes a diferentes índices.
    """

    # Devolver los valores en un diccionario
    valor_ARQ_T1_REC_MUESTRAS_1_1 = datos_ARQUITECTURA.iloc[36,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_1_2 = datos_ARQUITECTURA.iloc[36,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_1_3 = datos_ARQUITECTURA.iloc[36,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_2_1 = datos_ARQUITECTURA.iloc[37,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_2_2 = datos_ARQUITECTURA.iloc[37,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_2_3 = datos_ARQUITECTURA.iloc[37,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_3_1 = datos_ARQUITECTURA.iloc[38,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_3_2 = datos_ARQUITECTURA.iloc[38,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_3_3 = datos_ARQUITECTURA.iloc[38,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_4_1 = datos_ARQUITECTURA.iloc[39,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_4_2 = datos_ARQUITECTURA.iloc[39,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_4_3 = datos_ARQUITECTURA.iloc[39,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_5_1 = datos_ARQUITECTURA.iloc[40,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_5_2 = datos_ARQUITECTURA.iloc[40,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_5_3 = datos_ARQUITECTURA.iloc[40,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_6_1 = datos_ARQUITECTURA.iloc[41,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_6_2 = datos_ARQUITECTURA.iloc[41,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_6_3 = datos_ARQUITECTURA.iloc[41,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_7_1 = datos_ARQUITECTURA.iloc[42,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_7_2 = datos_ARQUITECTURA.iloc[42,5]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_8_1 = datos_ARQUITECTURA.iloc[43,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_8_2 = datos_ARQUITECTURA.iloc[43,5]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_9_1 = datos_ARQUITECTURA.iloc[44,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_9_2 = datos_ARQUITECTURA.iloc[44,5]  # Reemplaza con los índices correspondientes

    ###############################################################################################
    ################################### CONOCIMIENTO Y SABERES ####################################
    ###############################################################################################

    valor_ARQ_T1_REC_MUESTRAS_10_1 = datos_ARQUITECTURA.iloc[45,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_10_2 = datos_ARQUITECTURA.iloc[45,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_10_3 = datos_ARQUITECTURA.iloc[45,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_10_4 = datos_ARQUITECTURA.iloc[45,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_11_1 = datos_ARQUITECTURA.iloc[46,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_11_2 = datos_ARQUITECTURA.iloc[46,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_11_3 = datos_ARQUITECTURA.iloc[46,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_11_4 = datos_ARQUITECTURA.iloc[46,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_12_1 = datos_ARQUITECTURA.iloc[47,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_12_2 = datos_ARQUITECTURA.iloc[47,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_12_3 = datos_ARQUITECTURA.iloc[47,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_12_4 = datos_ARQUITECTURA.iloc[47,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_13_1 = datos_ARQUITECTURA.iloc[48,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_13_2 = datos_ARQUITECTURA.iloc[48,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_13_3 = datos_ARQUITECTURA.iloc[48,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_13_4 = datos_ARQUITECTURA.iloc[48,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_14_1 = datos_ARQUITECTURA.iloc[49,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_14_2 = datos_ARQUITECTURA.iloc[49,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_14_3 = datos_ARQUITECTURA.iloc[49,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_14_4 = datos_ARQUITECTURA.iloc[49,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_15_1 = datos_ARQUITECTURA.iloc[50,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_15_2 = datos_ARQUITECTURA.iloc[50,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_15_3 = datos_ARQUITECTURA.iloc[50,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_15_4 = datos_ARQUITECTURA.iloc[50,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_16_1 = datos_ARQUITECTURA.iloc[51,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_16_2 = datos_ARQUITECTURA.iloc[51,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_16_3 = datos_ARQUITECTURA.iloc[51,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_16_4 = datos_ARQUITECTURA.iloc[51,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_17_1 = datos_ARQUITECTURA.iloc[52,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_17_2 = datos_ARQUITECTURA.iloc[52,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_17_3 = datos_ARQUITECTURA.iloc[52,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_17_4 = datos_ARQUITECTURA.iloc[52,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_18_1 = datos_ARQUITECTURA.iloc[53,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_18_2 = datos_ARQUITECTURA.iloc[53,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_18_3 = datos_ARQUITECTURA.iloc[53,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_18_4 = datos_ARQUITECTURA.iloc[53,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_19_1 = datos_ARQUITECTURA.iloc[54,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_19_2 = datos_ARQUITECTURA.iloc[54,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_19_3 = datos_ARQUITECTURA.iloc[54,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_19_4 = datos_ARQUITECTURA.iloc[54,13]  # Reemplaza con los índices correspondientes

    ###############################################################################################
    ############################ EVIDENCIA DE PROYECTO  ###########################################
    ###############################################################################################

    valor_ARQ_T1_REC_MUESTRAS_20_1 = datos_ARQUITECTURA.iloc[55,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_20_2 = datos_ARQUITECTURA.iloc[55,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_20_3 = datos_ARQUITECTURA.iloc[55,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_20_4 = datos_ARQUITECTURA.iloc[55,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_21_1 = datos_ARQUITECTURA.iloc[56,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_21_2 = datos_ARQUITECTURA.iloc[56,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_21_3 = datos_ARQUITECTURA.iloc[56,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_21_4 = datos_ARQUITECTURA.iloc[56,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_22_1 = datos_ARQUITECTURA.iloc[57,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_22_2 = datos_ARQUITECTURA.iloc[57,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_22_3 = datos_ARQUITECTURA.iloc[57,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_22_4 = datos_ARQUITECTURA.iloc[57,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_23_1 = datos_ARQUITECTURA.iloc[58,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_23_2 = datos_ARQUITECTURA.iloc[58,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_23_3 = datos_ARQUITECTURA.iloc[58,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_23_4 = datos_ARQUITECTURA.iloc[58,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_24_1 = datos_ARQUITECTURA.iloc[59,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_24_2 = datos_ARQUITECTURA.iloc[59,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_24_3 = datos_ARQUITECTURA.iloc[59,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_24_4 = datos_ARQUITECTURA.iloc[59,13]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_REC_MUESTRAS_25_1 = datos_ARQUITECTURA.iloc[60,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_25_2 = datos_ARQUITECTURA.iloc[60,6]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_25_3 = datos_ARQUITECTURA.iloc[60,12]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_REC_MUESTRAS_25_4 = datos_ARQUITECTURA.iloc[60,13]  # Reemplaza con los índices correspondientes


    ###############################################################################################
    ########################################### TOTAL  ###########################################
    ###############################################################################################

    ###############################################################################################
    ###############################################################################################

    return {
        'valor_ARQ_T1_REC_MUESTRAS_1_1' : valor_ARQ_T1_REC_MUESTRAS_1_1,
        'valor_ARQ_T1_REC_MUESTRAS_1_2' : valor_ARQ_T1_REC_MUESTRAS_1_2,
        'valor_ARQ_T1_REC_MUESTRAS_1_3' : valor_ARQ_T1_REC_MUESTRAS_1_3,
        
        'valor_ARQ_T1_REC_MUESTRAS_2_1' : valor_ARQ_T1_REC_MUESTRAS_2_1,
        'valor_ARQ_T1_REC_MUESTRAS_2_2' : valor_ARQ_T1_REC_MUESTRAS_2_2,
        'valor_ARQ_T1_REC_MUESTRAS_2_3' : valor_ARQ_T1_REC_MUESTRAS_2_3,

        'valor_ARQ_T1_REC_MUESTRAS_3_1' : valor_ARQ_T1_REC_MUESTRAS_3_1,
        'valor_ARQ_T1_REC_MUESTRAS_3_2' : valor_ARQ_T1_REC_MUESTRAS_3_2,
        'valor_ARQ_T1_REC_MUESTRAS_3_3' : valor_ARQ_T1_REC_MUESTRAS_3_3,

        'valor_ARQ_T1_REC_MUESTRAS_4_1' : valor_ARQ_T1_REC_MUESTRAS_4_1,
        'valor_ARQ_T1_REC_MUESTRAS_4_2' : valor_ARQ_T1_REC_MUESTRAS_4_2,
        'valor_ARQ_T1_REC_MUESTRAS_4_3' : valor_ARQ_T1_REC_MUESTRAS_4_3,

        'valor_ARQ_T1_REC_MUESTRAS_5_1' : valor_ARQ_T1_REC_MUESTRAS_5_1,
        'valor_ARQ_T1_REC_MUESTRAS_5_2' : valor_ARQ_T1_REC_MUESTRAS_5_2,
        'valor_ARQ_T1_REC_MUESTRAS_5_3' : valor_ARQ_T1_REC_MUESTRAS_5_3,

        'valor_ARQ_T1_REC_MUESTRAS_6_1' : valor_ARQ_T1_REC_MUESTRAS_6_1,
        'valor_ARQ_T1_REC_MUESTRAS_6_2' : valor_ARQ_T1_REC_MUESTRAS_6_2,
        'valor_ARQ_T1_REC_MUESTRAS_6_3' : valor_ARQ_T1_REC_MUESTRAS_6_3,

        'valor_ARQ_T1_REC_MUESTRAS_7_1' : valor_ARQ_T1_REC_MUESTRAS_7_1,
        'valor_ARQ_T1_REC_MUESTRAS_7_2' : valor_ARQ_T1_REC_MUESTRAS_7_2,

        'valor_ARQ_T1_REC_MUESTRAS_8_1' : valor_ARQ_T1_REC_MUESTRAS_8_1,
        'valor_ARQ_T1_REC_MUESTRAS_8_2' : valor_ARQ_T1_REC_MUESTRAS_8_2,

        'valor_ARQ_T1_REC_MUESTRAS_9_1' : valor_ARQ_T1_REC_MUESTRAS_9_1,
        'valor_ARQ_T1_REC_MUESTRAS_9_2' : valor_ARQ_T1_REC_MUESTRAS_9_2,

    ###############################################################################################
    ################################### CONOCIMIENTO Y SABERES ####################################
    ###############################################################################################

        'valor_ARQ_T1_REC_MUESTRAS_10_1' : valor_ARQ_T1_REC_MUESTRAS_10_1,
        'valor_ARQ_T1_REC_MUESTRAS_10_2' : valor_ARQ_T1_REC_MUESTRAS_10_2,
        'valor_ARQ_T1_REC_MUESTRAS_10_3' : valor_ARQ_T1_REC_MUESTRAS_10_3,
        'valor_ARQ_T1_REC_MUESTRAS_10_4' : valor_ARQ_T1_REC_MUESTRAS_10_4,

        'valor_ARQ_T1_REC_MUESTRAS_11_1' : valor_ARQ_T1_REC_MUESTRAS_11_1,
        'valor_ARQ_T1_REC_MUESTRAS_11_2' : valor_ARQ_T1_REC_MUESTRAS_11_2,
        'valor_ARQ_T1_REC_MUESTRAS_11_3' : valor_ARQ_T1_REC_MUESTRAS_11_3,
        'valor_ARQ_T1_REC_MUESTRAS_11_4' : valor_ARQ_T1_REC_MUESTRAS_11_4,

        'valor_ARQ_T1_REC_MUESTRAS_12_1' : valor_ARQ_T1_REC_MUESTRAS_12_1,
        'valor_ARQ_T1_REC_MUESTRAS_12_2' : valor_ARQ_T1_REC_MUESTRAS_12_2,
        'valor_ARQ_T1_REC_MUESTRAS_12_3' : valor_ARQ_T1_REC_MUESTRAS_12_3,
        'valor_ARQ_T1_REC_MUESTRAS_12_4' : valor_ARQ_T1_REC_MUESTRAS_12_4,

        'valor_ARQ_T1_REC_MUESTRAS_13_1' : valor_ARQ_T1_REC_MUESTRAS_13_1,
        'valor_ARQ_T1_REC_MUESTRAS_13_2' : valor_ARQ_T1_REC_MUESTRAS_13_2,
        'valor_ARQ_T1_REC_MUESTRAS_13_3' : valor_ARQ_T1_REC_MUESTRAS_13_3,
        'valor_ARQ_T1_REC_MUESTRAS_13_4' : valor_ARQ_T1_REC_MUESTRAS_13_4,

        'valor_ARQ_T1_REC_MUESTRAS_14_1' : valor_ARQ_T1_REC_MUESTRAS_14_1,
        'valor_ARQ_T1_REC_MUESTRAS_14_2' : valor_ARQ_T1_REC_MUESTRAS_14_2,
        'valor_ARQ_T1_REC_MUESTRAS_14_3' : valor_ARQ_T1_REC_MUESTRAS_14_3,
        'valor_ARQ_T1_REC_MUESTRAS_14_4' : valor_ARQ_T1_REC_MUESTRAS_14_4,

        'valor_ARQ_T1_REC_MUESTRAS_15_1' : valor_ARQ_T1_REC_MUESTRAS_15_1,
        'valor_ARQ_T1_REC_MUESTRAS_15_2' : valor_ARQ_T1_REC_MUESTRAS_15_2,
        'valor_ARQ_T1_REC_MUESTRAS_15_3' : valor_ARQ_T1_REC_MUESTRAS_15_3,
        'valor_ARQ_T1_REC_MUESTRAS_15_4' : valor_ARQ_T1_REC_MUESTRAS_15_4,

        'valor_ARQ_T1_REC_MUESTRAS_16_1' : valor_ARQ_T1_REC_MUESTRAS_16_1,
        'valor_ARQ_T1_REC_MUESTRAS_16_2' : valor_ARQ_T1_REC_MUESTRAS_16_2,
        'valor_ARQ_T1_REC_MUESTRAS_16_3' : valor_ARQ_T1_REC_MUESTRAS_16_3,
        'valor_ARQ_T1_REC_MUESTRAS_16_4' : valor_ARQ_T1_REC_MUESTRAS_16_4,

        'valor_ARQ_T1_REC_MUESTRAS_17_1' : valor_ARQ_T1_REC_MUESTRAS_17_1,
        'valor_ARQ_T1_REC_MUESTRAS_17_2' : valor_ARQ_T1_REC_MUESTRAS_17_2,
        'valor_ARQ_T1_REC_MUESTRAS_17_3' : valor_ARQ_T1_REC_MUESTRAS_17_3,
        'valor_ARQ_T1_REC_MUESTRAS_17_4' : valor_ARQ_T1_REC_MUESTRAS_17_4,

        'valor_ARQ_T1_REC_MUESTRAS_18_1' : valor_ARQ_T1_REC_MUESTRAS_18_1,
        'valor_ARQ_T1_REC_MUESTRAS_18_2' : valor_ARQ_T1_REC_MUESTRAS_18_2,
        'valor_ARQ_T1_REC_MUESTRAS_18_3' : valor_ARQ_T1_REC_MUESTRAS_18_3,
        'valor_ARQ_T1_REC_MUESTRAS_18_4' : valor_ARQ_T1_REC_MUESTRAS_18_4,

        'valor_ARQ_T1_REC_MUESTRAS_19_1' : valor_ARQ_T1_REC_MUESTRAS_19_1,
        'valor_ARQ_T1_REC_MUESTRAS_19_2' : valor_ARQ_T1_REC_MUESTRAS_19_2,
        'valor_ARQ_T1_REC_MUESTRAS_19_3' : valor_ARQ_T1_REC_MUESTRAS_19_3,
        'valor_ARQ_T1_REC_MUESTRAS_19_4' : valor_ARQ_T1_REC_MUESTRAS_19_4,

    ###############################################################################################
    ############################ EVIDENCIA DE PROYECTO  ###########################################
    ###############################################################################################

        'valor_ARQ_T1_REC_MUESTRAS_20_1' : valor_ARQ_T1_REC_MUESTRAS_20_1,
        'valor_ARQ_T1_REC_MUESTRAS_20_2' : valor_ARQ_T1_REC_MUESTRAS_20_2,
        'valor_ARQ_T1_REC_MUESTRAS_20_3' : valor_ARQ_T1_REC_MUESTRAS_20_3,
        'valor_ARQ_T1_REC_MUESTRAS_20_4' : valor_ARQ_T1_REC_MUESTRAS_20_4,

        'valor_ARQ_T1_REC_MUESTRAS_21_1' : valor_ARQ_T1_REC_MUESTRAS_21_1,
        'valor_ARQ_T1_REC_MUESTRAS_21_2' : valor_ARQ_T1_REC_MUESTRAS_21_2,
        'valor_ARQ_T1_REC_MUESTRAS_21_3' : valor_ARQ_T1_REC_MUESTRAS_21_3,
        'valor_ARQ_T1_REC_MUESTRAS_21_4' : valor_ARQ_T1_REC_MUESTRAS_21_4,

        'valor_ARQ_T1_REC_MUESTRAS_22_1' : valor_ARQ_T1_REC_MUESTRAS_22_1,
        'valor_ARQ_T1_REC_MUESTRAS_22_2' : valor_ARQ_T1_REC_MUESTRAS_22_2,
        'valor_ARQ_T1_REC_MUESTRAS_22_3' : valor_ARQ_T1_REC_MUESTRAS_22_3,
        'valor_ARQ_T1_REC_MUESTRAS_22_4' : valor_ARQ_T1_REC_MUESTRAS_22_4,

        'valor_ARQ_T1_REC_MUESTRAS_23_1' : valor_ARQ_T1_REC_MUESTRAS_23_1,
        'valor_ARQ_T1_REC_MUESTRAS_23_2' : valor_ARQ_T1_REC_MUESTRAS_23_2,
        'valor_ARQ_T1_REC_MUESTRAS_23_3' : valor_ARQ_T1_REC_MUESTRAS_23_3,
        'valor_ARQ_T1_REC_MUESTRAS_23_4' : valor_ARQ_T1_REC_MUESTRAS_23_4,

        'valor_ARQ_T1_REC_MUESTRAS_24_1' : valor_ARQ_T1_REC_MUESTRAS_24_1,
        'valor_ARQ_T1_REC_MUESTRAS_24_2' : valor_ARQ_T1_REC_MUESTRAS_24_2,
        'valor_ARQ_T1_REC_MUESTRAS_24_3' : valor_ARQ_T1_REC_MUESTRAS_24_3,
        'valor_ARQ_T1_REC_MUESTRAS_24_4' : valor_ARQ_T1_REC_MUESTRAS_24_4,

    ###############################################################################################
    ########################################### TOTAL  ###########################################
    ###############################################################################################

        'valor_ARQ_T1_REC_MUESTRAS_25_1' : valor_ARQ_T1_REC_MUESTRAS_25_1,
        'valor_ARQ_T1_REC_MUESTRAS_25_2' : valor_ARQ_T1_REC_MUESTRAS_25_2,
        'valor_ARQ_T1_REC_MUESTRAS_25_3' : valor_ARQ_T1_REC_MUESTRAS_25_3,
        'valor_ARQ_T1_REC_MUESTRAS_25_4' : valor_ARQ_T1_REC_MUESTRAS_25_4,

        }