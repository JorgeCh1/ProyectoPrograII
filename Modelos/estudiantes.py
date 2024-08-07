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

    def agregar_estudiante(self, nombre, telefono, correo, fecha_nacimiento, direccion, genero):
        """Agregar un nuevo estudiante a la base de datos."""
        self.cursor.execute('''
            INSERT INTO estudiantes (nombre, telefono, correo, fecha_nacimiento, direccion, genero)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, telefono, correo, fecha_nacimiento, direccion, genero))
        self.conn.commit()

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

        self.cursor.execute(f'''
            UPDATE estudiantes
            SET {set_clause_str}
            WHERE id = ?
        ''', tuple(params))
        self.conn.commit()

    def eliminar_estudiante(self, id):
        """Eliminar un estudiante de la base de datos por su ID."""
        self.cursor.execute('''
            DELETE FROM estudiantes
            WHERE id = ?
        ''', (id,))
        self.conn.commit()

    def obtener_estudiantes(self):
        """Obtener todos los estudiantes de la base de datos."""
        self.cursor.execute('''
            SELECT * FROM estudiantes
        ''')
        return self.cursor.fetchall()

    def obtener_estudiante_por_id(self, id):
        """Obtener un estudiante de la base de datos por su ID."""
        self.cursor.execute('''
            SELECT * FROM estudiantes
            WHERE id = ?
        ''', (id,))
        return self.cursor.fetchone()
    
    def obtener_estudiante_por_nombre(self, Nombre):
        """Obtener un estudiante de la base de datos por su Nombre."""
        self.cursor.execute('''
            SELECT * FROM estudiantes
            WHERE Nombre = ?
        ''', (Nombre,))
        return self.cursor.fetchone()

    def cerrar_conexion(self):
        """Cerrar la conexión a la base de datos."""
        self.conn.close()
