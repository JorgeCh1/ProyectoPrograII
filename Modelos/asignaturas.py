#Nombre del programa: Proyecto Final Programacion II
#Fecha de creación:
#Versión de Python en ejecución:
#Nombre del equipo de programación: Team Rapidito
#Nombre del líder del equipo: Chavez Aviles Jorge 
#Nombre de los integrantes:   Chavez Aviles Jorge 
                            # Soto Saborio Gerardo
                            # Rodriguez Marin Yulieth 
                            # Romero Meza Norman

import sqlite3

class Asignaturas:
    def __init__(self):
        self.conn = sqlite3.connect('gestor_academico.db')
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        """Crear la tabla de asignaturas si no existe."""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS asignaturas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT NOT NULL
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def agregar_asignatura(self, nombre, descripcion):
        """Agregar una nueva asignatura a la base de datos."""
        try:
            self.cursor.execute('''
                INSERT INTO asignaturas (nombre, descripcion)
                VALUES (?, ?)
            ''', (nombre, descripcion))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al agregar la asignatura: {e}")

    def modificar_asignatura(self, id, nombre=None, descripcion=None):
        """Modificar los datos de una asignatura existente en la base de datos."""
        set_clause = []
        params = []

        if nombre:
            set_clause.append("nombre = ?")
            params.append(nombre)
        if descripcion:
            set_clause.append("descripcion = ?")
            params.append(descripcion)

        params.append(id)
        set_clause_str = ", ".join(set_clause)

        try:
            self.cursor.execute(f'''
                UPDATE asignaturas
                SET {set_clause_str}
                WHERE id = ?
            ''', tuple(params))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al modificar la asignatura: {e}")

    def eliminar_asignatura(self, id):
        """Eliminar una asignatura de la base de datos por su ID."""
        try:
            self.cursor.execute('''
                DELETE FROM asignaturas
                WHERE id = ?
            ''', (id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar la asignatura: {e}")

    def obtener_asignaturas(self):
        """Obtener todas las asignaturas de la base de datos."""
        try:
            self.cursor.execute('''
                SELECT * FROM asignaturas
            ''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener las asignaturas: {e}")
            return []

    def obtener_asignatura_por_id(self, id):
        """Obtener una asignatura de la base de datos por su ID."""
        try:
            self.cursor.execute('''
                SELECT * FROM asignaturas
                WHERE id = ?
            ''', (id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error al obtener la asignatura por ID: {e}")
            return 
        
    def obtener_asignaturas_por_nombre(self, nombre):
        """Obtener un estudiante de la base de datos por su nombre."""
        try:
            self.cursor.execute('''
                SELECT * FROM asignaturas
                WHERE nombre = ?
            ''', (nombre,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener la asignatura por nombre: {e}")
            return []

    def cerrar_conexion(self):
        """Cerrar la conexión a la base de datos."""
        self.conn.close()
