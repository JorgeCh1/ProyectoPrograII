#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo: Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman



import tkinter as tk
from tkinter import ttk
class asignatura:
    def __init__(self, id, nombre, descripcion):

        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):

        return f"Asignatura {self.id}: {self.nombre} - {self.descripcion}"

    def to_dict(self):

        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }

    @classmethod
    def from_dict(cls, data):

        return cls(data["id"], data["nombre"], data["descripcion"])