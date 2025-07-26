import streamlit as st
import random
import base64

# Lista de predicciones
predicciones = [
    "Hoy como de costumbre la vas a cagar.",
    "Descubrirás que sirves para algo, para dar cringe.",
    "Otro día solitario, aburrido y espantoso.",
    "Seguirás echándole ganas...y fallando cada vez mas.",
    "Al mirarte hoy al espejo, te verás mas acabado y rancio.",
    "Pensarás en lo que haz hecho con tu vida, un desperdicio de años.",
    "Hoy como todos los días serás invisible e innecesario.",
    "Tendrás otra genial idea que jamas vas a implementar.",
    "Hoy alguien te dirá -Te amo- y justo cuando le respondas despertarás.",
    "Lo estás haciendo horrible, ríndete.",
    "Todo el resto del año vas a seguir siendo inútil.",
    "Descubrirás que tienes talento para cosas absolutamente innecesarias.",
    "El cajero automático te mostrara mas ceros, a la izquierda.",
    "Tendrás un día normal, es decir muy jodido.",
    "Vas a ser noticia en tu jale, tus días en la empresa están contados.",
    "Seguirás de esclavo en tu jale culero, no sirves para emprender.",
    "Hoy empezaras una nueva vida, con menos porvenir que la anterior.",
    "Estas a punto de lograrlo, superar tu record de días seguidos sin lograr nada.",
    "¡¡ESTAS DE SUERTE!! pide un deseo y te lo concederé.",
    "Lo estas haciendo genial, eres el ejemplo perfecto del fracaso.",
    "Tus sospechas serán ciertas, eres un farsante y te van a descubrir.",
    "Eso que creías que hacías muy bien en realidad era pura suerte.",
    "Quedate tranquilo el Universo no te odia, todo lo malo te pasa por imbécil.",
    "Estas demasiado joven para quejarte y demasiado viejo para soñar”.",
    "Solo le caes bien a pura gente mierda, y hasta ellos te ignoran.",
    "Tu crush sabe que la stalkeas, y siente asco.",
    "Tu máximo logro de hoy será no convertirte en indigente todavía.",
    "Ponte a jalar en lugar de estar jugando esta madre, por eso no progresas.",
    "Vas a comprar eso que tanto querías y después te vas a arrepentir.",
    "Hoy será un dia grandioso para todos excepto para tí."
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

# 🧨 Fondo macabro personalizado
fondo_macabro = """
<style>
body {
    background-image: url("/static/images/fondo.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""
st.markdown(fondo_macabro, unsafe_allow_html=True)


# 🧟 Configuración de página
st.set_page_config(page_title="Oráculo Tóxico", layout="centered")
st.title("🎮 El Oráculo Tóxico")
st.subheader("🧙 El Maestro Zervantes te revela tu destino")
st.markdown("<h4 style='text-align: center;'>By Xibalbá Games</h4>", unsafe_allow_html=True)

# ⚠️ Instructivo inicial
st.markdown("""
<div style='background-color:rgba(0,0,0,0.7); padding:1em; border-radius:10px; color:white; font-size:1.1em'>
<b>Instrucciones:</b><br>
Si en tu <i>primer intento</i> aparece la predicción <b style='color:#00ccff'>“¡¡ESTAS DE SUERTE!! pide un deseo y te lo concederé.”</b><br>
Tu deseo se cumplirá sin consecuencias…<br>
Pero si fallas, <b>todo lo que el Maestro Zervantes decrete en cada intento será inevitable.</b><br>
<b>Juega si te atreves.</b>
</div>
""", unsafe_allow_html=True)

# 🔴 Botón rojo personalizado
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

def reproducir_audio_fondo_autoplay(ruta):
    with open(ruta, "rb") as audio_file:
        audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
        <audio autoplay loop>
            <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg" />
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)


# 🎶 Música de fondo al abrir la app
reproducir_audio_fondo_autoplay("static/audio/fondo.mp3")


# 📤 Botón de consulta
if st.button("Consultar el destino"):
    mensaje = random.choice(predicciones)
    if "ESTAS DE SUERTE" in mensaje.upper():
        st.markdown(f"<h3 style='color:#00ccff'>{mensaje}</h3>", unsafe_allow_html=True)
        st.success("¡Tu deseo será concedido! Escoge bien...")
    else:
        st.markdown(f"<h3 style='color:#cc0000'>{mensaje}</h3>", unsafe_allow_html=True)
    st.image("static/images/lemur.gif", caption="El universo te responde...", use_container_width=True)
    reproducir_audio_autoplay("static/audio/risa.mp3")
