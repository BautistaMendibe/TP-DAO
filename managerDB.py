import datetime
import random
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
            fechaDevolucion DATE, 
            diasRetraso INTEGER, 
            devuelto BOOLEAN, 
            socio_numeroSocio INTEGER, 
            libro_codigo INTEGER, 
            borrado INTEGER,
            FOREIGN KEY (socio_numeroSocio) REFERENCES socios (numeroSocio),
            FOREIGN KEY (libro_codigo) REFERENCES libros (codigo))''')
        
    def insertar_registros_ejemplo(self):
        # Método para insertar registros de ejemplo en las tablas
        cursor = self.conn.cursor()

        # Insertar libros de ejemplo
        libros_ejemplo = [
            ('El Señor de los Anillos', 25.99, 'Disponible', 0),
            ('Cien años de soledad', 19.99, 'Prestado', 0),
            ('1984', 15.99, 'Disponible', 0),
            ('Harry Potter', 20.00, 'Disponible', 0),
            ('Don Quijote', 40.00, 'Disponible', 0),
            
        ]
        cursor.executemany('INSERT INTO libros (titulo, precioReposicion, estado, borrado) VALUES (?, ?, ?, ?)', libros_ejemplo)

        # Insertar socios de ejemplo
        socios_ejemplo = [
            ('Ramiro Hosman', 0),
            ('Bautista Mendibe', 0),
            ('Valentino Di Fulvio', 0),
            ('Debora Sandoval', 0),
            ('Juan Pérez', 0),
            ('María Gómez', 0),
            ('Carlos Rodríguez', 0),
            # Agrega más socios de ejemplo según sea necesario
        ]
        cursor.executemany('INSERT INTO socios (nombre, borrado) VALUES (?, ?)', socios_ejemplo)
        
        # Ejemplo 1
        prestamo_1 = (
            '2023-01-15',  # fechaPrestamo
            '2023-02-01',  # fechaDevolucion
            0,              # diasRetraso
            False,          # devuelto
            1,              # socio_numeroSocio
            1,              # libro_codigo
            0               # borrado
        )

        # Ejemplo 2
        prestamo_2 = (
            '2023-02-01',
            '2023-02-15',
            32,
            True,
            2,
            2,
            0
        )

        # Ejemplo 3
        prestamo_3 = (
            '2023-03-10',
            '2023-03-25',
            0,
            False,
            3,
            3,
            0
        )

        # Ejemplo 4
        prestamo_4 = (
            '2023-04-05',
            '2023-04-20',
            14,
            True,
            4,
            5,
            0
        )

        prestamos_ejemplo = [prestamo_1, prestamo_2, prestamo_3, prestamo_4]

        cursor.executemany('INSERT INTO prestamos (fechaPrestamo, fechaDevolucion, diasRetraso, devuelto, socio_numeroSocio, libro_codigo, borrado) VALUES (?, ?, ?, ?, ?, ?, ?)', prestamos_ejemplo)
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

    