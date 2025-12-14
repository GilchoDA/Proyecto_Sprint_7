import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Vehicles Dashboard", layout="wide")

st.header("Cuadro de mandos: anuncios de venta de coches")

# Cargar datos
car_data = pd.read_csv('F:/TRIPLETEN/SPRINT 07/Proyecto Sprint 07/Proyecto_Sprint_7/vehicles_us.csv')

st.write("Vista previa del conjunto de datos:")
st.dataframe(car_data.head(10))

st.divider()

# Botón: Histograma
hist_button = st.button("Construir histograma (odometer)")

if hist_button:
    st.write("Creación de un histograma para el kilometraje (odometer).")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón: Dispersión
scatter_button = st.button("Construir gráfico de dispersión (odometer vs price)")

if scatter_button:
    st.write("Creación de un gráfico de dispersión: kilometraje (odometer) vs precio (price).")
    fig_scatter = px.scatter(car_data, x="odometer", y="price", opacity=0.4)
    st.plotly_chart(fig_scatter, use_container_width=True)