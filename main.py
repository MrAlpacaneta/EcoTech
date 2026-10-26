from models.departamento import Departamento
from models.usuario_sistema import UsuarioSistema

def iniciar_sesion():
    print("=== LOGIN ECOTECH SOLUTIONS ===")
    usuario = UsuarioSistema()
    intentos = 3
    
    while intentos > 0:
        user = input("Usuario: ")
        pwd = input("Contraseña: ")
        
        rol = usuario.iniciar_sesion(user, pwd)
        
        if rol:
            print(f"\n✅ ¡Bienvenido {user}! Has iniciado sesión como: {rol}")
            return rol
        else:
            intentos -= 1
            print(f"❌ Credenciales incorrectas. Te quedan {intentos} intentos.\n")
            
    print("Demasiados intentos fallidos. Saliendo...")
    return None

def imprimir_menu_admin():
    print("--- MENÚ ADMINISTRADOR ---")
    print("1. Ver todos los departamentos")
    print("2. Agregar departamento")
    print("3. Actualizar departamento")
    print("4. Eliminar departamento")
    print("0. Cerrar Sesión y Salir")
    print()

def imprimir_menu_normal():
    print("--- MENÚ USUARIO NORMAL ---")
    print("1. Ver todos los departamentos")
    print("0. Cerrar Sesión y Salir")
    print()

# --- FLUJO PRINCIPAL ---
rol_actual = iniciar_sesion()

if rol_actual:
    depto = Departamento()
    
    while True:
        # Mostramos un menú distinto según el rol
        if rol_actual == "Administrador":
            imprimir_menu_admin()
        else:
            imprimir_menu_normal()
            
        opcion = input("Ingresa una opción: ")
        print()
        
        # Opción 1: Disponible para ambos roles
        if opcion == "1":
            listaDeptos = depto.obtenerTodos()
            if listaDeptos:
                print("--- LISTA DE DEPARTAMENTOS ---")
                for fila in listaDeptos:
                    print(f"ID: {fila[0]} | Nombre: {fila[1]}")
            else:
                print("No hay departamentos registrados.")
            print()

        # Opciones 2, 3 y 4: Exclusivas del Administrador
        elif opcion == "2" and rol_actual == "Administrador":
            print("--- AGREGAR DEPARTAMENTO ---")
            depto.id_depto = input("ID del Departamento (ej. D01): ")
            depto.nombre = input("Nombre del Departamento: ")
            depto.insertar()
            print()

        elif opcion == "3" and rol_actual == "Administrador":
            idSeleccionado = input("Ingresa el ID del departamento a actualizar: ")
            if depto.cargarPorID(idSeleccionado):
                nuevoNombre = input(f"Nuevo nombre [{depto.nombre}]: ")
                if nuevoNombre != "":
                    depto.nombre = nuevoNombre
                depto.actualizar()
            print()

        elif opcion == "4" and rol_actual == "Administrador":
            idSeleccionado = input("Ingresa el ID a eliminar: ")
            depto.eliminar(idSeleccionado)
            print()

        elif opcion == "0":
            print("Cerrando sesión... ¡Hasta pronto!")
            break
            
        else:
            print("❌ Opción no válida o no tienes permisos para ejecutarla.\n")