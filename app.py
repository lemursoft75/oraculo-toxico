import streamlit as st
import random
import base64

# Lista de predicciones
predicciones = [
    "Tu café se derramará justo cuando respondas ese correo importante.",
    "Hoy alguien confundirá tu esfuerzo con flojera. No será la última vez.",
    "Otro día solitario, aburrido y espantoso.",
    "Te llegará una factura que no sabías que existía. Spoiler: es tuya.",
    "El WiFi funcionará… hasta que tengas tu reunión más importante.",
    "El pan se te quemará, como tus esperanzas por ese aumento.",
    "Hoy te confundirán con alguien... que no cae bien.",
    "La impresora fallará solo cuando estés apurado.",
    "Hoy alguien te dirá “tenemos que hablar”... y no será por algo bueno.",
    "Lo estás haciendo horrible, ríndete.",
    "La alarma sonará... 15 minutos después de lo necesario.",
    "Subirás una historia sin darte cuenta del fondo comprometedor.",
    "El cajero automático decidirá que hoy no reconocerá tu tarjeta.",
    "Tendrás un día normal, es decir muy jodido.",
    "Hoy el semáforo se coordinará para detenerte en cada esquina.",
    "Seguirás de esclavo en tu jale culero, no sirves para emprender.",
    "Hoy te felicitarán por algo que no hiciste. Pero igual tendrás que arreglarlo.",
    "Alguien dirá “¿No te lo había comentado?”... sobre un cambio crucial.",
    "Pensarás en la persona equivocada justo cuando digan “habla ahora”.",
    "Harás una compra innecesaria… y lo sabrás justo después de pagar.",
    "Tus sospechas serán ciertas, eres un loser.",
    "Alguien pensará que te puede pagar con “exposición”.",
    "Tu comida llegará… fría y tarde. Igual te cobrarán doble.",
    "Hoy la copia de seguridad no se habrá guardado… porque “algo falló”.",
    "Pensarás que te llaman para agradecerte… y será para pedirte algo.",
    "Tu crush sabe que le gustas, y siente asco.",
    "Hoy el clima será contradictorio, como tus decisiones financieras.",
    "Intentarás descansar… justo cuando comiencen las obras cerca de tu casa.",
    "Alguien dirá “no fue para tanto”… sobre algo que te costó años.",
    "Hoy te cruzarás con tu ex… justo después de tropezar."
]

# Función para reproducir audio en autoplay usando base64
def reproducir_audio_autoplay(ruta):
    with open(ruta, "rb") as audio_file:
        audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
            <audio autoplay>
                <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg" />
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# Configuración de página
st.set_page_config(page_title="Oráculo Tóxico", layout="centered")
st.title("🎮 El Oráculo Tóxico")
st.subheader("🧙 El Maestro Zervantes te revela tu destino")
st.markdown("<h4 style='text-align: center;'>By Xibalbá Games</h4>", unsafe_allow_html=True)

# Botón rojo con estilo personalizado
button_style = """
    <style>
    div.stButton > button:first-child {
        background-color: #990000;
        color: white;
        border: none;
        padding: 0.75em 1.5em;
        font-weight: bold;
        font-size: 1em;
        border-radius: 10px;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

if st.button("Consultar el destino"):
    mensaje = random.choice(predicciones)
    st.markdown(f"<h3 style='color:#cc0000'>{mensaje}</h3>", unsafe_allow_html=True)
    st.image("static/images/lemur.gif", caption="El universo te responde...", use_container_width=True)
    reproducir_audio_autoplay("static/audio/risa.mp3")
