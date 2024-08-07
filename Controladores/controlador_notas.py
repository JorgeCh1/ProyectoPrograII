#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo: Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman


# Controladores/controlador_notas.py
from Modelos.notas import Notas
from Modelos.estudiantes import Estudiantes
from Modelos.asignaturas import Asignaturas

class ControladorNotas:
    def __init__(self):
        self.notas_modelo = Notas()
        self.asignaturas_modelo = Asignaturas()
        self.estudiantes_modelo = Estudiantes()

    def agregar_nota(self, idNota, idEstudiante, idAsignatura, calificacion):
        if idEstudiante not in self.estudiantes_modelo.obtener_estudiantes():
            return f"Error: Estudiante con id {idEstudiante} no existe."
        
        if idAsignatura not in self.asignaturas_modelo.obtener_asignaturas():
            return f"Error: Asignatura con id {idAsignatura} no existe."
        
        self.notas_modelo.agregar_notas(idNota, idEstudiante, idAsignatura, calificacion)
        return f"Nota con id {idNota} agregada."

    def modificar_nota(self, idNota, idEstudiante=None, idAsignatura=None, calificacion=None):
        if idNota not in self.notas_modelo.obtener_notas():
            return f"Error: Nota con id {idNota} no existe."
        
        if idEstudiante is not None and idEstudiante not in self.estudiantes_modelo.obtener_estudiantes():
            return f"Error: Estudiante con id {idEstudiante} no existe."
        
        if idAsignatura is not None and idAsignatura not in self.asignaturas_modelo.obtener_asignaturas():
            return f"Error: Asignatura con id {idAsignatura} no existe."

        self.notas_modelo.modificar_nota(idNota, idEstudiante, idAsignatura, calificacion)
        return f"Nota con id {idNota} modificada."

    def eliminar_nota(self, idNota):
        if idNota not in self.notas_modelo.obtener_notas():
            return f"Error: Nota con id {idNota} no existe."

        self.notas_modelo.eliminar_notas(idNota)
        return f"Nota con id {idNota} eliminada."

    def obtener_notas(self):
        return self.notas_modelo.obtener_notas()

