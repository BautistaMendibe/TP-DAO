import sqlite3

# Clase para conectar la Base de datos. Se utiliza el patrón Singleton
class ManagerDataBase:
    _instance = None

    def __new__(cls):
        # Implementación del patrón Singleton: Garantiza que solo exista una instancia de la clase
        if cls._instance is None:
            cls._instance = super(ManagerDataBase, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect('libreria.db')
        return cls._instance
    
    def crear_tablas(self):
        # Método para crear las tablas en la base de datos si no existen
        cursor = self.conn.cursor()

        # Crear tabla 'libros'
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT, 
            precioReposicion REAL, 
            estado TEXT,
            borrado INTEGER)''')

        # Crear tabla 'socios'
        cursor.execute('''CREATE TABLE IF NOT EXISTS socios (
            numeroSocio INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT,
            borrado INTEGER)''')

        # Crear tabla 'prestamos' con claves foráneas
        cursor.execute('''CREATE TABLE IF NOT EXISTS prestamos (
            idPrestamo INTEGER PRIMARY KEY AUTOINCREMENT, 
            fechaPrestamo DATE, 
            diasDevolucion INTEGER, 
            diasRetraso INTEGER, 
            devuelto BOOLEAN, 
            socio_numeroSocio INTEGER, 
            libro_codigo INTEGER, 
            borrado INTEGER,
            FOREIGN KEY (socio_numeroSocio) REFERENCES socios (numeroSocio),
            FOREIGN KEY (libro_codigo) REFERENCES libros (codigo))''')

        # Confirmar cambios en la base de datos
        self.conn.commit()
        cursor.close()

    def consultar(self, consultaSQL):
        # Método para realizar consultas SELECT en la base de datos
        tabla = None
        cursor = self.conn.cursor()
        cursor.execute(consultaSQL)
        tabla = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return tabla

    def actualizar(self, consultaSQL):
        # Método para realizar operaciones de actualización en la base de datos (INSERT, UPDATE, DELETE)
        filasAfectadas = 0
        cursor = self.conn.cursor()
        try:
            cursor.execute(consultaSQL)
            filasAfectadas = cursor.rowcount
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error de SQLite: {e}")
        finally:
            cursor.close()
        return filasAfectadas

    