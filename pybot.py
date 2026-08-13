# ==============================================================================
# PROYECTO ACADÉMICO: CHATBOT CON IA Y PROCESAMIENTO DE LENGUAJE NATURAL (PLN)
# NOMBRE DEL PRODUCTO: PyBot
# LENGUAJE: Python 3
# LICENCIA: MIT (software libre, sin restricciones de autor para uso académico)
# ==============================================================================
#
# DESCRIPCIÓN GENERAL DEL PROYECTO
# ------------------------------------------------------------------------------
# PyBot es un "agente inteligente basado en reglas" (Rule-Based AI Agent), un
# tipo de Inteligencia Artificial simbólica que NO utiliza redes neuronales ni
# modelos entrenados con datos masivos, sino un sistema experto de reconocimiento
# de patrones y una Base de Conocimiento (Knowledge Base) predefinida[cite: 1].
#
# El "Procesamiento de Lenguaje Natural" (PLN / NLP) que aplica este programa
# consiste en:
#   1. Normalización de texto (quitar tildes, mayúsculas, signos de puntuación)[cite: 1].
#   2. Búsqueda de coincidencias de palabras clave (keyword matching)[cite: 1].
#   3. Selección de la mejor coincidencia (la palabra clave más larga/específica)[cite: 1].
#   4. Generación de una respuesta fija, aleatoria o dinámica (hora, fecha, etc.)[cite: 1].
# ==============================================================================

import json
import random
import unicodedata
from datetime import datetime

# ------------------------------------------------------------------------------
# SECCIÓN 2: BASE DE CONOCIMIENTO (KNOWLEDGE BASE)
# ------------------------------------------------------------------------------
BASE_CONOCIMIENTO = {
    "hola": [
        "¡Hola! Soy PyBot. ¿En qué puedo ayudarte?",
        "¡Hola de nuevo! ¿Qué tal todo?",
        "¡Hey! Aquí estoy, listo para chatear."
    ],
    "buenos dias": "¡Buenos días! Espero que tengas un excelente día.",
    "buenas tardes": "¡Buenas tardes! ¿Qué necesitas?",
    "buenas noches": "¡Buenas noches! Estoy listo para ayudarte.",
    "como estas": [
        "Estoy funcionando correctamente. ¡Gracias por preguntar!",
        "¡Todo bien por aquí, listo para responder tus dudas!"
    ],
    "quien eres": "Soy PyBot, un chatbot desarrollado en Python.",
    "que eres": "Soy un agente inteligente basado en reglas.",
    "que sabes hacer": "Puedo conversar sobre IA, hardware, software, Python, contarte un chiste, decirte la hora o la fecha. Escribe 'ayuda' para ver todo.",
    "inteligencia artificial": "La Inteligencia Artificial permite que las máquinas aprendan y tomen decisiones.",
    "hardware": "El hardware corresponde a todas las partes físicas del computador.",
    "software": "El software es el conjunto de programas que utiliza un computador.",
    "python": "Python es un lenguaje de programación muy utilizado en Inteligencia Artificial.",
    "cuentame un chiste": "CHISTE",
    "dime un chiste": "CHISTE",
    "que hora es": "HORA",
    "que dia es hoy": "FECHA",
    "me llamo": "NOMBRE",
    "mi nombre es": "NOMBRE",
    "ayuda": "AYUDA",
    "menu": "AYUDA",
    "gracias": [
        "¡Con gusto! Estoy para ayudarte.",
        "¡No hay de qué!"
    ],
    "adios": [
        "¡Hasta luego! Fue un placer conversar contigo.",
        "¡Nos vemos pronto!"
    ]
}

CHISTES = [
    "¿Por qué los programadores prefieren el frío? Porque odian los bugs.",
    "¿Sabes por qué Python no usa gafas? Porque ya tiene 'snake eyes'.",
    "Un programador va al supermercado, su esposa le dice: compra pan y si hay huevos, trae 6. Volvió con 6 panes."
]


# ------------------------------------------------------------------------------
# SECCIÓN 3: NORMALIZACIÓN DE TEXTO (PREPROCESAMIENTO DE PLN)
# ------------------------------------------------------------------------------
def limpiar_texto(texto):
    """
    Normaliza un texto para facilitar la comparación:
      1) Convierte a minúsculas.
      2) Elimina tildes/acentos (NFD + ASCII ignore).
      3) Elimina signos de puntuación comunes.
    """
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    
    caracteres = ",.;:¿?¡!()[]{}"
    for c in caracteres:
        texto = texto.replace(c, "")
        
    return texto.strip()


# ------------------------------------------------------------------------------
# SECCIÓN 4: FUNCIONES DE DIÁLOGO ESPECIALES (RESPUESTAS DINÁMICAS)
# ------------------------------------------------------------------------------
def responder_hora():
    ahora = datetime.now().strftime("%H:%M:%S")
    return f"Son las {ahora}."

def responder_fecha():
    hoy = datetime.now().strftime("%d/%m/%Y")
    return f"Hoy es {hoy}."

def responder_chiste():
    return random.choice(CHISTES)

def responder_ayuda():
    return (
        "Puedo ayudarte con estos temas:\n"
        "  - Saludos (hola, buenos días, etc.)\n"
        "  - Hablar sobre IA, hardware, software y Python\n"
        "  - Decirte la hora o la fecha\n"
        "  - Contarte un chiste\n"
        "  - Recordar tu nombre (dime 'me llamo ...')\n"
        "  - Escribe 'salir' para terminar"
    )

def extraer_nombre(texto_original, texto_limpio):
    for frase in ["me llamo", "mi nombre es"]:
        if frase in texto_limpio:
            partes = texto_limpio.split(frase, 1)
            if len(partes) > 1:
                nombre = partes[1].strip()
                if nombre:
                    return nombre.title()
    return None


# ------------------------------------------------------------------------------
# SECCIÓN 5: MOTOR DE RESPUESTAS
# ------------------------------------------------------------------------------
def obtener_respuesta_ia(entrada, contexto):
    texto = limpiar_texto(entrada)

    if "me llamo" in texto or "mi nombre es" in texto:
        nombre = extraer_nombre(entrada, texto)
        if nombre:
            contexto["nombre_usuario"] = nombre
            return f"¡Mucho gusto, {nombre}! A partir de ahora te recordaré."

    if texto in ("cual es mi nombre", "como me llamo"):
        if contexto.get("nombre_usuario"):
            return f"Tu nombre es {contexto['nombre_usuario']}, ¿cierto?"
        else:
            return "Todavía no me has dicho tu nombre. Dime 'me llamo ...'."

    mejor_coincidencia = None
    mayor_longitud = 0

    for clave, respuesta in BASE_CONOCIMIENTO.items():
        if clave in texto:
            if len(clave) > mayor_longitud:
                mayor_longitud = len(clave)
                mejor_coincidencia = respuesta

    if mejor_coincidencia:
        if mejor_coincidencia == "HORA":
            return responder_hora()
        if mejor_coincidencia == "FECHA":
            return responder_fecha()
        if mejor_coincidencia == "CHISTE":
            return responder_chiste()
        if mejor_coincidencia == "AYUDA":
            return responder_ayuda()
        if mejor_coincidencia == "NOMBRE":
            return "Cuéntame, ¿cómo te llamas?"

        if isinstance(mejor_coincidencia, list):
            respuesta_final = random.choice(mejor_coincidencia)
        else:
            respuesta_final = mejor_coincidencia

        return respuesta_final

    return "Lo siento, todavía no conozco esa respuesta. Escribe 'ayuda' para ver las opciones."


# ------------------------------------------------------------------------------
# SECCIÓN 6: PERSISTENCIA DEL HISTORIAL
# ------------------------------------------------------------------------------
def guardar_historial(historial):
    try:
        with open("historial_chat.json", "w", encoding="utf-8") as archivo:
            json.dump(historial, archivo, ensure_ascii=False, indent=4)
        print("\nHistorial guardado correctamente.")
    except Exception as e:
        print("Error al guardar:", e)


# ------------------------------------------------------------------------------
# SECCIÓN 7: BUCLE PRINCIPAL
# ------------------------------------------------------------------------------
def iniciar_chatbot():
    print("=" * 60)
    print("      CHATBOT INTELIGENTE - PYBOT")
    print("=" * 60)
    print("Escribe 'salir' para terminar o 'ayuda' para ver opciones.\n")

    historial = []
    contexto = {"nombre_usuario": None}

    while True:
        usuario = input("Usuario: ")

        if usuario.strip() == "":
            continue

        if limpiar_texto(usuario) == "salir":
            guardar_historial(historial)
            despedida = "¡Hasta pronto!"
            if contexto.get("nombre_usuario"):
                despedida = f"¡Hasta pronto, {contexto['nombre_usuario']}!"
            print(despedida)
            break

        respuesta = obtener_respuesta_ia(usuario, contexto)
        print("PyBot:", respuesta)
        print()

        historial.append({
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "usuario": usuario,
            "respuesta": respuesta
        })


if __name__ == "__main__":
    iniciar_chatbot()