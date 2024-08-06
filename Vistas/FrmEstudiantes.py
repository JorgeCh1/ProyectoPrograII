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
from Controladores.controlador_estudiantes import ControladorEstudiantes
import re

class InterfazEstudiante:
    def __init__(self, parent):
        self.controlador = ControladorEstudiantes()
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_data_panel()
        self.create_result_panel()
        
        # Asociar eventos de botones
        self.boton_agregar.config(command=self.agregar_estudiante)
        self.boton_modificar.config(command=self.modificar_estudiante)
        self.boton_eliminar.config(command=self.eliminar_estudiante)
        self.boton_limpiar.config(command=self.limpiar_campos)
        self.boton_buscar.config(command=self.buscar_estudiantes)
        self.boton_mostrar_todo.config(command=self.mostrar_todos_estudiantes)

    def create_data_panel(self):
        datos_frame = tk.Frame(self.frame, bd=4, relief=tk.RIDGE, bg="lightgrey")
        datos_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        datos_title = tk.Label(datos_frame, text="Control de Estudiantes", bg="lavender", fg="brown", font=("Arial", 20, "bold"))
        datos_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos de entrada
        self.txt_id = self.crear_campo(datos_frame, "ID", 1)
        self.txt_nombre = self.crear_campo(datos_frame, "Nombre", 2)
        self.txt_telefono = self.crear_campo(datos_frame, "Teléfono", 3)
        self.txt_correo = self.crear_campo(datos_frame, "Correo", 4)
        self.txt_fecha_de_nacimiento = self.crear_campo(datos_frame, "Fecha de nacimiento", 5)
        self.txt_direccion = self.crear_campo(datos_frame, "Dirección", 6, is_text=True)
        self.txt_genero = self.crear_campo(datos_frame, "Género", 7, is_combobox=True)

        # Botones
        btn_frame = tk.Frame(datos_frame, bd=4, relief=tk.RIDGE, bg="dark grey")
        btn_frame.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        button_texts = ["Agregar", "Modificar", "Eliminar", "Limpiar"]
        for index, button_text in enumerate(button_texts):
            boton = tk.Button(btn_frame, text=button_text, width=7, font=("Arial", 14))
            boton.grid(row=0, column=index, padx=10, pady=10)
            setattr(self, f"boton_{button_text.lower()}", boton)

        # Configuración de expansión
        datos_frame.grid_rowconfigure(8, weight=1)
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

        self.boton_buscar = tk.Button(resultados_frame, text="Buscar", width=7, font=("Arial", 14))
        self.boton_buscar.grid(row=0, column=3, padx=10, pady=10)

        self.boton_mostrar_todo = tk.Button(resultados_frame, text="Mostrar todo", width=10, font=("Arial", 14))
        self.boton_mostrar_todo.grid(row=0, column=4, padx=10, pady=10)

        tabla_frame = tk.Frame(resultados_frame, bd=4, relief=tk.RIDGE, bg="lavender")
        tabla_frame.grid(row=1, column=0, columnspan=5, pady=10, padx=10, sticky="nsew")

        scroll_x = tk.Scrollbar(tabla_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(tabla_frame, orient=tk.VERTICAL)

        self.tabla = ttk.Treeview(tabla_frame, columns=("ID", "Nombre", "Teléfono", "Correo", "Fecha Nac", "Dirección", "Género"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.tabla.xview)
        scroll_y.config(command=self.tabla.yview)

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Teléfono", text="Teléfono")
        self.tabla.heading("Correo", text="Correo")
        self.tabla.heading("Fecha Nac", text="Fecha de Nacimiento")
        self.tabla.heading("Dirección", text="Dirección")
        self.tabla.heading("Género", text="Género")
        self.tabla.pack(fill=tk.BOTH, expand=1)

        self.tabla['show'] = 'headings'
        self.tabla.column("ID", width=100)
        self.tabla.column("Nombre", width=100)
        self.tabla.column("Teléfono", width=100)
        self.tabla.column("Correo", width=100)
        self.tabla.column("Fecha Nac", width=100)
        self.tabla.column("Dirección", width=100)
        self.tabla.column("Género", width=90)

        # Configuración de expansión
        resultados_frame.grid_rowconfigure(1, weight=1)
        resultados_frame.grid_columnconfigure(4, weight=1)

    def crear_campo(self, frame, texto, fila, is_text=False, is_combobox=False):
        label = tk.Label(frame, text=f"{texto}: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        label.grid(row=fila, column=0, pady=10, sticky="w")

        if is_text:
            entry = tk.Text(frame, width=30, height=4, font=("Arial", 10))
        elif is_combobox:
            entry = ttk.Combobox(frame, width=27, font=("Arial", 15), state='readonly')
            entry['values'] = ("Masculino", "Femenino", "Otro")
        else:
            entry = tk.Entry(frame, font=("Arial", 15), bd=5, relief=tk.GROOVE)

        entry.grid(row=fila, column=1, pady=10, padx=30, sticky="w")
        return entry
    
    def validar_campos(self):
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

        # Validar Teléfono
        telefono = self.txt_telefono.get()
        if not telefono:
            errors.append("El campo Teléfono no puede estar vacío.")

        # Validar Correo
        correo = self.txt_correo.get()
        if not correo:
            errors.append("El campo Correo no puede estar vacío.")
        elif not self.validar_email(correo):
            errors.append("El correo electrónico no tiene un formato válido.")

        # Validar Fecha de Nacimiento
        fecha_nacimiento = self.txt_fecha_de_nacimiento.get()
        if not fecha_nacimiento:
            errors.append("El campo Fecha de nacimiento no puede estar vacío.")

        # Validar Dirección
        direccion = self.txt_direccion.get("1.0", tk.END).strip()
        if not direccion:
            errors.append("El campo Dirección no puede estar vacío.")

        # Validar Género
        genero = self.txt_genero.get()
        if not genero:
            errors.append("El campo Género no puede estar vacío.")

        if errors:
            self.mostrar_errores(errors)
            return False

        return True

    def validar_email(self, email):
        """Validar el formato del correo electrónico."""
        import re
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def mostrar_errores(self, errores):
        """Mostrar mensajes de error en una ventana emergente."""
        error_msg = "\n".join(errores)
        tk.messagebox.showerror("Errores de validación", error_msg)

    def agregar_estudiante(self):
        if self.validar_campos():
            id = self.txt_id.get()
            nombre = self.txt_nombre.get()
            telefono = self.txt_telefono.get()
            correo = self.txt_correo.get()
            fecha_nacimiento = self.txt_fecha_de_nacimiento.get()
            direccion = self.txt_direccion.get("1.0", tk.END).strip()
            genero = self.txt_genero.get()

            self.controlador.agregar_estudiante(
                id, nombre, telefono, correo, fecha_nacimiento, direccion, genero
            )
            self.mostrar_todos_estudiantes()

    def modificar_estudiante(self):
        if self.validar_campos():
            id = self.txt_id.get()
            nombre = self.txt_nombre.get()
            telefono = self.txt_telefono.get()
            correo = self.txt_correo.get()
            fecha_nacimiento = self.txt_fecha_de_nacimiento.get()
            direccion = self.txt_direccion.get("1.0", tk.END).strip()
            genero = self.txt_genero.get()

            self.controlador.modificar_estudiante(
                id, nombre, telefono, correo, fecha_nacimiento, direccion, genero
            )
            self.mostrar_todos_estudiantes()

    def eliminar_estudiante(self):
        id = self.txt_id.get()
        if not id:
            tk.messagebox.showwarning("Advertencia", "El campo ID no puede estar vacío.")
            return
        self.controlador.eliminar_estudiante(id)
        self.mostrar_todos_estudiantes()

    def buscar_estudiantes(self):
        criterio = self.combo_buscar.get()
        valor = self.buscar_entry.get()
        if not valor:
            tk.messagebox.showwarning("Advertencia", "El campo de búsqueda no puede estar vacío.")
            return
        resultados = self.controlador.obtener_estudiantes()
        resultados_filtrados = {k: v for k, v in resultados.items() if v.get(criterio.lower()) == valor}
        self.mostrar_resultados(resultados_filtrados)

    def mostrar_todos_estudiantes(self):
        resultados = self.controlador.obtener_estudiantes()
        self.mostrar_resultados(resultados)

    def mostrar_resultados(self, resultados):
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        for id, datos in resultados.items():
            self.tabla.insert("", tk.END, values=(
                id,
                datos['nombre'],
                datos['telefono'],
                datos['correo'],
                datos['fecha_nacimiento'],
                datos['direccion'],
                datos['genero']
            ))

    def limpiar_campos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_telefono.delete(0, tk.END)
        self.txt_correo.delete(0, tk.END)
        self.txt_fecha_de_nacimiento.delete(0, tk.END)
        self.txt_direccion.delete("1.0", tk.END)
        self.txt_genero.set("")

