from Modelos.estudiantes import Estudiantes

class ControladorEstudiantes:
    def __init__(self):
        self.modelo = Estudiantes()

    def agregar_estudiante(self, id, nombre, telefono, correo, fecha_nacimiento, direccion, genero):
        self.modelo.agregar_estudiante(id, nombre, telefono, correo, fecha_nacimiento, direccion, genero)

    def modificar_estudiante(self, id, nombre=None, telefono=None, correo=None, fecha_nacimiento=None, direccion=None, genero=None):
        self.modelo.modificar_estudiante(id, nombre, telefono, correo, fecha_nacimiento, direccion, genero)

    def eliminar_estudiante(self, id):
        self.modelo.eliminar_estudiante(id)

    def obtener_estudiantes(self):
        return self.modelo.obtener_estudiantes()

    def obtener_estudiante_por_id(self, id):
        estudiantes = self.obtener_estudiantes()
        return estudiantes.get(id, None)
