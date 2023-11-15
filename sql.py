from managerDB import ManagerDataBase
from libro import Libro
from socio import Socio

# Funciones para la gestión de LIBROS

def insertar_libro(libro):
    # Conectar a la base de datos
    db_manager = ManagerDataBase()
    
    # Obtener datos del libro
    titulo = str(libro.titulo)
    precio_reposicion = float(libro.precioReposicion)
    estado = str(libro.estado)
    
    # Crear y ejecutar la consulta SQL para insertar el libro
    query = f"INSERT INTO libros (titulo, precioReposicion, estado, borrado) " \
            f"VALUES ('{titulo}', {precio_reposicion}, '{estado}', 0)"
    db_manager.actualizar(query)

def actualizar_libro(libro):
    db_manager = ManagerDataBase()
    codigo = int(libro.codigo)
    titulo = str(libro.titulo)
    precio_reposicion = float(libro.precioReposicion)
    estado = str(libro.estado)
    query = f"UPDATE libros SET titulo = '{titulo}', precioReposicion = {precio_reposicion}, estado = '{estado}' WHERE codigo = {codigo}"
    db_manager.actualizar(query)

def eliminar_libro(codigo):
    db_manager = ManagerDataBase()
    query = f"UPDATE libros SET borrado = 1 WHERE codigo = {codigo}"
    db_manager.actualizar(query)

def buscar_libros_por_titulo(titulo):
    query = f"SELECT * FROM libros WHERE titulo = '{titulo}'"
    db_manager = ManagerDataBase()
    resultados = db_manager.consultar(query)
    libros = [Libro(codigo=row[0], titulo=row[1], precioReposicion=row[2], estado=row[3]) for row in resultados]
    return libros

# Funciones para la administración de SOCIOS

def insertar_socio(socio):
    # Conectar a la base de datos
    db_manager = ManagerDataBase()
    
    # Obtener datos del socio
    nombre = str(socio.nombre)
    
    # Crear y ejecutar la consulta SQL para insertar el socio
    query = f"INSERT INTO socios (nombre, borrado) VALUES ('{nombre}', 0)"
    db_manager.actualizar(query)

def actualizar_socio(socio):
    db_manager = ManagerDataBase()
    numero_socio = int(socio.numeroSocio)
    nombre = str(socio.nombre)
    query = f"UPDATE socios SET nombre = '{nombre}' WHERE numeroSocio = {numero_socio}"
    db_manager.actualizar(query)

def eliminar_socio(numeroSocio):
    db_manager = ManagerDataBase()
    query = f"UPDATE socios SET borrado = 1 WHERE numeroSocio = {numeroSocio}"
    db_manager.actualizar(query)

def consultar_socio(numeroSocio):
    query = f"SELECT * FROM socios WHERE numeroSocio = {numeroSocio}"
    db_manager = ManagerDataBase()
    resultados = db_manager.consultar(query)
    socio_encontrado = resultados[0]
    socio: Socio = Socio(socio_encontrado)
    return socio_encontrado

def listar_socios():
    query = "SELECT * FROM socios"
    db_manager = ManagerDataBase()
    resultados = db_manager.consultar(query)
    socios = [Socio(numeroSocio=row[0], nombre=row[1]) for row in resultados]
    return socios


# Funciones para la registración de PRESTAMOS y DEVOLUCIONES

def registrar_prestamo(socio_id, libro_id, fecha_prestamo, dias_devolucion):
    # Conectar a la base de datos
    db_manager = ManagerDataBase()
    
    # Crear y ejecutar la consulta SQL para registrar un préstamo
    query = f"INSERT INTO prestamos (socio_numeroSocio, libro_codigo, fechaPrestamo, diasDevolucion, devuelto) " \
            f"VALUES ({socio_id}, {libro_id}, '{fecha_prestamo}', {dias_devolucion}, 0)"
    db_manager.actualizar(query)

def registrar_devolucion(prestamo_id, fecha_devolucion, dias_retraso):
    db_manager = ManagerDataBase()
    query = f"UPDATE prestamos SET fechaPrestamo = '{fecha_devolucion}', diasRetraso = {dias_retraso}, devuelto = 1 " \
            f"WHERE idPrestamo = {prestamo_id}"
    db_manager.actualizar(query)

# Funciones para la actualización de préstamos

def actualizar_prestamo(idPrestamo, fechaPrestamo, diasDevolucion, socio_numeroSocio, libro_codigo, devuelto, diasRetraso):
    # Conectar a la base de datos
    db_manager = ManagerDataBase()
    
    # Crear y ejecutar la consulta SQL para actualizar un préstamo
    query = f"UPDATE prestamos SET fechaPrestamo = '{fechaPrestamo}', diasDevolucion = {diasDevolucion}, " \
            f"socio_numeroSocio = {socio_numeroSocio}, libro_codigo = {libro_codigo}, devuelto = {devuelto}, " \
            f"diasRetraso = {diasRetraso} WHERE idPrestamo = {idPrestamo}"
    db_manager.actualizar(query)

# Función para eliminar un préstamo
def eliminar_prestamo(idPrestamo):
    db_manager = ManagerDataBase()
    query = f"DELETE FROM prestamos WHERE idPrestamo = {idPrestamo}"
    db_manager.actualizar(query)

# Funciones para los REPORTES

def sumatoria_precio_reposicion_librExtraviados():
    db_manager = ManagerDataBase()
    query = "SELECT SUM(precioReposicion) AS sumatoria FROM libros WHERE estado = 'Extraviado'"
    resultados = db_manager.consultar(query)
    return resultados

def listar_cantidad_libros_estado():
    # Conectar a la base de datos
    db_manager = ManagerDataBase()
    
    # Crear y ejecutar la consulta SQL para listar la cantidad de libros por estado
    query = "SELECT estado, COUNT(*) AS cantidad FROM libros GROUP BY estado"
    resultados = db_manager.consultar(query)
    return resultados


def solicitantes_por_titulo_libro(titulo):
    db_manager = ManagerDataBase()
    query = f"SELECT s.numeroSocio, s.nombre FROM socios s " \
            f"INNER JOIN prestamos p ON s.numeroSocio = p.socio_numeroSocio " \
            f"INNER JOIN libros l ON p.libro_codigo = l.codigo " \
            f"WHERE l.titulo = '{titulo}'"
    resultados = db_manager.consultar(query)
    return resultados

def listar_prestamos_demorados():
    db_manager = ManagerDataBase()
    query = "SELECT p.idPrestamo, p.fechaPrestamo, p.diasDevolucion, p.devuelto, " \
            "l.codigo AS codigo_libro, l.titulo AS titulo_libro, s.numeroSocio, s.nombre AS nombre_socio " \
            "FROM prestamos p " \
            "INNER JOIN libros l ON p.libro_codigo = l.codigo " \
            "INNER JOIN socios s ON p.socio_numeroSocio = s.numeroSocio " \
            "WHERE p.devuelto = 0 AND DATE('now') > DATE(p.fechaPrestamo, '+' || p.diasDevolucion || ' days')"
    resultados = db_manager.consultar(query)
    return resultados

def listar_prestamos_por_socio(numeroSocio):
    db_manager = ManagerDataBase()
    query = f"SELECT p.idPrestamo, p.fechaPrestamo, p.diasDevolucion, p.devuelto, " \
            f"l.codigo AS codigo_libro, l.titulo AS titulo_libro " \
            f"FROM prestamos p " \
            f"INNER JOIN libros l ON p.libro_codigo = l.codigo " \
            f"WHERE p.socio_numeroSocio = {numeroSocio}"
    resultados = db_manager.consultar(query)
    return resultados
