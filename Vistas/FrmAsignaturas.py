#from Modelos.asignaturas  import asignaturas
from Controladores.controlador_asignaturas  import ControladorAsignaturas
import tkinter as tk
from tkinter import ttk
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
        self.boton_buscar.config(command=self.buscar_asignatura)
        self.boton_mostrar_todo.config(command=self.mostrar_todos_asignaturas)

    def create_data_panel(self):
        datos_frame = tk.Frame(self.frame, bd=4, relief=tk.RIDGE, bg="lightgrey")
        datos_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        datos_title = tk.Label(datos_frame, text="Control de Asignaturas", bg="lavender", fg="brown", font=("Arial", 20, "bold"))
        datos_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos de entrada
        self.txt_id = self.crear_campo(datos_frame, "ID", 1)
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
        self.combo_buscar['values'] = ("ID", "Nombre")
        self.combo_buscar.grid(row=0, column=1, padx=20, pady=10)

        self.buscar_entry = tk.Entry(resultados_frame, width=20, font=("Arial", 11), bd=5, relief=tk.GROOVE)
        self.buscar_entry.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        self.buscar_btn = tk.Button(resultados_frame, text="Buscar", width=7, font=("Arial", 14))
        self.buscar_btn.grid(row=0, column=3, padx=10, pady=10)

        self.mostrar_btn = tk.Button(resultados_frame, text="Mostrar todo", width=10, font=("Arial", 14))
        self.mostrar_btn.grid(row=0, column=4, padx=10, pady=10)

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
        self.tabla.column("Descripción", width=200)

        setattr(self, "tabla_asignatura", self.tabla)

        # Configuración de expansión
        resultados_frame.grid_rowconfigure(1, weight=1)
        resultados_frame.grid_columnconfigure(4, weight=1)

    def crear_campo(self, frame, texto, fila, is_text=False):
        label = tk.Label(frame, text=f"{texto}: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        label.grid(row=fila, column=0, pady=10, sticky="w")

        if is_text:
            entry = tk.Text(frame, width=30, height=4, font=("Arial", 10))
        else:
            entry = tk.Entry(frame, font=("Arial", 15), bd=5, relief=tk.GROOVE)

        entry.grid(row=fila, column=1, pady=10, padx=30, sticky="w")
        return entry
            
    def validar_campos_asignatura(self):
        """Validar que los campos no estén vacíos y que los datos sean correctos."""
        errors = []

        # Validar ID
        id = self.txt_id.get()
        if not id:
            errors.append("El campo ID no puede estar vacío.")

        # Validar Nombre
        nombre = self.txt_nombre.get()
        if not nombre:
            errors.append("El campo Nombre no puede estar vacío.")

        # Validar Descripción
        descripcion = self.txt_descripcion.get("1.0", tk.END).strip()
        if not descripcion:
            errors.append("El campo Descripción no puede estar vacío.")

        if errors:
            self.mostrar_errores(errors)
            return False

        return True
    
    def mostrar_errores(self, errores):
        """Mostrar mensajes de error en una ventana emergente."""
        error_msg = "\n".join(errores)
        tk.messagebox.showerror("Errores de validación", error_msg)

    def agregar_asignatura(self):
        if self.validar_campos_asignatura():
            id = self.txt_id.get()
            nombre = self.txt_nombre.get()
            descripcion = self.txt_descripcion.get("1.0", tk.END).strip()

            self.controlador.agregar_asignatura(
                id, nombre, descripcion
            )
            self.mostrar_todas_asignaturas()

    def modificar_asignatura(self):
        if self.validar_campos_asignatura():
            id = self.txt_id.get()
            nombre = self.txt_nombre.get()
            descripcion = self.txt_descripcion.get("1.0", tk.END).strip()

            self.controlador.modificar_asignatura(
                id, nombre, descripcion
            )
            self.mostrar_todas_asignaturas()

    def eliminar_asignatura(self):
        id = self.txt_id.get()
        if not id:
            tk.messagebox.showwarning("Advertencia", "El campo ID no puede estar vacío.")
            return
        self.controlador.eliminar_asignatura(id)
        self.mostrar_todas_asignaturas()

    def buscar_asignaturas(self):
        criterio = self.combo_buscar.get()
        valor = self.buscar_entry.get()
        if not valor:
            tk.messagebox.showwarning("Advertencia", "El campo de búsqueda no puede estar vacío.")
            return
        resultados = self.controlador.obtener_asignaturas()
        resultados_filtrados = {k: v for k, v in resultados.items() if v.get(criterio.lower()) == valor}
        self.mostrar_resultados(resultados_filtrados)

    def mostrar_todas_asignaturas(self):
        resultados = self.controlador.obtener_asignaturas()
        self.mostrar_resultados(resultados)

    def mostrar_resultados(self, resultados):
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        for id, datos in resultados.items():
            self.tabla.insert("", tk.END, values=(
                id,
                datos['nombre'],
                datos['descripcion']
            ))

    def limpiar_campos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_descripcion.delete("1.0", tk.END)
