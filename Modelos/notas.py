#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo: Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman



# class Notas:
#     def __init__(self): 
#         self.notas = {}


def agregar_notas(self, idNota, idEstudiante, idAsigatura, calificacion):
    self.notas[idNota] = {
        'idEstudiante': idEstudiante,
        'idAsigatura': idAsigatura,
        'calificacion': calificacion
}

def modificar_nota(self, idNota, idEstudiante=None, idAsigatura=None, calificacion=None):
    if id in self.notas:
        if idEstudiante is not None:
            self.notas[idNota]['idEstudiante'] = idEstudiante
        if idAsigatura is not None:
            self.notas[idNota]['idAsigatura'] = idAsigatura
        if calificacion is not None:
            self.notas[idNota]['calificacion'] = calificacion


def eliminar_notas(self, idNota):
    if idNota in self.notas:
        del self.notas[idNota]

def obtener_notas(self):
    return self.notas
