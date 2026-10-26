from .conexion_db import ConexionDB

class Departamento:
    id_depto: str = ""
    nombre: str = ""

    def __str__(self):
        return f"ID: {self.id_depto} | Nombre: {self.nombre}"

    #C: CREATE (Insertar)
    def insertar(self):
        try:
            c = ConexionDB()
            sql = "INSERT INTO departamento (id_depto, nombre) VALUES (:id_depto, :nom)"
            c.cursor.execute(sql, id_depto=self.id_depto, nom=self.nombre)
            c.conexion.commit()
            print("¡Departamento insertado correctamente!")
        except Exception as e:
            print(f"ERROR al insertar en la Base de Datos: {e}")
        finally:
            try: c.conexion.close()
            except: pass

    #R: READ (Obtener todos)
    def obtenerTodos(self):
        try:
            c = ConexionDB()
            c.cursor.execute("SELECT id_depto, nombre FROM departamento")
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los departamentos: {e}")
            return []
        finally:
            try: c.conexion.close()
            except: pass

    def cargarPorID(self, idBuscado):
        try:
            c = ConexionDB()
            sql = "SELECT id_depto, nombre FROM departamento WHERE id_depto = :id"
            c.cursor.execute(sql, id=idBuscado)
            fila = c.cursor.fetchone()
            
            if fila:
                self.id_depto = fila[0]
                self.nombre = fila[1]
                return True
            else:
                print("No se encontró un departamento con ese ID.")
                return False
        except Exception as e:
            print(f"ERROR al cargar departamento por ID: {e}")
            return False
        finally:
            try: c.conexion.close()
            except: pass

    #U: UPDATE (Actualizar)
    def actualizar(self):
        try:
            c = ConexionDB()
            sql = "UPDATE departamento SET nombre=:nom WHERE id_depto=:id_depto"
            c.cursor.execute(sql, nom=self.nombre, id_depto=self.id_depto)
            c.conexion.commit()
            print("¡Departamento actualizado correctamente!")
        except Exception as e:
            print(f"ERROR al actualizar en la Base de Datos: {e}")
        finally:
            try: c.conexion.close()
            except: pass

    #D: DELETE (Eliminar)
    def eliminar(self, idEliminar):
        try:
            c = ConexionDB()
            sql = "DELETE FROM departamento WHERE id_depto = :id"
            c.cursor.execute(sql, id=idEliminar)
            c.conexion.commit()
            print("¡Departamento eliminado correctamente!")
        except Exception as e:
            print(f"ERROR al eliminar en la Base de Datos: {e}")
        finally:
            try: c.conexion.close()
            except: pass