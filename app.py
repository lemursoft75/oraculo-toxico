import streamlit as st
import random
import base64

# Lista de predicciones humorísticas
import streamlit as st
import random

# Lista de predicciones
predicciones = [
    "Tu café se derramará justo cuando respondas ese correo importante.",
    "Hoy alguien confundirá tu esfuerzo con flojera. No será la última vez.",
    "Recibirás un mensaje… no de quien esperas. Y será spam.",
    "Te llegará una factura que no sabías que existía. Spoiler: es tuya.",
    "El WiFi funcionará… hasta que tengas tu reunión más importante.",
    "El pan se te quemará, como tus esperanzas por ese aumento.",
    "Hoy te confundirán con alguien... que no cae bien.",
    "La impresora fallará solo cuando estés apurado.",
    "Hoy alguien te dirá “tenemos que hablar”... y no será por algo bueno.",
    "Buscarás las llaves por 20 minutos. Estaban en tu mano.",
    "La alarma sonará... 15 minutos después de lo necesario.",
    "Subirás una historia sin darte cuenta del fondo comprometedor.",
    "El cajero automático decidirá que hoy no reconocerá tu tarjeta.",
    "Enviarás el mensaje equivocado... al grupo equivocado.",
    "Hoy el semáforo se coordinará para detenerte en cada esquina.",
    "Tu celular caerá… en cámara lenta… sin funda.",
    "Hoy te felicitarán por algo que no hiciste. Pero igual tendrás que arreglarlo.",
    "Alguien dirá “¿No te lo había comentado?”... sobre un cambio crucial.",
    "Pensarás en la persona equivocada justo cuando digan “habla ahora”.",
    "Harás una compra innecesaria… y lo sabrás justo después de pagar.",
    "Hoy aprenderás que “modo avión” no arregla emociones.",
    "Alguien pensará que te puede pagar con “exposición”.",
    "Tu comida llegará… fría y tarde. Igual te cobrarán doble.",
    "Hoy la copia de seguridad no se habrá guardado… porque “algo falló”.",
    "Pensarás que te llaman para agradecerte… y será para pedirte algo.",
    "Te saludarán como si te conocieran… pero tú no sabrás quién es.",
    "Hoy el clima será contradictorio, como tus decisiones financieras.",
    "Intentarás descansar… justo cuando comiencen las obras cerca de tu casa.",
    "Alguien dirá “no fue para tanto”… sobre algo que te costó años.",
    "Hoy te cruzarás con tu ex… justo después de tropezar."
]

# Configuración
st.set_page_config(page_title="Oráculo Tóxico", layout="centered")
st.title("🔮 Tu tragedia del día")

# Botón
if st.button("Consultar el destino"):
    mensaje = random.choice(predicciones)
    st.markdown(f"### {mensaje}")
    st.image("static/images/lemur.gif", caption="El universo te responde...", use_container_width=True)

    # Truco con HTML + autoplay
    audio_autoplay = """
    <audio autoplay>
        <source src="static/audio/risa.mp3" type="audio/mpeg">
    </audio>
    """
    st.markdown(audio_autoplay, unsafe_allow_html=True)
