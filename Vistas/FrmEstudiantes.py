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
from tkcalendar import DateEntry
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

        # Asignar evento de selección de la tabla
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)
        
        # Cargar todos los estudiantes al iniciar la interfaz
        self.mostrar_todos_estudiantes()

    def create_data_panel(self):
        datos_frame = tk.Frame(self.frame, bd=4, relief=tk.RIDGE, bg="lightgrey")
        datos_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        datos_title = tk.Label(datos_frame, text="Control de Estudiantes", bg="lavender", fg="brown", font=("Arial", 20, "bold"))
        datos_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos de entrada (sin ID)
        self.txt_id = self.crear_campo(datos_frame, "ID", 1, is_disabled=True)  # ID se desactiva ya que es autoincremental
        self.txt_nombre = self.crear_campo(datos_frame, "Nombre", 2)
        self.txt_telefono = self.crear_campo(datos_frame, "Teléfono", 3)
        self.txt_correo = self.crear_campo(datos_frame, "Correo", 4)
        self.txt_fecha_de_nacimiento = self.crear_campo(datos_frame, "Fecha de nacimiento", 5, is_date=True)
        self.txt_direccion = self.crear_campo(datos_frame, "Dirección", 6, is_text=True)
        self.txt_genero = self.crear_campo(datos_frame, "Género", 7, is_combobox=True)

        # Botones
        btn_frame = tk.Frame(datos_frame, bd=4, relief=tk.RIDGE, bg="dark grey")
        btn_frame.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        button_texts = ["Agregar", "Modificar", "Eliminar", "Limpiar"]
        for index, button_text in enumerate(button_texts):
            boton = tk.Button(btn_frame, text=button_text, width=7, font=("Arial", 12, "bold"), bd=3, cursor="hand2")
            boton.grid(row=0, column=index, padx=5, pady=5)
            setattr(self, f'boton_{button_text.lower()}', boton)


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

    def crear_campo(self, parent, label_text, fila, is_disabled=False, is_text=False, is_combobox=False, is_date=False):
        label = tk.Label(parent, text=label_text, bg="lightgrey", fg="black", font=("Arial", 14, "bold"))
        label.grid(row=fila, column=0, pady=5, padx=10, sticky="w")
        
        if is_combobox:
            field = ttk.Combobox(parent, font=("Arial", 13), state="readonly")
            field['values'] = ("Masculino", "Femenino", "Otro")
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
        elif is_text:
            field = tk.Text(parent, height=4, width=25, font=("Arial", 13))
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
        elif is_date:
            field = DateEntry(parent, font=("Arial", 13), date_pattern="yyyy-mm-dd")
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
        else:
            field = tk.Entry(parent, font=("Arial", 13))
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
            if is_disabled:
                field.config(state='disabled')
                
        return field
    
    def crear_campo(self, parent, label_text, fila, is_disabled=False, is_text=False, is_combobox=False, is_date=False):
        label = tk.Label(parent, text=label_text, bg="lightgrey", fg="black", font=("Arial", 14, "bold"))
        label.grid(row=fila, column=0, pady=5, padx=10, sticky="w")
        
        if is_combobox:
            field = ttk.Combobox(parent, font=("Arial", 13), state="readonly")
            field['values'] = ("Masculino", "Femenino", "Otro")
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
        elif is_text:
            field = tk.Text(parent, height=4, width=25, font=("Arial", 13))
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
        elif is_date:
            field = DateEntry(parent, font=("Arial", 13), date_pattern="yyyy-mm-dd")
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
        else:
            field = tk.Entry(parent, font=("Arial", 13))
            field.grid(row=fila, column=1, pady=5, padx=10, sticky="w")
            if is_disabled:
                field.config(state='disabled')
                
        return field
    
    def agregar_estudiante(self):
        datos = self.obtener_datos_entrada()
        if datos:
            self.controlador.agregar_estudiante(*datos)
            self.mostrar_todos_estudiantes()
            self.limpiar_campos()

    def modificar_estudiante(self):
        id_estudiante = self.txt_id.get()
        if id_estudiante:
            datos = self.obtener_datos_entrada()
            if datos:
                self.controlador.modificar_estudiante(id_estudiante, *datos)
                self.mostrar_todos_estudiantes()
                self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Seleccione un estudiante para modificar")

    def eliminar_estudiante(self):
        id_estudiante = self.txt_id.get()
        if id_estudiante:
            self.controlador.eliminar_estudiante(id_estudiante)
            self.mostrar_todos_estudiantes()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Seleccione un estudiante para eliminar")

    def buscar_estudiantes(self):
        campo_busqueda = self.combo_buscar.get()
        valor_busqueda = self.buscar_entry.get()

        if campo_busqueda and valor_busqueda:
            if campo_busqueda == "ID":
                estudiante = self.controlador.obtener_estudiante_por_id(valor_busqueda)
                if estudiante:
                    self.mostrar_resultados({valor_busqueda: estudiante})
                else:
                    self.tabla.delete(*self.tabla.get_children())  # Limpiar tabla si no se encuentra ningún resultado
                    messagebox.showinfo("Información", "No se encontró ningún estudiante con ese ID")
            elif campo_busqueda == "Nombre":
                estudiantes = self.controlador.obtener_estudiantes_por_nombre(valor_busqueda)
                self.mostrar_resultados(estudiantes)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un criterio de búsqueda y proporcione un valor")

    def mostrar_todos_estudiantes(self):
        estudiantes = self.controlador.obtener_estudiantes()
        self.mostrar_resultados(estudiantes)

    def limpiar_campos(self):
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state='disabled')
        self.txt_nombre.delete(0, tk.END)
        self.txt_telefono.delete(0, tk.END)
        self.txt_correo.delete(0, tk.END)
        self.txt_fecha_de_nacimiento.delete(0, tk.END)
        self.txt_direccion.delete('1.0', tk.END)
        self.txt_genero.set('')

    def obtener_datos_entrada(self):
        nombre = self.txt_nombre.get()
        telefono = self.txt_telefono.get()
        correo = self.txt_correo.get()
        fecha_nacimiento = self.txt_fecha_de_nacimiento.get()
        direccion = self.txt_direccion.get('1.0', tk.END).strip()
        genero = self.txt_genero.get()

        if not nombre or not telefono or not correo or not fecha_nacimiento or not direccion or not genero:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return None

        if not re.match(r'^\S+@\S+\.\S+$', correo):
            messagebox.showerror("Error", "Correo inválido")
            return None

        if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_nacimiento):
            messagebox.showerror("Error", "Fecha de nacimiento inválida (use formato YYYY-MM-DD)")
            return None

        return nombre, telefono, correo, fecha_nacimiento, direccion, genero

    def mostrar_resultados(self, estudiantes):
        self.tabla.delete(*self.tabla.get_children())
        for id_estudiante, datos in estudiantes.items():
            self.tabla.insert("", tk.END, values=(id_estudiante, datos['nombre'], datos['telefono'], datos['correo'], datos['fecha_nacimiento'], datos['direccion'], datos['genero']))

    def seleccionar_fila(self, event):
        item = self.tabla.selection()[0]
        datos = self.tabla.item(item, 'values')
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.insert(0, datos[0])
        self.txt_id.config(state='disabled')
        self.txt_nombre.delete(0, tk.END)
        self.txt_nombre.insert(0, datos[1])
        self.txt_telefono.delete(0, tk.END)
        self.txt_telefono.insert(0, datos[2])
        self.txt_correo.delete(0, tk.END)
        self.txt_correo.insert(0, datos[3])
        self.txt_fecha_de_nacimiento.delete(0, tk.END)
        self.txt_fecha_de_nacimiento.insert(0, datos[4])
        self.txt_direccion.delete('1.0', tk.END)
        self.txt_direccion.insert('1.0', datos[5])
        self.txt_genero.set(datos[6])