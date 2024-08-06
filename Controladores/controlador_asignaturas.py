#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo:  Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman   





from Modelos.asignaturas  import asignatura

class controlador_asignaturas:
    def __init__(self, vista):
        self.vista = vista
        self.asignaturas = []

    def agregar_asignatura(self):
        id = self.vista.txt_id.get()
        nombre = self.vista.txt_nombre.get()
        descripcion = self.vista.txt_descripcion.get("1.0", "end-1c")

        if id and nombre and descripcion:
            asignatura_nueva = asignatura(int(id), nombre, descripcion)
            self.asignaturas.append(asignatura_nueva)
            self.vista.mostrar_resultados(self.asignaturas)
            self.vista.limpiar_campos()
        else:
            print("Debes ingresar todos los campos")

    def modificar_asignatura(self):
        seleccionado = self.vista.tabla.selection()
        if seleccionado:
            id = self.vista.txt_id.get()
            nombre = self.vista.txt_nombre.get()
            descripcion = self.vista.txt_descripcion.get("1.0", "end-1c")

            if id and nombre and descripcion:
                for asignatura in self.asignaturas:
                    if asignatura.id == int(id):
                        asignatura.nombre = nombre
                        asignatura.descripcion = descripcion
                        self.vista.mostrar_resultados(self.asignaturas)
                        self.vista.limpiar_campos()
                        break
            else:
                print("Debes ingresar todos los campos")
        else:
            print("Debes seleccionar una asignatura")

    def eliminar_asignatura(self):
        seleccionado = self.vista.tabla.selection()
        if seleccionado:
            id = self.vista.tabla.item(seleccionado, "values")[0]
            for asignatura in self.asignaturas:
                if asignatura.id == int(id):
                    self.asignaturas.remove(asignatura)
                    self.vista.mostrar_resultados(self.asignaturas)
                    break
        else:
            print("Debes seleccionar una asignatura")

    def buscar_asignatura(self):
        id = self.vista.buscar_entry.get()
        if id:
            resultados = [asignatura for asignatura in self.asignaturas if asignatura.id == int(id)]
            self.vista.mostrar_resultados(resultados)
        else:
            print("Debes ingresar un ID")

    def mostrar_todos_asignaturas(self):
        self.vista.mostrar_resultados(self.asignaturas)