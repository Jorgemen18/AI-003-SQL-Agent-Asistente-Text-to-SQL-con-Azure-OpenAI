import sqlite3

def inicializar_base_datos():
    """Crea una base de datos local y la puebla con datos de un Service Desk."""
    # Esto creará un archivo llamado 'inventario_it.db' en tu carpeta
    conexion = sqlite3.connect('inventario_it.db')
    cursor = conexion.cursor()
    
    # 1. Crear la tabla de equipos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipos (
            id_equipo INTEGER PRIMARY KEY AUTOINCREMENT,
            empleado TEXT NOT NULL,
            departamento TEXT NOT NULL,
            tipo_equipo TEXT NOT NULL,
            modelo TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    ''')
    
    # 2. Limpiar la tabla por si corremos el script varias veces
    cursor.execute('DELETE FROM equipos')
    
    # 3. Insertar datos de prueba (Mock Data)
    datos_prueba = [
        ('Artur', 'Soporte', 'Laptop', 'Dell Inspiron 15', 'Activo'),
        ('Selene', 'Finanzas', 'Laptop', 'MacBook Air', 'Activo'),
        ('Carlos', 'Ventas', 'Tablet', 'iPad Pro', 'En Reparación'),
        ('Diana', 'Recursos Humanos', 'Laptop', 'Lenovo ThinkPad', 'Activo'),
        ('Rubén', 'Operaciones', 'Monitor', 'LG 27 pulgadas', 'Activo')
    ]
    
    cursor.executemany('''
        INSERT INTO equipos (empleado, departamento, tipo_equipo, modelo, estado)
        VALUES (?, ?, ?, ?, ?)
    ''', datos_prueba)
    
    # 4. Guardar los cambios y cerrar
    conexion.commit()
    conexion.close()
    
    print("✅ Base de datos 'inventario_it.db' creada y poblada con éxito.")

if __name__ == "__main__":
    print("--- Inicializando Entorno SQL ---")
    inicializar_base_datos()