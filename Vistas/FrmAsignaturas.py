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
from tkinter import ttk, messagebox
from Controladores.controlador_asignaturas  import ControladorAsignaturas
import re

class InterfazAsignatura:
    def __init__(self, parent):
        self.controlador = ControladorAsignaturas()
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_data_panel()
        self.create_result_panel()
        
        # Asociar eventos de botones
        self.boton_agregar.config(command=self.agregar_asignatura)
        self.boton_modificar.config(command=self.modificar_asignatura)
        self.boton_eliminar.config(command=self.eliminar_asignatura)
        self.boton_limpiar.config(command=self.limpiar_campos)
        self.boton_buscar.config(command=self.buscar_asignaturas)
        self.boton_mostrar_todo.config(command=self.mostrar_todas_asignaturas)
        
        # Asignar evento de selección de la tabla
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)
        
        # Cargar todas las asignaturas al iniciar la interfaz
        self.mostrar_todas_asignaturas()

    def create_data_panel(self):
        datos_frame = tk.Frame(self.frame, bd=4, relief=tk.RIDGE, bg="lightgrey")
        datos_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        datos_title = tk.Label(datos_frame, text="Control de Asignaturas", bg="lavender", fg="brown", font=("Arial", 20, "bold"))
        datos_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos de entrada (sin ID)
        self.txt_id = self.crear_campo(datos_frame, "ID", 1, is_disabled=True)  # ID se desactiva ya que es autoincremental
        self.txt_nombre = self.crear_campo(datos_frame, "Nombre", 2)
        self.txt_descripcion = self.crear_campo(datos_frame, "Descripción", 3, is_text=True)

        # Botones
        btn_frame = tk.Frame(datos_frame, bd=4, relief=tk.RIDGE, bg="dark grey")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        button_texts = ["Agregar", "Modificar", "Eliminar", "Limpiar"]
        for index, button_text in enumerate(button_texts):
            boton = tk.Button(btn_frame, text=button_text, width=7, font=("Arial", 14))
            boton.grid(row=0, column=index, padx=10, pady=10)
            setattr(self, f"boton_{button_text.lower()}", boton)

        # Configuración de expansión
        datos_frame.grid_rowconfigure(4, weight=1)
        datos_frame.grid_columnconfigure(1, weight=1)

    def create_result_panel(self):
        resultados_frame = tk.Frame(self.frame, bd=4, relief=tk.RIDGE, bg="navy")
        resultados_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        buscar_label = tk.Label(resultados_frame, text="Buscar por: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        buscar_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.combo_buscar = ttk.Combobox(resultados_frame, width=10, font=("Arial", 15), state='readonly')
        self.combo_buscar['values'] = ("ID", "Nombre")  # Búsqueda por ID y por nombre
        self.combo_buscar.grid(row=0, column=1, padx=20, pady=10)

        self.buscar_entry = tk.Entry(resultados_frame, width=20, font=("Arial", 11), bd=5, relief=tk.GROOVE)
        self.buscar_entry.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        self.boton_buscar = tk.Button(resultados_frame, text="Buscar", width=7, font=("Arial", 14))
        self.boton_buscar.grid(row=0, column=3, padx=10, pady=10)

        self.boton_mostrar_todo = tk.Button(resultados_frame, text="Mostrar todo", width=10, font=("Arial", 14))
        self.boton_mostrar_todo.grid(row=0, column=4, padx=10, pady=10)

        tabla_frame = tk.Frame(resultados_frame, bd=4, relief=tk.RIDGE, bg="lavender")
        tabla_frame.grid(row=1, column=0, columnspan=5, pady=10, padx=10, sticky="nsew")

        scroll_x = tk.Scrollbar(tabla_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(tabla_frame, orient=tk.VERTICAL)

        self.tabla = ttk.Treeview(tabla_frame, columns=("ID", "Nombre", "Descripción"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.tabla.xview)
        scroll_y.config(command=self.tabla.yview)

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Descripción", text="Descripción")
        self.tabla.pack(fill=tk.BOTH, expand=1)

        self.tabla['show'] = 'headings'
        self.tabla.column("ID", width=100)
        self.tabla.column("Nombre", width=100)
        self.tabla.column("Descripción", width=300)

        # Configuración de expansión
        resultados_frame.grid_rowconfigure(1, weight=1)
        resultados_frame.grid_columnconfigure(4, weight=1)

    def crear_campo(self, parent, label_text, fila, is_disabled=False, is_text=False):
        label = tk.Label(parent, text=label_text, bg="lightgrey", fg="black", font=("Arial", 14, "bold"))
        label.grid(row=fila, column=0, pady=5, padx=10, sticky="w")
        
        if is_text:
            field = tk.Text(parent, height=4, width=25, font=("Arial", 13))
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
        else:
            field = tk.Entry(parent, font=("Arial", 13))
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
            if is_disabled:
                field.config(state='disabled')
                
        return field
            
    def agregar_asignatura(self):
        datos = self.obtener_datos_entrada()
        if datos:
            self.controlador.agregar_asignatura(*datos)
            self.mostrar_todas_asignaturas()
            self.limpiar_campos()

    def modificar_asignatura(self):
        id_asignatura = self.txt_id.get()
        if id_asignatura:
            datos = self.obtener_datos_entrada()
            if datos:
                self.controlador.modificar_asignatura(id_asignatura, *datos)
                self.mostrar_todas_asignaturas()
                self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Seleccione una asignatura para modificar")

    def eliminar_asignatura(self):
        id_asignatura = self.txt_id.get()
        if id_asignatura:
            self.controlador.eliminar_asignatura(id_asignatura)
            self.mostrar_todas_asignaturas()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Seleccione una asignatura para eliminar")

    def buscar_asignaturas(self):
        campo_busqueda = self.combo_buscar.get()
        valor_busqueda = self.buscar_entry.get()

        if campo_busqueda and valor_busqueda:
            if campo_busqueda == "ID":
                asignatura = self.controlador.obtener_asignatura_por_id(valor_busqueda)
                if asignatura:
                    self.mostrar_resultados({valor_busqueda: asignatura})
                else:
                    self.tabla.delete(*self.tabla.get_children())  # Limpiar tabla si no se encuentra ningún resultado
                    messagebox.showinfo("Información", "No se encontró ninguna asignatura con ese ID")
            elif campo_busqueda == "Nombre":
                asignaturas = self.controlador.obtener_asignaturas_por_nombre(valor_busqueda)
                self.mostrar_resultados(asignaturas)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un criterio de búsqueda y proporcione un valor")

    def mostrar_todas_asignaturas(self):
        asignaturas = self.controlador.obtener_asignaturas()
        self.mostrar_resultados(asignaturas)

    def limpiar_campos(self):
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state='disabled')
        self.txt_nombre.delete(0, tk.END)
        self.txt_descripcion.delete('1.0', tk.END)

    def obtener_datos_entrada(self):
        nombre = self.txt_nombre.get()
        descripcion = self.txt_descripcion.get('1.0', tk.END).strip()

        if not nombre or not descripcion:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return None

        return nombre, descripcion

    def mostrar_resultados(self, asignaturas):
        self.tabla.delete(*self.tabla.get_children())
        for id_asignatura, datos in asignaturas.items():
            self.tabla.insert("", tk.END, values=(id_asignatura, datos['nombre'], datos['descripcion']))

    def seleccionar_fila(self, event):
        item = self.tabla.selection()[0]
        datos = self.tabla.item(item, 'values')
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.insert(0, datos[0])
        self.txt_id.config(state='disabled')
        self.txt_nombre.delete(0, tk.END)
        self.txt_nombre.insert(0, datos[1])
        self.txt_descripcion.delete('1.0', tk.END)
        self.txt_descripcion.insert('1.0', datos[2])