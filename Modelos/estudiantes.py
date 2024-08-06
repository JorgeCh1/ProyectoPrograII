# modelo/estudiantes.py

#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo: Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman

class Estudiantes:
    def __init__(self):
        self.estudiantes = {}  # {id: {'nombre': '', 'telefono': '', 'correo': '', 'fecha_nacimiento': '', 'direccion': '', 'genero': ''}}

    def agregar_estudiante(self, id, nombre, telefono, correo, fecha_nacimiento, direccion, genero):
        self.estudiantes[id] = {
            'nombre': nombre,
            'telefono': telefono,
            'correo': correo,
            'fecha_nacimiento': fecha_nacimiento,
            'direccion': direccion,
            'genero': genero
        }

    def modificar_estudiante(self, id, nombre=None, telefono=None, correo=None, fecha_nacimiento=None, direccion=None, genero=None):
        if id in self.estudiantes:
            if nombre is not None:
                self.estudiantes[id]['nombre'] = nombre
            if telefono is not None:
                self.estudiantes[id]['telefono'] = telefono
            if correo is not None:
                self.estudiantes[id]['correo'] = correo
            if fecha_nacimiento is not None:
                self.estudiantes[id]['fecha_nacimiento'] = fecha_nacimiento
            if direccion is not None:
                self.estudiantes[id]['direccion'] = direccion
            if genero is not None:
                self.estudiantes[id]['genero'] = genero

    def eliminar_estudiante(self, id):
        if id in self.estudiantes:
            del self.estudiantes[id]

    def obtener_estudiantes(self):
        return self.estudiantes
