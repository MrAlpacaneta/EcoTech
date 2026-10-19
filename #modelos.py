#modelos.py

# 1. CLASE PADRE (Herencia para evitar duplicación - Criterio 2.1.2.G.4)
class UsuarioSistema:
    def __init__(self, id_usuario, username, password, rol, activo=True):
        # El doble guion bajo (__) aplica el Encapsulamiento (Criterio 2.1.2.G.3)
        self.__idUsuario = id_usuario
        self.__username = username
        self.__password = password
        self.__rol = rol
        self.__activo = activo

    def iniciar_sesion(self):
        print(f"Iniciando sesión para el usuario: {self.__username}")
        return True

    def cerrar_sesion(self):
        print("Sesión cerrada correctamente.")

# 2. CLASE HIJA (Empleado hereda de UsuarioSistema)
class Empleado(UsuarioSistema):
    def __init__(self, id_usuario, username, password, rol, id_empleado, nombre, telefono, correo, fecha_inicio, salario):
        # super() llama al constructor del padre, reciclando el código de usuario
        super().__init__(id_usuario, username, password, rol)
        self.__idEmpleado = id_empleado
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo
        self.__fechaInicio = fecha_inicio
        self.__salario = salario
        self.__departamento = None # Representa la agregación con Departamento (0..*)

    # Métodos accesores (Getters y Setters) para acceder a datos encapsulados
    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
            print("Salario actualizado.")

    def asignar_departamento(self, departamento):
        self.__departamento = departamento

# 3. ENTIDADES RESTANTES (Criterio 2.1.1.G.1)
class Departamento:
    def __init__(self, id_depto, nombre):
        self.__idDepto = id_depto
        self.__nombre = nombre
        self.__gerente = None

    def asignar_gerente(self, empleado):
        self.__gerente = empleado

class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio):
        self.__idProyecto = id_proyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fechaInicio = fecha_inicio

class AsignacionProyecto:
    # Clase asociativa que conecta Empleado y Proyecto (Relaciones - Criterio 2.1.1.G.2)
    def __init__(self, id_asignacion, fecha_asignacion, rol_proyecto, empleado, proyecto):
        self.__idAsignacion = id_asignacion
        self.__fechaAsignacion = fecha_asignacion
        self.__rolProyecto = rol_proyecto
        self.__empleado = empleado   
        self.__proyecto = proyecto   

class RegistroTiempo:
    # Composición con empleado
    def __init__(self, id_registro, fecha, horas, descripcion, empleado):
        self.__idRegistro = id_registro
        self.__fecha = fecha
        self.__horasTrabajadas = horas
        self.__descripcionTarea = descripcion
        self.__empleado = empleado

class GestorReportes:
    def generar_reportes_pdf(self):
        pass
    def generar_reportes_excel(self):
        pass