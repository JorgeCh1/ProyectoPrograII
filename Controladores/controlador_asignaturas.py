#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo:  Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman   



from Modelos.asignaturas import Asignaturas

class ControladorAsignaturas:
    def __init__(self):
        self.modelo = Asignaturas()

    def agregar_asignatura(self, id, nombre, descripcion):
        self.modelo.agregar_asignatura(id, nombre, descripcion)

    def modificar_asignatura(self, id, nombre=None, descripcion=None):
        self.modelo.modificar_asignatura(id, nombre, descripcion)

    def eliminar_asignatura(self, id):
        self.modelo.eliminar_asignatura(id)

    def obtener_asignaturas(self):
        return self.modelo.obtener_asignaturas()

    def obtener_asignatura_por_id(self, id):
        asignaturas = self.obtener_asignaturas()
        return asignaturas.get(id, None)