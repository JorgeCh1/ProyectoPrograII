import tkinter as tk
from tkinter import ttk

class InterfazNota:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_data_panel()
        self.create_result_panel()

    def create_data_panel(self):
        datos_frame = tk.Frame(self.frame, bd=4, relief=tk.RIDGE, bg="lightgrey")
        datos_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        datos_title = tk.Label(datos_frame, text="Control de Notas", bg="lavender", fg="brown", font=("Arial", 20, "bold"))
        datos_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos de entrada
        self.crear_campo(datos_frame, "ID Estudiante", 1)
        self.crear_campo(datos_frame, "ID Asignatura", 2)
        self.crear_campo(datos_frame, "Nota", 3)

        # Botones
        btn_frame = tk.Frame(datos_frame, bd=4, relief=tk.RIDGE, bg="dark grey")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        button_texts = ["Agregar", "Modificar", "Eliminar", "Limpiar"]
        for index, button_text in enumerate(button_texts):
            boton = tk.Button(btn_frame, text=button_text, width=7, font=("Arial", 14))
            boton.grid(row=0, column=index, padx=10, pady=10)

        # Configuración de expansión
        datos_frame.grid_rowconfigure(4, weight=1)
        datos_frame.grid_columnconfigure(1, weight=1)

    def create_result_panel(self):
        resultados_frame = tk.Frame(self.frame, bd=4, relief=tk.RIDGE, bg="navy")
        resultados_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        buscar_label = tk.Label(resultados_frame, text="Buscar por: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        buscar_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        combo_buscar = ttk.Combobox(resultados_frame, width=10, font=("Arial", 15), state='readonly')
        combo_buscar['values'] = ("ID Estudiante", "ID Asignatura")
        combo_buscar.grid(row=0, column=1, padx=20, pady=10)

        buscar_entry = tk.Entry(resultados_frame, width=20, font=("Arial", 11), bd=5, relief=tk.GROOVE)
        buscar_entry.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        buscar_btn = tk.Button(resultados_frame, text="Buscar", width=7, font=("Arial", 14))
        buscar_btn.grid(row=0, column=3, padx=10, pady=10)

        mostrar_btn = tk.Button(resultados_frame, text="Mostrar todo", width=10, font=("Arial", 14))
        mostrar_btn.grid(row=0, column=4, padx=10, pady=10)

        tabla_frame = tk.Frame(resultados_frame, bd=4, relief=tk.RIDGE, bg="lavender")
        tabla_frame.grid(row=1, column=0, columnspan=5, pady=10, padx=10, sticky="nsew")

        scroll_x = tk.Scrollbar(tabla_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(tabla_frame, orient=tk.VERTICAL)

        tabla = ttk.Treeview(tabla_frame, columns=("ID Estudiante", "ID Asignatura", "Nota"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=tabla.xview)
        scroll_y.config(command=tabla.yview)

        tabla.heading("ID Estudiante", text="ID Estudiante")
        tabla.heading("ID Asignatura", text="ID Asignatura")
        tabla.heading("Nota", text="Nota")
        tabla.pack(fill=tk.BOTH, expand=1)

        tabla['show'] = 'headings'
        tabla.column("ID Estudiante", width=150)
        tabla.column("ID Asignatura", width=150)
        tabla.column("Nota", width=100)

        setattr(self, "tabla_nota", tabla)

        # Configuración de expansión
        resultados_frame.grid_rowconfigure(1, weight=1)
        resultados_frame.grid_columnconfigure(4, weight=1)

    def crear_campo(self, frame, texto, fila):
        label = tk.Label(frame, text=f"{texto}: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        label.grid(row=fila, column=0, pady=10, sticky="w")

        entry = tk.Entry(frame, font=("Arial", 15), bd=5, relief=tk.GROOVE)
        entry.grid(row=fila, column=1, pady=10, padx=30, sticky="w")
        setattr(self, f"txt_{texto.lower().replace(' ', '_')}", entry)

