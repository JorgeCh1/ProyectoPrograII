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

    def agregar_asignatura(self, nombre, descripcion):
        self.modelo.agregar_asignatura(nombre, descripcion)

    def modificar_asignatura(self, id, nombre=None, descripcion=None):
        self.modelo.modificar_asignatura(id, nombre, descripcion)

    def eliminar_asignatura(self, id):
        self.modelo.eliminar_asignatura(id)

    def obtener_asignaturas(self):
        asignaturas = self.modelo.obtener_asignaturas()
        return {asg[0]: {'nombre': asg[1], 'descripcion': asg[2]} for asg in asignaturas}

    def obtener_asignatura_por_id(self, id):
        asignatura = self.modelo.obtener_asignatura_por_id(id)
        if asignatura:
            return {'id': asignatura[0], 'nombre': asignatura[1], 'descripcion': asignatura[2]}
        return None
    
    def obtener_asignaturas_por_nombre(self, nombre):
        asignaturas = self.modelo.obtener_asignaturas_por_nombre(nombre)
        if asignaturas and isinstance(asignaturas[0], tuple):
            return {asg[0]: {'nombre': asg[1], 'descripcion': asg[2]} for asg in asignaturas}
        else:
            # Manejar el caso donde `obtener_asignaturas_por_nombre` devuelve solo IDs
            asignaturas_completas = {}
            for asg_id in asignaturas:
                asg = self.obtener_asignatura_por_id(asg_id)
                if asg:
                    asignaturas_completas[asg_id] = asg
            return asignaturas_completas

