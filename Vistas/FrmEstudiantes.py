# Frame de Estudiantes

from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self, ventana):
        self.ventana= ventana
        self.ventana.title("Sistema Gestión de Matrícula")
        self.ventana.geometry("1370x700+0+0")
        self.ventana.resizable(False, False)

        #Diseño del titulo principal 
        title=Label(self.ventana, text="Sistema Gestión de Matrícula", bd=10, relief=RAISED, font=("Arial", 40, "bold"), bg="navy", fg="lavender")
        title.pack(side=TOP)

        #Instancia de cuadro izquierdo (ingreso de datos)
        Ingreso_Datos_Frame =Frame(self.ventana, bd=4, relief=RIDGE, bg="navy")
        Ingreso_Datos_Frame.place(x=20, y=100, width=520, height=580)

        #CUADRO IZQUIERDO
        #Diseño del subtitulo control de estudiantes 
        m_title= Label(Ingreso_Datos_Frame, text="Control de Estudiantes", bg="lavender", fg="brown", relief=RAISED, font=("Arial", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        #Diseño del subtitulo 1 ID
        lbl_roll= Label(Ingreso_Datos_Frame, text="ID: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, sticky="w")

        #caja de texto ID
        txt_roll =Entry(Ingreso_Datos_Frame, font=("Arial", 15), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=30, sticky="w")

        #Diseño del subtitulo 2 nombre
        lbl_name= Label(Ingreso_Datos_Frame, text="Nombre: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, sticky="w")

        #caja de texto nombre
        txt_name =Entry(Ingreso_Datos_Frame, font=("Arial", 15), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=30, sticky="w")

        #Diseño del subtitulo 3 telefono
        lbl_telefono= Label(Ingreso_Datos_Frame, text="Teléfono: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        lbl_telefono.grid(row=3, column=0, pady=10, sticky="w")

        #caja de texto telefono
        txt_telefono =Entry(Ingreso_Datos_Frame, font=("Arial", 15), bd=5, relief=GROOVE)
        txt_telefono.grid(row=3, column=1, pady=10, padx=30, sticky="w")

        #Diseño del subtitulo 4 correo
        lbl_correo= Label(Ingreso_Datos_Frame, text="Correo: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        lbl_correo.grid(row=4, column=0, pady=10, sticky="w")

        #caja de texto correo
        txt_email =Entry(Ingreso_Datos_Frame, font=("Arial", 15), bd=5, relief=GROOVE)
        txt_email.grid(row=4, column=1, pady=10, padx=30, sticky="w")

        #Diseño del subtitulo 5 fecha de nacimiento 
        lbl_fechanac= Label(Ingreso_Datos_Frame, text="Fecha de nacimiento: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        lbl_fechanac.grid(row=5, column=0, pady=10, sticky="w")

        #caja de texto fecha de nacimiento 
        txt_fechanac =Entry(Ingreso_Datos_Frame, font=("Arial", 15), bd=5, relief=GROOVE)
        txt_fechanac.grid(row=5, column=1, pady=10, padx=30, sticky="w")

        #Diseño del subtitulo 6 direccion
        lbl_direccion= Label(Ingreso_Datos_Frame, text="Dirección: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        lbl_direccion.grid(row=6, column=0, pady=10, sticky="w")

        #caja de texto direccion
        self.txt_direccion=Text(Ingreso_Datos_Frame, width=30, height=4, font=("Arial", 10))
        self.txt_direccion.grid(row=6, column=1, pady=10, padx=30, sticky="w")

        #Diseño del subtitulo 7 genero
        lbl_genero= Label(Ingreso_Datos_Frame, text="Genero: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        lbl_genero.grid(row=7, column=0, pady=10, sticky="w")

        #combo box genero
        combo_genero=ttk.Combobox(Ingreso_Datos_Frame, width=9, font=("Arial", 15), state='readonly')
        combo_genero['values']=("Masculino", "Femenino", "Otro")
        combo_genero.grid(row=7, column=1, padx=30, pady=10)

        #Fondo donde contiene los botones
        btn_Frame=Frame(Ingreso_Datos_Frame, bd=4, relief=RIDGE, bg="dark grey")
        btn_Frame.place(x=115, y=510, width=320)

        #Boton agregar
        btn_agregar=Button(btn_Frame, text="Agregar", width=7)
        btn_agregar.grid(row=0, column=0, padx=10, pady=10)

        #Boton modificar
        btn_modificar=Button(btn_Frame, text="Modificar", width=7)
        btn_modificar.grid(row=0, column=1, padx=10, pady=10)

        #Boton eliminar
        btn_eliminar=Button(btn_Frame, text="Eliminar", width=7)
        btn_eliminar.grid(row=0, column=2, padx=10, pady=10)

        #Boton limpiar
        btn_limpiar=Button(btn_Frame, text="Limpiar", width=7)
        btn_limpiar.grid(row=0, column=3, padx=10, pady=10)

        #Instanciar cuadro derecho de resultados
        Resultados_Frame=Frame(self.ventana, bd=4, relief=RIDGE, bg="navy")
        Resultados_Frame.place(x=550, y=100, width=810, height=580)

        #CUADRO DERECHO 
        #Diseño subtitulo 1 derecho 
        lbl_buscar= Label(Resultados_Frame, text="Buscar por: ", bg="lavender", fg="brown", font=("Arial", 18, "bold"))
        lbl_buscar.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        #combo box buscar
        combo_buscar=ttk.Combobox(Resultados_Frame, width=10, font=("Arial", 15), state='readonly')
        combo_buscar['values']=("ID", "Nombre")
        combo_buscar.grid(row=0, column=2, padx=20, pady=10)

        #caja de texto para buscar
        txt_buscar=Entry(Resultados_Frame, width=20, font=("Arial", 11), bd=5, relief=GROOVE)
        txt_buscar.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        #Boton buscar
        btn_buscar=Button(Resultados_Frame, text="Buscar", width=7)
        btn_buscar.grid(row=0, column=4, padx=10, pady=10)

        #Boton mostrar todo 
        btn_mostrar=Button(Resultados_Frame, text="Mostrar todo", width=10)
        btn_mostrar.grid(row=0, column=5, padx=10, pady=10)

        #Creacion del cuadro de la tabla
        tabla_Frame=Frame(Resultados_Frame, bd=4, relief=RIDGE, bg="lavender")
        tabla_Frame.place(x=10, y=70, width=780, height=492)

        #barras de scroll en la tabla
        scroll_x=Scrollbar(tabla_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(tabla_Frame, orient=VERTICAL)

        tabla_estudiante=ttk.Treeview(tabla_Frame,columns=("ID", "Nombre", "Teléfono", "Correo", "Fecha Nac", "Dirección", "Género"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=tabla_estudiante.xview)
        scroll_y.config(command=tabla_estudiante.yview)

        #Encabezados de la tabla
        tabla_estudiante.heading("ID", text="ID")
        tabla_estudiante.heading("Nombre", text="Nombre")
        tabla_estudiante.heading("Teléfono", text="Teléfono")
        tabla_estudiante.heading("Correo", text="Correo")
        tabla_estudiante.heading("Fecha Nac", text="Fecha de Nacimiento")
        tabla_estudiante.heading("Dirección", text="Dirección")
        tabla_estudiante.heading("Género", text="Género")
        tabla_estudiante.pack(fill=BOTH, expand=1)
        
        #darle tamannos especificos a cada encabezado de las columnas de la tabla
        tabla_estudiante['show']='headings'
        tabla_estudiante.column("ID", width=100)
        tabla_estudiante.column("Nombre", width=100)
        tabla_estudiante.column("Teléfono", width=100)
        tabla_estudiante.column("Correo", width=100)
        tabla_estudiante.column("Fecha Nac", width=100)
        tabla_estudiante.column("Dirección", width=100)
        tabla_estudiante.column("Género", width=90)

ventana = Tk()
ob=Student(ventana)
ventana.mainloop()
