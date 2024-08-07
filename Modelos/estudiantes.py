# modelo/estudiantes.py

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

class Estudiantes:
    def __init__(self):
        self.conn = sqlite3.connect('gestor_academico.db')
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        """Crear la tabla de estudiantes si no existe."""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS estudiantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    correo TEXT NOT NULL UNIQUE,
                    fecha_nacimiento TEXT NOT NULL,
                    direccion TEXT NOT NULL,
                    genero TEXT NOT NULL
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def agregar_estudiante(self, nombre, telefono, correo, fecha_nacimiento, direccion, genero):
        """Agregar un nuevo estudiante a la base de datos."""
        try:
            self.cursor.execute('''
                INSERT INTO estudiantes (nombre, telefono, correo, fecha_nacimiento, direccion, genero)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (nombre, telefono, correo, fecha_nacimiento, direccion, genero))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al agregar el estudiante: {e}")

    def modificar_estudiante(self, id, nombre=None, telefono=None, correo=None, fecha_nacimiento=None, direccion=None, genero=None):
        """Modificar los datos de un estudiante existente en la base de datos."""
        set_clause = []
        params = []

        if nombre:
            set_clause.append("nombre = ?")
            params.append(nombre)
        if telefono:
            set_clause.append("telefono = ?")
            params.append(telefono)
        if correo:
            set_clause.append("correo = ?")
            params.append(correo)
        if fecha_nacimiento:
            set_clause.append("fecha_nacimiento = ?")
            params.append(fecha_nacimiento)
        if direccion:
            set_clause.append("direccion = ?")
            params.append(direccion)
        if genero:
            set_clause.append("genero = ?")
            params.append(genero)

        params.append(id)
        set_clause_str = ", ".join(set_clause)

        try:
            self.cursor.execute(f'''
                UPDATE estudiantes
                SET {set_clause_str}
                WHERE id = ?
            ''', tuple(params))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al modificar el estudiante: {e}")

    def eliminar_estudiante(self, id):
        """Eliminar un estudiante de la base de datos por su ID."""
        try:
            self.cursor.execute('''
                DELETE FROM estudiantes
                WHERE id = ?
            ''', (id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar el estudiante: {e}")

    def obtener_estudiantes(self):
        """Obtener todos los estudiantes de la base de datos."""
        try:
            self.cursor.execute('''
                SELECT * FROM estudiantes
            ''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener los estudiantes: {e}")
            return []

    def obtener_estudiante_por_id(self, id):
        """Obtener un estudiante de la base de datos por su ID."""
        try:
            self.cursor.execute('''
                SELECT * FROM estudiantes
                WHERE id = ?
            ''', (id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error al obtener el estudiante por ID: {e}")
            return None
    
    def obtener_estudiante_por_nombre(self, nombre):
        """Obtener un estudiante de la base de datos por su nombre."""
        try:
            self.cursor.execute('''
                SELECT * FROM estudiantes
                WHERE nombre = ?
            ''', (nombre,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener el estudiante por nombre: {e}")
            return []

    def cerrar_conexion(self):
        """Cerrar la conexión a la base de datos."""
        self.conn.close()
