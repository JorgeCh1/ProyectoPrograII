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
from tkinter import PhotoImage

# Asegúrate de importar las clases de tus otras interfaces
from .FrmEstudiantes import InterfazEstudiante
from .FrmAsignaturas import InterfazAsignatura
from .FrmNotas import InterfazNota

class FrmPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema Gestión de Matrícula - Menú Principal")
        self.ventana.geometry("800x600")  # Tamaño inicial de la ventana
        self.ventana.state('zoomed')      # Maximiza la ventana al iniciar
        self.ventana.resizable(False, False)  # No permite redimensionar la ventana

        # Frame para el menú
        menu_frame = tk.LabelFrame(self.ventana, text="Menú Principal", font=("Arial", 18, "bold"), bg="navy", fg="lavender", padx=10, pady=10)
        menu_frame.pack(side=tk.TOP, fill=tk.X)

        # Frame para centrar los botones
        button_frame = tk.Frame(menu_frame, bg="navy")
        button_frame.pack(pady=10)

        # Botones de navegación
        btn_estudiantes = tk.Button(button_frame, text="Gestión de Estudiantes", command=self.mostrar_interfaz_estudiante, font=("Arial", 14), width=30)
        btn_estudiantes.pack(side=tk.LEFT, padx=5)

        btn_asignaturas = tk.Button(button_frame, text="Gestión de Asignaturas", command=self.mostrar_interfaz_asignatura, font=("Arial", 14), width=30)
        btn_asignaturas.pack(side=tk.LEFT, padx=5)

        btn_notas = tk.Button(button_frame, text="Gestión de Notas", command=self.mostrar_interfaz_nota, font=("Arial", 14), width=30)
        btn_notas.pack(side=tk.LEFT, padx=5)

        # Frame para el contenido
        self.content_frame = tk.Frame(self.ventana, bg="white")
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Mostrar mensaje inicial
        self.mostrar_mensaje_inicial()

    def mostrar_mensaje_inicial(self):
        # Limpiar el contenido actual (si lo hubiera)
        self._limpiar_content_frame()

        # Añadir texto
        mensaje = tk.Label(self.content_frame, text="Bienvenido al Sistema de Gestión de Matrícula\nProyecto de Programación II", font=("Arial", 24, "bold"), bg="white")
        mensaje.pack(expand=True)

        # # Podemos añadir una imagen
        # # Dejo esto acá por si queremos añadirla
        # try:
        #     imagen = PhotoImage(file="ruta/a/tu/imagen.png")  # Asegúrate de tener una imagen en esta ruta
        #     imagen_label = tk.Label(self.content_frame, image=imagen, bg="white")
        #     imagen_label.image = imagen  # Mantener una referencia de la imagen
        #     imagen_label.pack(expand=True)
        # except Exception as e:
        #     print(f"No se pudo cargar la imagen: {e}")

    def mostrar_interfaz_estudiante(self):
        self._limpiar_content_frame()
        InterfazEstudiante(self.content_frame)

    def mostrar_interfaz_asignatura(self):
        self._limpiar_content_frame()
        InterfazAsignatura(self.content_frame)

    def mostrar_interfaz_nota(self):
        self._limpiar_content_frame()
        InterfazNota(self.content_frame)

    def _limpiar_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
