# Importar las bibliotecas necesarias
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

# Importar la función desde el otro archivo
from T1_Trimestre import FUNCTION_T1

# Función para crear el diagrama de barras
def FUNCTION_GRAPH_1(datos_TIME):
    # Obtener los valores de las variables
    valor_TIME_T1_HIDRAULICA_1 = datos_TIME.iloc[187, 2]
    valor_TIME_T1_REC_MUESTRAS_1 = datos_TIME.iloc[188, 2]
    valor_TIME_T1_INGLES_1 = datos_TIME.iloc[189,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_MATEMATICAS_1 = datos_TIME.iloc[190,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_BIOLOGIA_1 = datos_TIME.iloc[191,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMUNICACION_1 = datos_TIME.iloc[192,2]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_LOGISTICA_1 = datos_TIME.iloc[193,2]  # Reemplaza con los índices correspondientes

    valor_TIME_T1_HIDRAULICA_3 = datos_TIME.iloc[187,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_REC_MUESTRAS_3 = datos_TIME.iloc[188,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_INGLES_3 = datos_TIME.iloc[189,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_MATEMATICAS_3 = datos_TIME.iloc[190,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_BIOLOGIA_3 = datos_TIME.iloc[191,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMUNICACION_3 = datos_TIME.iloc[192,4]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_LOGISTICA_3 = datos_TIME.iloc[193,4]  # Reemplaza con los índices correspondientes

 # Crear un DataFrame para Horas de Formación Directa
    df1 = pd.DataFrame({
        "Competencia": ["Hidráulica", "Recolección de Muestras", "Inglés", "Matemáticas", "Biología","Comunicación","Logística, Costos e Inventarios" ],
        "Horas de formación directa [FD]": [valor_TIME_T1_HIDRAULICA_1, valor_TIME_T1_REC_MUESTRAS_1,
                                       valor_TIME_T1_INGLES_1, valor_TIME_T1_MATEMATICAS_1,
                                       valor_TIME_T1_BIOLOGIA_1, valor_TIME_T1_COMUNICACION_1,
                                       valor_TIME_T1_LOGISTICA_1]
    })

    # Crear un DataFrame para Horas de Formación Autónoma
    # Asegúrate de obtener los valores correctos para las Horas de Formación Autónoma
    df3 = pd.DataFrame({
        "Competencia": ["Hidráulica", "Recolección de Muestras", "Inglés", "Matemáticas", "Biología","Comunicación","Logística, Costos e Inventarios" ],
        "Horas de formación autónoma [FA]": [valor_TIME_T1_HIDRAULICA_3, valor_TIME_T1_REC_MUESTRAS_3,
                                        valor_TIME_T1_INGLES_3, valor_TIME_T1_MATEMATICAS_3,
                                        valor_TIME_T1_BIOLOGIA_3, valor_TIME_T1_COMUNICACION_3,
                                        valor_TIME_T1_LOGISTICA_3]
    })


        # Llamar a create_bar_chart con df1 y df2
    components_bar_chart = create_bar_chart(df1, df3)
    #components_pie_chart = create_bar_chart(df2, df4)

    return components_bar_chart 
#components_pie_chart

def create_bar_chart(df1, df3):
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Horas de Formación Directa [FD]", "Horas de Formación Autónoma [FA]"))

    fig.add_trace(
        go.Bar(
            x=df1["Competencia"],
            y=df1["Horas de formación directa [FD]"],
            marker_color=['#6BA7CE', '#6BA7CE','#EC6605','#BCB8B6', '#BCB8B6', '#BCB8B6', '#3E9494'],
            text=df1["Horas de formación directa [FD]"],
            textposition='auto'
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(
            x=df3["Competencia"],
            y=df3["Horas de formación autónoma [FA]"],
            marker_color=['#6BA7CE', '#6BA7CE','#EC6605','#BCB8B6', '#BCB8B6', '#BCB8B6', '#3E9494'],
            text=df3["Horas de formación autónoma [FA]"],
            textposition='auto'
        ),
        row=1, col=2
    )

    fig.update_layout(
        autosize=False,
        width=1600,
        height=500,
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
            pad=4
        ),
        paper_bgcolor="LightSteelBlue",
    )


    return pio.to_html(fig, full_html=False)


# Función para crear el diagrama de barras
def FUNCTION_GRAPH_2(datos_TIME):
    # Obtener los valores de las variables
    valor_TIME_T1_HIDRAULICA_2 = datos_TIME.iloc[187,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_HIDRAULICA_2 = round(valor_TIME_T1_HIDRAULICA_2, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_REC_MUESTRAS_2 = datos_TIME.iloc[188,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_REC_MUESTRAS_2 = round(valor_TIME_T1_REC_MUESTRAS_2, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_INGLES_2 = datos_TIME.iloc[189,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_INGLES_2 = round(valor_TIME_T1_INGLES_2, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_MATEMATICAS_2 = datos_TIME.iloc[190,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_MATEMATICAS_2 = round(valor_TIME_T1_MATEMATICAS_2, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_BIOLOGIA_2 = (datos_TIME.iloc[191,3])*100  # Reemplaza con los índices correspondientes
    valor_TIME_T1_BIOLOGIA_2 = "{:.3}".format(valor_TIME_T1_BIOLOGIA_2)  # Redondear a 2 decimales

    valor_TIME_T1_COMUNICACION_2 = datos_TIME.iloc[192,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMUNICACION_2 = round(valor_TIME_T1_COMUNICACION_2, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_LOGISTICA_2 = datos_TIME.iloc[193,3]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_LOGISTICA_2 = round(valor_TIME_T1_LOGISTICA_2, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_HIDRAULICA_4 = datos_TIME.iloc[187,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_HIDRAULICA_4 = round(valor_TIME_T1_HIDRAULICA_4, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_REC_MUESTRAS_4 = datos_TIME.iloc[188,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_REC_MUESTRAS_4 = round(valor_TIME_T1_REC_MUESTRAS_4, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_INGLES_4 = datos_TIME.iloc[189,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_INGLES_4 = round(valor_TIME_T1_INGLES_4, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_MATEMATICAS_4 = datos_TIME.iloc[190,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_MATEMATICAS_4 = round(valor_TIME_T1_MATEMATICAS_4, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_BIOLOGIA_4 = datos_TIME.iloc[191,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_BIOLOGIA_4 = round(valor_TIME_T1_BIOLOGIA_4, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_COMUNICACION_4 = datos_TIME.iloc[192,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_COMUNICACION_4 = round(valor_TIME_T1_COMUNICACION_4, 2)*100  # Redondear a 2 decimales

    valor_TIME_T1_LOGISTICA_4 = datos_TIME.iloc[193,5]  # Reemplaza con los índices correspondientes
    valor_TIME_T1_LOGISTICA_4 = round(valor_TIME_T1_LOGISTICA_4, 2)*100  # Redondear a 2 decimales

 # Crear un DataFrame para Horas de Formación Directa
    df2 = pd.DataFrame({
        "Competencia": ["Hidráulica", "Recolección de Muestras", "Inglés", "Matemáticas", "Biología","Comunicación","Logística, Costos e Inventarios" ],
        "Horas de formación directa [FD]": [valor_TIME_T1_HIDRAULICA_2, valor_TIME_T1_REC_MUESTRAS_2,
                                        valor_TIME_T1_INGLES_2, valor_TIME_T1_MATEMATICAS_2,
                                        valor_TIME_T1_BIOLOGIA_2, valor_TIME_T1_COMUNICACION_2,
                                        valor_TIME_T1_LOGISTICA_2]
    })

    df4 = pd.DataFrame({
        "Competencia": ["Hidráulica", "Recolección de Muestras", "Inglés", "Matemáticas", "Biología","Comunicación","Logística, Costos e Inventarios" ],
        "Horas de formación autónoma [FA]": [valor_TIME_T1_HIDRAULICA_4, valor_TIME_T1_REC_MUESTRAS_4,
                                       valor_TIME_T1_INGLES_4, valor_TIME_T1_MATEMATICAS_4,
                                       valor_TIME_T1_BIOLOGIA_4, valor_TIME_T1_COMUNICACION_4,
                                       valor_TIME_T1_LOGISTICA_4]
    })


    components_pie_chart = create_pie_chart(df2, df4)

    return components_pie_chart

def create_pie_chart(df2, df4):
        # Define los colores que deseas usar
    colors = ['#6BA7CE', '#6BA7CE', '#EC6605', '#BCB8B6', '#BCB8B6', '#BCB8B6', '#3E9494']

    fig_2 = make_subplots(rows=1, cols=2, specs=[[{'type':'pie'}, {'type':'pie'}]], subplot_titles=("Porcentaje de formación directa [FD]", "Porcentaje de formación Autónoma [FA]"))

    fig_2.add_trace(
        go.Pie(labels=df2["Competencia"], values=df2["Horas de formación directa [FD]"], marker=dict(colors=colors)),
        1, 1
    )

    fig_2.add_trace(
        go.Pie(labels=df4["Competencia"], values=df4["Horas de formación autónoma [FA]"], marker=dict(colors=colors)),
        1, 2
    )

    fig_2.update_traces(hole=0.4, hoverinfo="label+percent+name")

    fig_2.update_layout(
        autosize=False,
        width=1000,
        height=600,
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
            pad=4
        ),
        paper_bgcolor="LightSteelBlue",
    )

    return pio.to_html(fig_2, full_html=False)