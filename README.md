# 🤖 AI-003-SQL-Agent: Asistente Text-to-SQL con Azure OpenAI

Este proyecto es un Agente de Inteligencia Artificial diseñado para un entorno de Service Desk. Traduce preguntas de usuarios en lenguaje natural directamente a consultas SQL, ejecutándolas contra una base de datos relacional para devolver información precisa sobre el inventario de TI.

## 🚀 Características Principales
* **Integración Text-to-SQL:** Conexión directa entre el modelo de lenguaje y una base de datos SQLite.
* **Prompt Engineering Avanzado:** Instrucciones de sistema diseñadas para mitigar alucinaciones, manejar sinónimos del usuario y aplicar operadores SQL (`LIKE`, comodines) para búsquedas flexibles.
* **Consumo de API Real:** Integración segura con Azure OpenAI utilizando variables de entorno para proteger credenciales.
* **Interfaz Interactiva de Terminal:** Ciclo de ejecución continuo para consultas en tiempo real.

## 📸 Demostración
<img width="1208" height="418" alt="Captura de pantalla 2026-07-27 134446" src="https://github.com/user-attachments/assets/b432a948-0093-443e-90e6-3091e2d08dee" />



## 🛠️ Tecnologías Utilizadas
* Python 3.x
* SQLite3 (Base de datos nativa)
* Azure OpenAI API (Modelo GPT)
* `python-dotenv` (Gestión de secretos)

## ⚙️ Cómo ejecutar este proyecto localmente
1. Clona este repositorio.
2. Crea un entorno virtual: `python -m venv .venv`
3. Instala las dependencias: `pip install openai python-dotenv`
4. Crea un archivo `.env` en la raíz con tus credenciales de Azure OpenAI:
   ```env
   AZURE_OPENAI_ENDPOINT="tu_endpoint"
   AZURE_OPENAI_API_KEY="tu_llave"
   AZURE_OPENAI_DEPLOYMENT_NAME="tu_modelo"
   ´´´
