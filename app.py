#librerias que se utilizaran
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon
from matplotlib.patches import Rectangle
import streamlit as st
import math
import numpy as np
#nombre de la aplicacion en pantalla e informacion del autor
st.title("calculadora de figuras y funciones")
st.sidebar.write("alan manuel lopez garcia 377341")
#caja seleccionadora de las distintas funciones qu eofrece la app
option=st.selectbox(
    "¿Que figura deseas calcular?",
("Circulo","Triangulo","Rectangulo","Cuadrado","sen, cos, tan"),
  )
st.write("Eleccion:",option)
#solicitar un radio para realizar los calculos
if option=="Circulo":
    radio = st.slider("selecciona el radio", 0.0, 10.0, 5.0)
    area1=math.pi * radio**2
    perimetro1=2*math.pi*radio
    #mostrara los datos en pantalla
    col1, col2, col3 = st.columns(3)
    col1.metric("Radio", radio, "0")
    col2.metric("Area", area1, "0")
    col3.metric("Perimetro", perimetro1, "0")
  
    color = st.color_picker("Pick A Color", "#00f900")
    st.write("The current color is", color)
# 1. Crea una figura y un eje
    fig, ax = plt.subplots()

# 2. Crea un círculo. 
# Parámetros: centro (x, y) y radio (radius)
# fill=False para que solo dibuje el borde
    circle = patches.Circle((0.0, 0.0), radio, color=color, fill=False)

# 3. Añade el parche del círculo al eje
    ax.add_artist(circle)
    ax.set_aspect('equal')
    ax.set_xlim(-radio - 1, radio + 1)
    ax.set_ylim(-radio - 1, radio + 1)

# Mostrar en Streamlit
    st.pyplot(fig)
    plt.close(fig)
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
  
    color = st.color_picker("Pick A Color", "#00f900")
    st.write("The current color is", color)
    # Coordenadas del triángulo
    A = (0, 0)
    B = (base, 0)
    C = (base / 2, altura)
    fig, ax = plt.subplots()
    triangulo = Polygon([A, B, C], closed=True, edgecolor=color, facecolor='none', linewidth=2)
    ax.add_patch(triangulo)
    padding = max(base, altura) * 0.2
    ax.set_xlim(-padding, base + padding)
    ax.set_ylim(-padding, altura + padding)
    ax.set_aspect('equal')
    ax.axis('off') # Opcional: oculta los ejes

# Mostrar en Streamlit
    st.pyplot(fig)
    plt.close(fig)
#se uso if para que al momento de elegir una funcion u opcion en la caja de opciones solo muestre lo requerido
if option=="Rectangulo":
    base = st.slider("seleccione la longitud de la base", 0.0, 10.0, 5.0) 
    altura= st.slider("seleccione la altura", 0.0, 10.0, 5.0)
    area3=base*altura
    perimetro3=2*(base+altura)
    col6, col7 = st.columns(2)
    col6.metric("perimetro", perimetro3, "0")
    col7.metric("Area", area3, "0")
  
    color = st.color_picker("Pick A Color", "#00f900")
    st.write("The current color is", color)
    fig, ax = plt.subplots()
    rectangulo = Rectangle((0, 0), base, altura, edgecolor=color, facecolor='none', linewidth=2)
    ax.add_patch(rectangulo)

# Ajustes del gráfico
    padding = altura * 0.2
    ax.set_xlim(-padding, base + padding)
    ax.set_ylim(-padding, altura + padding)
    ax.set_aspect('equal')
    ax.axis('off')  # Opcional: oculta ejes

    st.pyplot(fig)
    plt.close(fig)
elif option=="Cuadrado":
    lado=st.slider("longitud de un lado",0.0, 10.0, 5.0)
    area4=lado**2
    Perimetro4=4*lado
    col8, col9 = st.columns(2)
    col8.metric("perimetro", Perimetro4, "0")
    col9.metric("Area", area4, "0")

    color = st.color_picker("Pick A Color", "#00f900")
    st.write("The current color is", color)
    fig, ax = plt.subplots()
    cuadrado = Rectangle((0, 0), lado, lado, edgecolor=color, facecolor='none', linewidth=2)
    ax.add_patch(cuadrado)

# Ajustes del gráfico
    padding = lado * 0.2
    ax.set_xlim(-padding, lado + padding)
    ax.set_ylim(-padding, lado + padding)
    ax.set_aspect('equal')
    ax.axis('off')  # Opcional: oculta ejes

    st.pyplot(fig)
    plt.close(fig)
if option=="sen, cos, tan":
    radio = st.slider("selecciona el rango", 0.0, 2*math.pi, math.pi)
    st.title("Visualizador de funciones trigonométricas (en radianes)")

# Slider para ángulo individual en radianes
    angulo = st.slider("Selecciona un ángulo (radianes)", 0.0, 2 * np.pi, np.pi / 4, step=0.01, format="%.2f")

# Mostrar valores trigonométricos
    st.markdown(f"**Seno({angulo:.2f} rad):** {np.sin(angulo):.2f}")
    st.markdown(f"**Coseno({angulo:.2f} rad):** {np.cos(angulo):.2f}")
    try:
        tan = np.tan(angulo)
        tan_str = f"{tan:.2f}" if abs(tan) < 100 else "Infinito (aproximado)"
    except:
        tan_str = "Infinito"
    st.markdown(f"**Tangente({angulo:.2f} rad):** {tan_str}")

# --- Rango del gráfico ---
    st.subheader("Rango del gráfico (eje X)")
    inicio = st.slider("Inicio del rango (radianes)", 0.0, 2*np.pi, 0.0, step=0.1, format="%.2f")
    fin = st.slider("Fin del rango (radianes)", 0.0, 2*np.pi, 2*np.pi, step=0.1, format="%.2f")

# Validar que inicio < fin
    if inicio >= fin:
        st.error("⚠️ El valor de inicio debe ser menor que el de fin.")
    else:
    # Crear valores para X en el rango elegido
        x = np.linspace(inicio, fin, 1000)

    # Crear gráfica
    fig, ax = plt.subplots(figsize=(10, 4))

    # Graficar funciones
    ax.plot(x, np.sin(x), label="Seno", color='red')
    ax.plot(x, np.cos(x), label="Coseno", color='blue')
    ax.plot(x, np.tan(x), label="Tangente", color='green')

    # Línea vertical para ángulo actual
    ax.axvline(x=angulo, color='gray', linestyle='--', alpha=0.6, label=f"Ángulo: {angulo:.2f} rad")

    # Limitar eje Y por la tangente
    ax.set_ylim(-5, 5)

    ax.set_xlabel("Ángulo (radianes)")
    ax.set_ylabel("Valor")
    ax.set_title("Seno, Coseno y Tangente")
    ax.grid(True)
    ax.legend()

    # Mostrar gráfico
    st.pyplot(fig)
    plt.close(fig)
