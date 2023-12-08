def T1_Hidraulica():
    """
    Muestra la información correspondiente a la fase 3.
    Lee el contenido de T1_Hidraulica.html y lo renderiza en la plantilla 'T1_Hidraulica.html'.
    """
    with open('templates/T1_Hidraulica.html', 'r') as T1_Hidraulica_file:
        T1_Hidraulica_html = T1_Hidraulica_file.read()

        # Suponiendo que 'datos_TIME' es un DataFrame que contiene la información necesaria
    valor_ARQ_T1_HIDRAULICA_1_1 = datos_ARQUITECTURA.iloc[8,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_1_2 = datos_ARQUITECTURA.iloc[8,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_1_3 = datos_ARQUITECTURA.iloc[8,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_HIDRAULICA_2_1 = datos_ARQUITECTURA.iloc[9,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_2_2 = datos_ARQUITECTURA.iloc[9,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_2_3 = datos_ARQUITECTURA.iloc[9,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_HIDRAULICA_3_1 = datos_ARQUITECTURA.iloc[10,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_3_2 = datos_ARQUITECTURA.iloc[10,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_3_3 = datos_ARQUITECTURA.iloc[10,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_HIDRAULICA_4_1 = datos_ARQUITECTURA.iloc[11,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_4_2 = datos_ARQUITECTURA.iloc[11,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_4_3 = datos_ARQUITECTURA.iloc[11,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_HIDRAULICA_5_1 = datos_ARQUITECTURA.iloc[12,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_5_2 = datos_ARQUITECTURA.iloc[12,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_5_3 = datos_ARQUITECTURA.iloc[12,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_HIDRAULICA_6_1 = datos_ARQUITECTURA.iloc[13,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_6_2 = datos_ARQUITECTURA.iloc[13,5]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_6_3 = datos_ARQUITECTURA.iloc[13,6]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_HIDRAULICA_7_1 = datos_ARQUITECTURA.iloc[14,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_7_2 = datos_ARQUITECTURA.iloc[14,5]  # Reemplaza con los índices correspondientes

    valor_ARQ_T1_HIDRAULICA_8_1 = datos_ARQUITECTURA.iloc[15,4]  # Reemplaza con los índices correspondientes
    valor_ARQ_T1_HIDRAULICA_8_2 = datos_ARQUITECTURA.iloc[15,5]  # Reemplaza con los índices correspondientes

    return render_template('T1_Hidraulica.html', 
                           valor_ARQ_T1_HIDRAULICA_1_1 = valor_ARQ_T1_HIDRAULICA_1_1,
                           valor_ARQ_T1_HIDRAULICA_1_2 = valor_ARQ_T1_HIDRAULICA_1_2,
                           valor_ARQ_T1_HIDRAULICA_1_3 = valor_ARQ_T1_HIDRAULICA_1_3,
                          
                           valor_ARQ_T1_HIDRAULICA_2_1 = valor_ARQ_T1_HIDRAULICA_2_1,
                           valor_ARQ_T1_HIDRAULICA_2_2 = valor_ARQ_T1_HIDRAULICA_2_2,
                           valor_ARQ_T1_HIDRAULICA_2_3 = valor_ARQ_T1_HIDRAULICA_2_3,

                           valor_ARQ_T1_HIDRAULICA_3_1 = valor_ARQ_T1_HIDRAULICA_3_1,
                           valor_ARQ_T1_HIDRAULICA_3_2 = valor_ARQ_T1_HIDRAULICA_3_2,
                           valor_ARQ_T1_HIDRAULICA_3_3 = valor_ARQ_T1_HIDRAULICA_3_3,

                           valor_ARQ_T1_HIDRAULICA_4_1 = valor_ARQ_T1_HIDRAULICA_4_1,
                           valor_ARQ_T1_HIDRAULICA_4_2 = valor_ARQ_T1_HIDRAULICA_4_2,
                           valor_ARQ_T1_HIDRAULICA_4_3 = valor_ARQ_T1_HIDRAULICA_4_3,

                           valor_ARQ_T1_HIDRAULICA_5_1 = valor_ARQ_T1_HIDRAULICA_5_1,
                           valor_ARQ_T1_HIDRAULICA_5_2 = valor_ARQ_T1_HIDRAULICA_5_2,
                           valor_ARQ_T1_HIDRAULICA_5_3 = valor_ARQ_T1_HIDRAULICA_5_3,

                           valor_ARQ_T1_HIDRAULICA_6_1 = valor_ARQ_T1_HIDRAULICA_6_1,
                           valor_ARQ_T1_HIDRAULICA_6_2 = valor_ARQ_T1_HIDRAULICA_6_2,
                           valor_ARQ_T1_HIDRAULICA_6_3 = valor_ARQ_T1_HIDRAULICA_6_3,
                           valor_ARQ_T1_HIDRAULICA_7_1 = valor_ARQ_T1_HIDRAULICA_7_1,
                           valor_ARQ_T1_HIDRAULICA_7_2 = valor_ARQ_T1_HIDRAULICA_7_2,

                           valor_ARQ_T1_HIDRAULICA_8_1 = valor_ARQ_T1_HIDRAULICA_8_1,
                           valor_ARQ_T1_HIDRAULICA_8_2 = valor_ARQ_T1_HIDRAULICA_8_2,

                           T1_Hidraulica=T1_Hidraulica_html)