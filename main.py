import os
import sqlite3
from dotenv import load_dotenv
from openai import AzureOpenAI

# 1. Cargar las credenciales seguras desde el archivo .env
load_dotenv()

# 2. Configurar la conexión al servicio real de Azure
cliente = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01" # Versión estándar recomendada de la API
)
modelo_despliegue = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

def consultar_agente(pregunta_usuario):
    print(f"\n👤 Pregunta: {pregunta_usuario}")
    
    # 3. El Prompt del Sistema: Le damos su identidad y el esquema exacto de la base de datos
    instrucciones_sistema = """
    Eres un asistente de TI experto en bases de datos para un Service Desk. 
    Tu única tarea es traducir las preguntas del usuario a consultas SQL válidas para SQLite.
    
    La base de datos tiene una sola tabla llamada 'equipos' con este esquema:
    - id_equipo (INTEGER)
    - empleado (TEXT)
    - departamento (TEXT)
    - tipo_equipo (TEXT) (Valores permitidos: 'Laptop', 'Tablet', 'Monitor')
    - modelo (TEXT)
    - estado (TEXT) (Valores permitidos: 'Activo', 'En Reparación')
    
    REGLAS ESTRICTAS:
    1. Devuelve ÚNICAMENTE el código SQL puro. Sin explicaciones, sin comillas invertidas de markdown.
    2. Respeta exactamente las mayúsculas y minúsculas de los Valores permitidos (ej. usa 'Laptop' con L mayúscula, no 'laptop').
    3. Si el usuario usa sinónimos como "computadora", "PC" o "máquina", asume que se refiere al tipo_equipo 'Laptop'.
    4. Usa SIEMPRE el operador LIKE y comodines (%) cuando el usuario busque por marcas o modelos (ej. modelo LIKE '%LG%') para atrapar coincidencias parciales.
    """
    try:
        # 4. Llamamos a tu modelo en Azure OpenAI
        respuesta = cliente.chat.completions.create(
            model=modelo_despliegue,
            messages=[
                {"role": "system", "content": instrucciones_sistema},
                {"role": "user", "content": pregunta_usuario}
            ],
            temperature=0 # Temperatura 0 para máxima precisión y cero inventos
        )
        
        # Extraemos el SQL que generó la IA
        consulta_sql = respuesta.choices[0].message.content.strip()
        print(f"🤖 SQL Generado por IA: {consulta_sql}")
        
        # 5. Ejecutamos esa consulta real en nuestra base de datos local
        conexion = sqlite3.connect('inventario_it.db')
        cursor = conexion.cursor()
        cursor.execute(consulta_sql)
        resultados = cursor.fetchall()
        conexion.close()
        
        # 6. Imprimir los resultados de forma limpia
        if resultados:
            print("✅ Resultados encontrados en la BD:")
            for fila in resultados:
                print(f"   - {fila}")
        else:
            print("⚠️ No se encontraron resultados.")
            
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

# Zona interactiva
if __name__ == "__main__":
    print("--- 🤖 Iniciando Agente de Soporte de IA ---")
    print("💡 Escribe tu pregunta sobre el inventario, o 'salir' para terminar.\n")
    
    while True:
        # Esperamos a que el usuario escriba algo en la terminal
        entrada_usuario = input("👤 Tú: ")
        
        # Condición de salida para romper el ciclo
        if entrada_usuario.strip().lower() == 'salir':
            print("👋 ¡Cerrando el Agente de Soporte! Hasta luego.")
            break
            
        # Si el usuario presiona Enter sin escribir nada, lo ignoramos
        if entrada_usuario.strip() == "":
            continue
            
        # Le pasamos la pregunta a nuestra función de IA
        consultar_agente(entrada_usuario)
        print("-" * 50) # Una línea separadora visual para que se lea mejor