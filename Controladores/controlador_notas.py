#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo: Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman


from Modelos.notas import Notas
from Modelos.estudiantes import Estudiantes
from Modelos.asignaturas import Asignaturas

class ControladorNotas:
    def __init__(self):
        self.modelo_notas = Notas()
        self.modelo_estudiantes = Estudiantes()
        self.modelo_asignaturas = Asignaturas()

    def agregar_nota(self, id_estudiante, id_asignatura, calificacion):
        if self.modelo_estudiantes.obtener_estudiante_por_id(id_estudiante) is None:
            return f"Error: Estudiante con ID {id_estudiante} no existe."
        if self.modelo_asignaturas.obtener_asignatura_por_id(id_asignatura) is None:
            return f"Error: Asignatura con ID {id_asignatura} no existe."
        
        self.modelo_notas.agregar_nota(id_estudiante, id_asignatura, calificacion)
        return f"Nota agregada para el estudiante {id_estudiante} en la asignatura {id_asignatura}."

    def modificar_nota(self, id, id_estudiante=None, id_asignatura=None, calificacion=None):
        if self.modelo_notas.obtener_nota_por_id(id) is None:
            return f"Error: Nota con ID {id} no existe."
        if id_estudiante is not None and self.modelo_estudiantes.obtener_estudiante_por_id(id_estudiante) is None:
            return f"Error: Estudiante con ID {id_estudiante} no existe."
        if id_asignatura is not None and self.modelo_asignaturas.obtener_asignatura_por_id(id_asignatura) is None:
            return f"Error: Asignatura con ID {id_asignatura} no existe."

        self.modelo_notas.modificar_nota(id, id_estudiante, id_asignatura, calificacion)
        return f"Nota con ID {id} modificada."

    def eliminar_nota(self, id):
        if self.modelo_notas.obtener_nota_por_id(id) is None:
            return f"Error: Nota con ID {id} no existe."

        self.modelo_notas.eliminar_nota(id)
        return f"Nota con ID {id} eliminada."

    def obtener_notas(self):
        notas = self.modelo_notas.obtener_notas()
        return {nota[0]: {'id_estudiante': nota[1], 'id_asignatura': nota[2], 'calificacion': nota[3]} for nota in notas}

    def obtener_nota_por_id(self, id):
        nota = self.modelo_notas.obtener_nota_por_id(id)
        if nota:
            return {'id': nota[0], 'id_estudiante': nota[1], 'id_asignatura': nota[2], 'calificacion': nota[3]}
        return None

    def obtener_notas_por_estudiante(self, id_estudiante):
        notas = self.modelo_notas.obtener_notas_por_estudiante(id_estudiante)
        return {nota[0]: {'id_estudiante': nota[1], 'id_asignatura': nota[2], 'calificacion': nota[3]} for nota in notas}

    def obtener_notas_por_asignatura(self, id_asignatura):
        notas = self.modelo_notas.obtener_notas_por_asignatura(id_asignatura)
        return {nota[0]: {'id_estudiante': nota[1], 'id_asignatura': nota[2], 'calificacion': nota[3]} for nota in notas}