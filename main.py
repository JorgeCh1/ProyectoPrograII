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
from Vistas.FrmPrincipal import FrmPrincipal

if __name__ == "__main__":
    ventana = tk.Tk()
    app = FrmPrincipal(ventana)
    ventana.mainloop()
