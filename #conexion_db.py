#conexion_db

import oracledb 

def probar_conexion():
    # Credenciales extraídas de tu configuración en SQL Developer
    usuario = "POO"
    contrasena = "inacap"
    
    # DSN (Data Source Name): localhost, puerto 1521 y servicio 'xe'
    # Nota: Si tu Oracle usa un servicio distinto (ej. orcl o XEPDB1), cámbialo aquí.
    dsn = "localhost:1521/xe" 

    conexion = None
    try:
        print("Intentando conectar a Oracle Database...")
        # oracledb en modo "Thin" no requiere instalar clientes adicionales
        conexion = oracledb.connect(user=usuario, password=contrasena, dsn=dsn)
        
        print("✅ ¡Conexión EXITOSA a la base de datos Oracle de EcoTech Solutions!")
        print(f"Versión de la BD: {conexion.version}")

    except oracledb.Error as error:
        print("❌ Error al conectar a la base de datos Oracle:", error)
        print("Revisa que el servicio de Oracle esté iniciado en tu computador.")
        
    finally:
        if conexion:
            conexion.close()
            print("🔒 Conexión cerrada por seguridad.")

if __name__ == "__main__":
    probar_conexion()