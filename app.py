import streamlit as st
import math

st.title("calculadora de figuras")
option=st.selectbox(
  "¿Que figura deseas calcular?",
  ("Circulo","Triangulo","Rectangulo","Cuadrado"),
)
st.write("Eleccion:",option)
if option=circulo:
  radio = st.slider("selecciona el radio", 0.0, 10.0, 5.0)
  area=math.pi * radio**2
  perimetro=2*math.pi*radio
  col1, col2, col3 = st.columns(3)
col1.metric("Radio", "radio", "0")
col2.metric("Area", "area", "0")
col3.metric("Perimetro", "perimetro", "0")
