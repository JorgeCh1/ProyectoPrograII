#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo: Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman

from Modelos.estudiantes import Estudiantes

class ControladorEstudiantes:
    def __init__(self):
        self.modelo = Estudiantes()  # El modelo ya maneja la base de datos SQLite

    def agregar_estudiante(self, nombre, telefono, correo, fecha_nacimiento, direccion, genero):
        self.modelo.agregar_estudiante(nombre, telefono, correo, fecha_nacimiento, direccion, genero)

    def modificar_estudiante(self, id, nombre=None, telefono=None, correo=None, fecha_nacimiento=None, direccion=None, genero=None):
        self.modelo.modificar_estudiante(id, nombre, telefono, correo, fecha_nacimiento, direccion, genero)

    def eliminar_estudiante(self, id):
        self.modelo.eliminar_estudiante(id)

    def obtener_estudiantes(self):
        estudiantes = self.modelo.obtener_estudiantes()
        return {est[0]: {'nombre': est[1], 'telefono': est[2], 'correo': est[3], 'fecha_nacimiento': est[4], 'direccion': est[5], 'genero': est[6]} for est in estudiantes}

    def obtener_estudiante_por_id(self, id):
        estudiante = self.modelo.obtener_estudiante_por_id(id)
        if estudiante:
            return {'id': estudiante[0], 'nombre': estudiante[1], 'telefono': estudiante[2], 'correo': estudiante[3], 'fecha_nacimiento': estudiante[4], 'direccion': estudiante[5], 'genero': estudiante[6]}
        return None

    def obtener_estudiantes_por_nombre(self, nombre):
        estudiantes = self.modelo.obtener_estudiante_por_nombre(nombre)
        if estudiantes and isinstance(estudiantes[0], tuple):
            return {est[0]: {'nombre': est[1], 'telefono': est[2], 'correo': est[3], 'fecha_nacimiento': est[4], 'direccion': est[5], 'genero': est[6]} for est in estudiantes}
        else:
            # Manejar el caso donde `obtener_estudiante_por_nombre` devuelve solo IDs
            estudiantes_completos = {}
            for est_id in estudiantes:
                est = self.obtener_estudiante_por_id(est_id)
                if est:
                    estudiantes_completos[est_id] = est
            return estudiantes_completos



