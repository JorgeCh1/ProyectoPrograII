import tkinter as tk
from tkinter import ttk, messagebox
from Controladores.controlador_notas import ControladorNotas 
import re

class InterfazNota:
    def __init__(self, parent):
        self.controlador = ControladorNotas()
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_data_panel()
        self.create_result_panel()

        # Asociar eventos de botones
        self.boton_agregar.config(command=self.agregar_nota)
        self.boton_modificar.config(command=self.modificar_nota)
        self.boton_eliminar.config(command=self.eliminar_nota)
        self.boton_limpiar.config(command=self.limpiar_campos)
        self.boton_buscar.config(command=self.buscar_notas)
        self.boton_mostrar_todo.config(command=self.mostrar_todas_notas)
        
        # Asignar evento de selección de la tabla
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)
        
        # Cargar todas las notas al iniciar la interfaz
        self.mostrar_todas_notas()

    def create_data_panel(self):
        datos_frame = tk.Frame(self.frame, bd=4, relief=tk.RIDGE, bg="lightgrey")
        datos_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        datos_title = tk.Label(datos_frame, text="Control de Notas", bg="lavender", fg="brown", font=("Arial", 20, "bold"))
        datos_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos de entrada (sin ID)
        self.txt_id = self.crear_campo(datos_frame, "ID", 1, is_disabled=True)  # ID se desactiva ya que es autoincremental
        self.txt_id_estudiante = self.crear_campo(datos_frame, "ID Estudiante", 2)
        self.txt_id_asignatura = self.crear_campo(datos_frame, "ID Asignatura", 3)
        self.txt_calificacion = self.crear_campo(datos_frame, "Calificación", 4)

        # Botones
        btn_frame = tk.Frame(datos_frame, bd=4, relief=tk.RIDGE, bg="dark grey")
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

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
        self.combo_buscar['values'] = ("ID", "ID Estudiante", "ID Asignatura")
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

        self.tabla = ttk.Treeview(tabla_frame, columns=("ID", "ID Estudiante", "ID Asignatura", "Calificación"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.tabla.xview)
        scroll_y.config(command=self.tabla.yview)

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("ID Estudiante", text="ID Estudiante")
        self.tabla.heading("ID Asignatura", text="ID Asignatura")
        self.tabla.heading("Calificación", text="Calificación")
        self.tabla.pack(fill=tk.BOTH, expand=1)

        self.tabla['show'] = 'headings'
        self.tabla.column("ID", width=100)
        self.tabla.column("ID Estudiante", width=100)
        self.tabla.column("ID Asignatura", width=100)
        self.tabla.column("Calificación", width=100)

        # Configuración de expansión
        resultados_frame.grid_rowconfigure(1, weight=1)
        resultados_frame.grid_columnconfigure(4, weight=1)

    def crear_campo(self, parent, label_text, fila, is_disabled=False):
        label = tk.Label(parent, text=label_text, bg="lightgrey", fg="black", font=("Arial", 14, "bold"))
        label.grid(row=fila, column=0, pady=5, padx=10, sticky="w")
        
        field = tk.Entry(parent, font=("Arial", 13))
        field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
        if is_disabled:
            field.config(state='disabled')
                
        return field
    
    def agregar_nota(self):
        datos = self.obtener_datos_entrada()
        if datos:
            resultado = self.controlador.agregar_nota(*datos)
            self.mostrar_todas_notas()
            self.limpiar_campos()
            messagebox.showinfo("Información", resultado)

    def modificar_nota(self):
        id_nota = self.txt_id.get()
        if id_nota:
            datos = self.obtener_datos_entrada()
            if datos:
                resultado = self.controlador.modificar_nota(id_nota, *datos)
                self.mostrar_todas_notas()
                self.limpiar_campos()
                messagebox.showinfo("Información", resultado)
        else:
            messagebox.showerror("Error", "Seleccione una nota para modificar")

    def eliminar_nota(self):
        id_nota = self.txt_id.get()
        if id_nota:
            resultado = self.controlador.eliminar_nota(id_nota)
            self.mostrar_todas_notas()
            self.limpiar_campos()
            messagebox.showinfo("Información", resultado)
        else:
            messagebox.showerror("Error", "Seleccione una nota para eliminar")

    def buscar_notas(self):
        campo_busqueda = self.combo_buscar.get()
        valor_busqueda = self.buscar_entry.get()

        if campo_busqueda and valor_busqueda:
            if campo_busqueda == "ID":
                nota = self.controlador.obtener_nota_por_id(valor_busqueda)
                if nota:
                    self.mostrar_resultados({valor_busqueda: nota})
                else:
                    self.tabla.delete(*self.tabla.get_children())  # Limpiar tabla si no se encuentra ningún resultado
                    messagebox.showinfo("Información", "No se encontró ninguna nota con ese ID")
            elif campo_busqueda == "ID Estudiante":
                notas = self.controlador.obtener_notas_por_estudiante(valor_busqueda)
                self.mostrar_resultados(notas)
            elif campo_busqueda == "ID Asignatura":
                notas = self.controlador.obtener_notas_por_asignatura(valor_busqueda)
                self.mostrar_resultados(notas)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un criterio de búsqueda y proporcione un valor")

    def mostrar_todas_notas(self):
        notas = self.controlador.obtener_notas()
        self.mostrar_resultados(notas)

    def limpiar_campos(self):
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state='disabled')
        self.txt_id_estudiante.delete(0, tk.END)
        self.txt_id_asignatura.delete(0, tk.END)
        self.txt_calificacion.delete(0, tk.END)

    def obtener_datos_entrada(self):
        id_estudiante = self.txt_id_estudiante.get()
        id_asignatura = self.txt_id_asignatura.get()
        calificacion = self.txt_calificacion.get()

        if not id_estudiante or not id_asignatura or not calificacion:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return None

        try:
            calificacion = float(calificacion)
        except ValueError:
            messagebox.showerror("Error", "La calificación debe ser un número")
            return None

        return id_estudiante, id_asignatura, calificacion

    def mostrar_resultados(self, notas):
        self.tabla.delete(*self.tabla.get_children())
        for id_nota, datos in notas.items():
            self.tabla.insert("", tk.END, values=(id_nota, datos['id_estudiante'], datos['id_asignatura'], datos['calificacion']))

    def seleccionar_fila(self, event):
        item = self.tabla.selection()[0]
        datos = self.tabla.item(item, 'values')
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.insert(0, datos[0])
        self.txt_id.config(state='disabled')
        self.txt_id_estudiante.delete(0, tk.END)
        self.txt_id_estudiante.insert(0, datos[1])
        self.txt_id_asignatura.delete(0, tk.END)
        self.txt_id_asignatura.insert(0, datos[2])
        self.txt_calificacion.delete(0, tk.END)
        self.txt_calificacion.insert(0, datos[3])
