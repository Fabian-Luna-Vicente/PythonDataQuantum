import mysql.connector

print("Paso 1 - Importado OK")

try:
    print("Paso 2 - Intentando conectar...")
    
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        connection_timeout=10  
    )
    
    print("Paso 3 - Conexion establecida")

except Exception as e:
    print(f"Paso 3 - FALLO: {e}")

print("Paso 4 - Fin del script")
input("ENTER para salir")