#conexion_db

import oracledb 

def probar_conexion():
    usuario = "POO"
    contrasena = "inacap"
    dsn = "localhost:1521/xe" 

    conexion = None
    try:
        print("Intentando conectar a Oracle Database...")
        conexion = oracledb.connect(user=usuario, password=contrasena, dsn=dsn)
        
        print("Conexión establecida a la base de datos de EcoTech Solutions!")
        print(f"Versión de la BD: {conexion.version}")

    except oracledb.Error as error:
        print("Error al conectar a la base de datos Oracle:", error)
        print("Revisa el servicio de Oracle.")
        
    finally:
        if conexion:
            conexion.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    probar_conexion()