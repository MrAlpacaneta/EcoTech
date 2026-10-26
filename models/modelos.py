#modelos.py

#CLASE PADRE (Herencia para evitar duplicación de datos)
class UsuarioSistema:
    def __init__(self, id_usuario, username, password, rol, activo=True):
        self.__idusuario = id_usuario
        self.__username = username
        self.__password = password
        self.__rol = rol
        self.__activo = activo

    def iniciar_sesion(self):
        print(f"Iniciando sesión para el usuario: {self.__username}")
        return True

    def cerrar_sesion(self):
        print("Sesión cerrada correctamente.")

    def get_id_usuario(self):
        return self.__idusuario
    def get_password(self):
            return self.__password
    def get_rol(self):
            return self.__rol
    def get_activo(self):
            return self.__activo

# 2. CLASE HIJA (Empleado hereda de UsuarioSistema)
class Empleado(UsuarioSistema):
    def __init__(self, id_usuario, username, password, rol, id_empleado, nombre, telefono, correo, fecha_inicio, salario):
        super().__init__(id_usuario, username, password, rol)
        self.__idempleado = id_empleado
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo
        self.__fechainicio = fecha_inicio
        self.__salario = salario
        self.__departamento = None 

    def get_id_empleado(self):
        return self.__idempleado

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_correo(self):
        return self.__correo

    def get_fecha_inicio(self):
        return self.__fechainicio
    
    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
            print("Salario actualizado.")

    def get_departamento(self):
        return self.__departamento

    def asignar_departamento(self, departamento):
        self.__departamento = departamento

class Departamento:
    def __init__(self, id_depto, nombre):
        self.__iddepto = id_depto
        self.__nombre = nombre
        self.__gerente = None

    def get_id_depto(self):
        return self.__iddepto

    def get_nombre(self):
        return self.__nombre

    def get_gerente(self):
        return self.__gerente

    def asignar_gerente(self, empleado):
        self.__gerente = empleado

    def asignar_gerente(self, empleado):
        self.__gerente = empleado

class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio):
        self.__idproyecto = id_proyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fechainicio = fecha_inicio

    def get_id_proyecto(self):
        return self.__idproyecto

    def get_nombre(self):
        return self.__nombre

    def get_descripcion(self):
        return self.__descripcion

    def get_fecha_inicio(self):
        return self.__fechainicio

class AsignacionProyecto:
    def __init__(self, id_asignacion, fecha_asignacion, rol_proyecto, empleado, proyecto):
        self.__idasignacion = id_asignacion
        self.__fechaasignacion = fecha_asignacion
        self.__rolproyecto = rol_proyecto
        self.__empleado = empleado   
        self.__proyecto = proyecto   

    def get_id_asignacion(self):
        return self.__idasignacion

    def get_fecha_asignacion(self):
        return self.__fechaasignacion

    def get_rol_proyecto(self):
        return self.__rolproyecto

    def get_empleado(self):
        return self.__empleado

    def get_proyecto(self):
        return self.__proyecto    

class RegistroTiempo:
    def __init__(self, id_registro, fecha, horas, descripcion, empleado):
        self.__idregistro = id_registro
        self.__fecha = fecha
        self.__horastrabajadas = horas
        self.__descripciontarea = descripcion
        self.__empleado = empleado

    def get_id_registro(self):
        return self.__idregistro

    def get_fecha(self):
        return self.__fecha

    def get_horas_trabajadas(self):
        return self.__horastrabajadas

    def get_descripcion_tarea(self):
        return self.__descripciontarea

    def get_empleado(self):
        return self.__empleado

class GestorReportes:
    def generar_reportes_pdf(self):
        print("Generando reportes en PDF...")
    def generar_reportes_excel(self):
        print("Generando reportes en Excel...")

