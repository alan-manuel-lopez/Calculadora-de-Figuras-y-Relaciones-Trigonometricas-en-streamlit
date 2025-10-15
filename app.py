import streamlit as st
import math
st.title("calculadora de figuras")
st.sidebar.write("alan manuel lopez garcia")
option=st.selectbox(
  "¿Que figura deseas calcular?",
  ("Circulo","Triangulo","Rectangulo","Cuadrado"),
)
st.write("Eleccion:",option)
#solicitar un radio
if option=="Circulo":
  radio = st.slider("selecciona el radio", 0.0, 10.0, 5.0)
  area1=math.pi * radio**2
  perimetro1=2*math.pi*radio
  col1, col2, col3 = st.columns(3)
  col1.metric("Radio", radio, "0")
  col2.metric("Area", area1, "0")
  col3.metric("Perimetro", perimetro1, "0")
  import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# 1. Crear una figura y un eje
fig, ax = plt.subplots()

# 2. Crear el objeto círculo
#    - El primer argumento es la coordenada del centro (x, y).
#    - El argumento 'radius' define el tamaño.
#    - 'fill=False' lo dibuja solo como un contorno.
  circulo = Circle((0, 0), radius=radio, fill=False, color='blue')

# 3. Añadir el círculo al eje
  ax.add_patch(circulo)

# 4. Establecer los límites para asegurar que el círculo sea visible
  ax.set_xlim(-6, 6)
  ax.set_ylim(-6, 6)

# 5. Asegurar que la relación de aspecto sea igual (para que no se vea como una elipse)
  ax.set_aspect('equal')

# 6. Mostrar el gráfico
  plt.show()
if option=="Triangulo":
# Solicitar al usuario la base y la altura
  base = st.slider("seleccione la longitud de la base", 0.0, 10.0, 5.0) 
  altura= st.slider("seleccione la altura", 0.0, 10.0, 5.0)
  a=st.slider("longiutd de a", 0.0, 10.0, 5.0) 
  b=st.slider("longiutd de b", 0.0, 10.0, 5.0) 
  c=base
  Perimetro2=a+b+c
# Calcular y mostrar el área
  area2 = base*altura*0.5
  col4, col5 = st.columns(2)
  col4.metric("perimetro", Perimetro2, "0")
  col5.metric("Area", area2, "0")
elif option=="Rectangulo":
  base = st.slider("seleccione la longitud de la base", 0.0, 10.0, 5.0) 
  altura= st.slider("seleccione la altura", 0.0, 10.0, 5.0)
  area3=base*altura
  perimetro3=2*(base+altura)
  col6, col7 = st.columns(2)
  col6.metric("perimetro", perimetro3, "0")
  col7.metric("Area", area3, "0")
elif option=="Cuadrado":
  lado=st.slider("longitud de un lado",0.0, 10.0, 5.0)
  area4=lado**2
  Perimetro4=4*lado
  col8, col9 = st.columns(2)
  col8.metric("perimetro", Perimetro4, "0")
  col9.metric("Area", area4, "0")
