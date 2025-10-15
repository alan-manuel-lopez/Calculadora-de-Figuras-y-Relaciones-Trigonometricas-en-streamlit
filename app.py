import streamlit as st
import math

st.title("calculadora de figuras")
option=st.selectbox(
  "¿Que figura deseas calcular?",
  ("Circulo","Triangulo","Rectangulo","Cuadrado"),
)
st.write("Eleccion:",option)
