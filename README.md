# 🤖 PyBot — Chatbot con IA basada en reglas (Python)

Proyecto académico de un **chatbot inteligente basado en reglas** (Rule-Based AI Agent), desarrollado en Python 3, que aplica conceptos básicos de **Procesamiento de Lenguaje Natural (PLN/NLP)** sin usar redes neuronales ni modelos entrenados.

---

## 📋 ¿Qué es PyBot?

PyBot es un agente que responde mediante **reconocimiento de patrones de texto** y una base de conocimiento predefinida (diccionario), no mediante machine learning. Es ideal para introducir conceptos de PLN de forma simple y didáctica.

---

## 🧠 ¿Cómo funciona?

```
Usuario escribe → limpiar_texto() → buscar coincidencia en BASE_CONOCIMIENTO
→ generar respuesta (fija, aleatoria o dinámica) → mostrar + guardar en historial
```

### 1. Normalización de texto — `limpiar_texto()`
Antes de comparar la entrada del usuario con la base de conocimiento, el texto se normaliza:
- Convierte todo a **minúsculas**
- Elimina **tildes/acentos** (con `unicodedata.normalize`)
- Quita **signos de puntuación** (`,.;:¿?¡!()[]{}`)

Así, `"¿Cómo Estás?"` y `"como estas"` se tratan como equivalentes.

### 2. Base de conocimiento — `BASE_CONOCIMIENTO`
Diccionario `{palabra_clave: respuesta}` donde la respuesta puede ser:
- Un **string fijo**
- Una **lista** (se elige una al azar con `random.choice`)
- Una **palabra especial** (`"HORA"`, `"FECHA"`, `"CHISTE"`, `"AYUDA"`, `"NOMBRE"`) que dispara una función dinámica.

### 3. Motor de respuestas — `obtener_respuesta_ia()`
- Revisa primero casos especiales para **recordar el nombre** del usuario.
- Busca qué claves del diccionario están **contenidas** en el texto ingresado.
- Si hay varias coincidencias, se queda con la **más larga/específica**, para evitar falsos positivos (ej. que "hola" gane sobre "buenos dias").
- Ejecuta la función correspondiente según el tipo de coincidencia.

### 4. Funciones dinámicas

| Función | Qué hace |
|---|---|
| `responder_hora()` | Devuelve la hora actual (`datetime.now()`) |
| `responder_fecha()` | Devuelve la fecha actual |
| `responder_chiste()` | Elige un chiste aleatorio |
| `responder_ayuda()` | Muestra el menú de opciones |
| `extraer_nombre()` | Extrae el nombre después de "me llamo" / "mi nombre es" |

### 5. Contexto de conversación
Un diccionario `contexto = {"nombre_usuario": None}` permite que el bot **recuerde el nombre del usuario** mientras dura la sesión activa (no persiste entre ejecuciones).

### 6. Persistencia del historial — `guardar_historial()`
Al escribir `salir`, el historial completo de la conversación (con timestamp) se guarda en `historial_chat.json`.

### 7. Bucle principal — `iniciar_chatbot()`
Ciclo `while True` típico de chatbot de consola: recibe entrada, procesa, responde, guarda en historial, y termina al detectar `"salir"`.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Python 3** | Lenguaje del proyecto |
| `json` | Guardar historial en formato JSON |
| `random` | Elegir respuestas/chistes aleatorios |
| `unicodedata` | Normalizar texto (quitar tildes) |
| `datetime` | Obtener hora y fecha actuales |

Todas las librerías son parte de la **librería estándar de Python**.

---

## 📦 Dependencias

**Ninguna.** No requiere `pip install` ni `requirements.txt`, ya que solo usa módulos incluidos por defecto en Python.

---

## ⚙️ Requisitos

- Python 3.6 o superior
- Permisos de escritura en el directorio de ejecución (para generar `historial_chat.json`)
- Ejecución desde terminal/consola (no tiene interfaz gráfica)

---

## 🚀 Instalación y uso

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/pybot.git
cd pybot

# Ejecutar
python pybot.py
```

Comandos disponibles dentro del chat:
- `ayuda` o `menu` → muestra las opciones disponibles
- `salir` → termina la conversación y guarda el historial

---

## 📁 Estructura del proyecto

```
pybot/
├── pybot.py              # Código principal del chatbot
├── historial_chat.json   # Se genera automáticamente al salir
└── README.md
```

---

## ⚠️ Limitaciones conocidas

- No es IA real: usa *keyword matching* (búsqueda de subcadenas), por lo que errores ortográficos, sinónimos no contemplados o negaciones pueden confundir al bot.
- El nombre del usuario **no persiste entre ejecuciones**, solo durante la sesión activa.
- `historial_chat.json` se **sobrescribe** por completo en cada sesión (no se acumula entre ejecuciones).

---

## 📄 Licencia

MIT — software libre, sin restricciones de autor para uso académico.
