class Notas:
    def __init__(self):
        self.notas = {}

    def agregar_notas(self, idNotas, idEstudiante, idAsigatura, calificacion):
        self.notas[idNotas] = {
            'idEstudiante': idEstudiante,
            'idAsigatura': idAsigatura,
            'calificacion': calificacion
        }

    def modificar_nota(self, idNota, idEstudiante=None, idAsigatura=None, calificacion=None):
        if idNota in self.notas:
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
