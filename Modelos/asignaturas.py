#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo: Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman



class Asignaturas:
    def __init__(self):
        self.asignaturas = {}  # {id: {'nombre': '', 'descripcion': ''}}

    def agregar_asignatura(self, id, nombre, descripcion):
        self.asignaturas[id] = {
            'nombre': nombre,
            'descripcion': descripcion
        }

    def modificar_asignatura(self, id, nombre=None, descripcion=None):
        if id in self.asignaturas:
            if nombre is not None:
                self.asignaturas[id]['nombre'] = nombre
            if descripcion is not None:
                self.asignaturas[id]['descripcion'] = descripcion

    def eliminar_asignatura(self, id):
        if id in self.asignaturas:
            del self.asignaturas[id]

    def obtener_asignaturas(self):
        return self.asignaturas