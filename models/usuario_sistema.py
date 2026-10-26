from .conexion_db import ConexionDB

class UsuarioSistema:
    def __init__(self):
        self.id_usuario = ""
        self.username = ""
        self.rol = ""

    def iniciar_sesion(self, username_input, password_input):
        try:
            c = ConexionDB()
            sql = "SELECT id_usuario, username, rol FROM usuario_sistema WHERE username = :usr AND password = :pwd AND activo = 1"
            c.cursor.execute(sql, usr=username_input, pwd=password_input)
            
            fila = c.cursor.fetchone()
            
            if fila:
                # Si encuentra al usuario, guardamos sus datos y retornamos el rol
                self.id_usuario = fila[0]
                self.username = fila[1]
                self.rol = fila[2]
                return self.rol
            else:
                return None
                
        except Exception as e:
            print(f"ERROR al intentar iniciar sesión: {e}")
            return None
        finally:
            try: c.conexion.close()
            except: pass