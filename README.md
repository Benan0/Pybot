# PyBot - Chatbot Inteligente Basado en Reglas

PyBot es un proyecto académico de Inteligencia Artificial simbólica y Procesamiento de Lenguaje Natural (PLN) desarrollado en **Python 3**.

## 🧠 ¿Cómo funciona?
A diferencia de los modelos de lenguaje modernos (como ChatGPT), PyBot opera como un agente inteligente basado en reglas y un sistema experto:
1. **Normalización de texto:** Elimina tildes, mayúsculas y signos de puntuación de la entrada del usuario mediante `unicodedata`.
2. **Búsqueda por palabras clave:** Analiza la Base de Conocimiento para encontrar la coincidencia más específica.
3. **Respuestas dinámicas:** Genera respuestas basadas en el reloj del sistema (hora y fecha), selecciones aleatorias (chistes y saludos) o memoria a corto plazo (nombre del usuario).
4. **Persistencia:** Guarda un historial detallado de la conversación en formato JSON (`historial_chat.json`).

## 🛠️ Tecnologías utilizadas
* Python 3 (Librería estándar: `json`, `random`, `unicodedata`, `datetime`)
* Doxygen (Para la generación de documentación técnica)

## 📥 Cómo descargar y probar el proyecto
1. Haz clic en el botón verde **"Code"** en la parte superior del repositorio.
2. Selecciona **"Download ZIP"** o clona el repositorio usando Git.
3. Ejecuta el archivo en tu terminal:
   ```bash
   python pybot.py
   ```
