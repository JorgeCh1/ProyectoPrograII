import sqlite3

class Notas:
    def __init__(self):
        self.conn = sqlite3.connect('gestor_academico.db')
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        """Crear la tabla de notas si no existe."""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS notas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_estudiante INTEGER NOT NULL,
                    id_asignatura INTEGER NOT NULL,
                    calificacion REAL NOT NULL,
                    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id),
                    FOREIGN KEY (id_asignatura) REFERENCES asignaturas(id)
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la tabla de notas: {e}")

    def agregar_nota(self, id_estudiante, id_asignatura, calificacion):
        """Agregar una nueva nota a la base de datos."""
        try:
            self.cursor.execute('''
                INSERT INTO notas (id_estudiante, id_asignatura, calificacion)
                VALUES (?, ?, ?)
            ''', (id_estudiante, id_asignatura, calificacion))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al agregar la nota: {e}")

    def modificar_nota(self, id, id_estudiante=None, id_asignatura=None, calificacion=None):
        """Modificar los datos de una nota existente en la base de datos."""
        set_clause = []
        params = []

        if id_estudiante:
            set_clause.append("id_estudiante = ?")
            params.append(id_estudiante)
        if id_asignatura:
            set_clause.append("id_asignatura = ?")
            params.append(id_asignatura)
        if calificacion:
            set_clause.append("calificacion = ?")
            params.append(calificacion)

        params.append(id)
        set_clause_str = ", ".join(set_clause)

        try:
            self.cursor.execute(f'''
                UPDATE notas
                SET {set_clause_str}
                WHERE id = ?
            ''', tuple(params))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al modificar la nota: {e}")

    def eliminar_nota(self, id):
        """Eliminar una nota de la base de datos por su ID."""
        try:
            self.cursor.execute('''
                DELETE FROM notas
                WHERE id = ?
            ''', (id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar la nota: {e}")

    def obtener_notas(self):
        """Obtener todas las notas de la base de datos."""
        try:
            self.cursor.execute('''
                SELECT * FROM notas
            ''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener las notas: {e}")
            return []

    def obtener_nota_por_id(self, id):
        """Obtener una nota de la base de datos por su ID."""
        try:
            self.cursor.execute('''
                SELECT * FROM notas
                WHERE id = ?
            ''', (id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error al obtener la nota por ID: {e}")
            return None
    
    def obtener_notas_por_estudiante(self, id_estudiante):
        """Obtener todas las notas de un estudiante por su ID."""
        try:
            self.cursor.execute('''
                SELECT * FROM notas
                WHERE id_estudiante = ?
            ''', (id_estudiante,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener las notas por estudiante: {e}")
            return []

    def obtener_notas_por_asignatura(self, id_asignatura):
        """Obtener todas las notas de una asignatura por su ID."""
        try:
            self.cursor.execute('''
                SELECT * FROM notas
                WHERE id_asignatura = ?
            ''', (id_asignatura,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener las notas por asignatura: {e}")
            return []

    def cerrar_conexion(self):
        """Cerrar la conexión a la base de datos."""
        self.conn.close()
