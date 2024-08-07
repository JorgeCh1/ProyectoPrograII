import tkinter as tk
from tkinter import ttk, messagebox
from Controladores.controlador_notas import ControladorNotas  # Asegúrate de que la importación sea correcta
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

    def create_data_panel(self):
        datos_frame = tk.Frame(self.frame, bd=4, relief=tk.RIDGE, bg="lightgrey")
        datos_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        datos_title = tk.Label(datos_frame, text="Control de Notas", bg="lavender", fg="brown", font=("Arial", 20, "bold"))
        datos_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos de entrada
        self.txt_id_nota = self.crear_campo(datos_frame, "ID Nota", 1)
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
        self.combo_buscar['values'] = ("ID Estudiante", "ID Asignatura")
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

        self.tabla = ttk.Treeview(tabla_frame, columns=("ID Nota", "ID Estudiante", "ID Asignatura", "Calificación"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.tabla.xview)
        scroll_y.config(command=self.tabla.yview)

        self.tabla.heading("ID Nota", text="ID Nota")
        self.tabla.heading("ID Estudiante", text="ID Estudiante")
        self.tabla.heading("ID Asignatura", text="ID Asignatura")
        self.tabla.heading("Calificación", text="Calificación")
        self.tabla.pack(fill=tk.BOTH, expand=1)

        self.tabla['show'] = 'headings'
        self.tabla.column("ID Nota", width=150)
        self.tabla.column("ID Estudiante", width=150)
        self.tabla.column("ID Asignatura", width=150)
        self.tabla.column("Calificación", width=150)

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

        # Validar ID Nota
        id_nota = self.txt_id_nota.get()
        if not id_nota:
            errors.append("El campo ID Nota no puede estar vacío.")

        # Validar ID Estudiante
        id_estudiante = self.txt_id_estudiante.get()
        if not id_estudiante:
            errors.append("El campo ID Estudiante no puede estar vacío.")

        # Validar ID Asignatura
        id_asignatura = self.txt_id_asignatura.get()
        if not id_asignatura:
            errors.append("El campo ID Asignatura no puede estar vacío.")

        # Validar Calificación
        calificacion = self.txt_calificacion.get()
        if not calificacion:
            errors.append("El campo Calificación no puede estar vacío.")
        elif not calificacion.isdigit():
            errors.append("La Calificación debe ser un número entero.")

        if errors:
            self.mostrar_errores(errors)
            return False

        return True

    def mostrar_errores(self, errores):
        """Mostrar mensajes de error en una ventana emergente."""
        error_msg = "\n".join(errores)
        tk.messagebox.showerror("Errores de validación", error_msg)

    def agregar_nota(self):
        if self.validar_campos():
            id_nota = self.txt_id_nota.get()
            id_estudiante = self.txt_id_estudiante.get()
            id_asignatura = self.txt_id_asignatura.get()
            calificacion = self.txt_calificacion.get()

            resultado = self.controlador.agregar_nota(id_nota, id_estudiante, id_asignatura, calificacion)
            tk.messagebox.showinfo("Resultado", resultado)
            self.limpiar_campos()
            self.mostrar_todas_notas()

    def modificar_nota(self):
        if self.validar_campos():
            id_nota = self.txt_id_nota.get()
            id_estudiante = self.txt_id_estudiante.get()
            id_asignatura = self.txt_id_asignatura.get()
            calificacion = self.txt_calificacion.get()

            resultado = self.controlador.modificar_nota(id_nota, id_estudiante, id_asignatura, calificacion)
            tk.messagebox.showinfo("Resultado", resultado)
            self.limpiar_campos()
            self.mostrar_todas_notas()

    def eliminar_nota(self):
        id_nota = self.txt_id_nota.get()
        if not id_nota:
            tk.messagebox.showwarning("Advertencia", "El campo ID Nota no puede estar vacío.")
            return
        resultado = self.controlador.eliminar_nota(id_nota)
        tk.messagebox.showinfo("Resultado", resultado)
        self.mostrar_todas_notas()

    def buscar_notas(self):
        criterio = self.combo_buscar.get()
        valor = self.buscar_entry.get()
        if not valor:
            tk.messagebox.showwarning("Advertencia", "El campo de búsqueda no puede estar vacío.")
            return
        resultados = self.controlador.obtener_notas()
        resultados_filtrados = {k: v for k, v in resultados.items() if v.get(criterio.lower()) == valor}
        self.mostrar_resultados(resultados_filtrados)

    def mostrar_todas_notas(self):
        resultados = self.controlador.obtener_notas()
        self.mostrar_resultados(resultados)

    def mostrar_resultados(self, resultados):
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        for id_nota, datos in resultados.items():
            self.tabla.insert("", tk.END, values=(
                id_nota,
                datos['id_estudiante'],
                datos['id_asignatura'],
                datos['calificacion']
            ))

    def limpiar_campos(self):
        self.txt_id_nota.delete(0, tk.END)
        self.txt_id_estudiante.delete(0, tk.END)
        self.txt_id_asignatura.delete(0, tk.END)
        self.txt_calificacion.delete(0, tk.END)
