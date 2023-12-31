from datetime import datetime
from managerDB import ManagerDataBase
from libro import Libro
from socio import Socio
from prestamo import Prestamo

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
    
def existe_libro_con_titulo(titulo):
    # Verificar si ya existe un libro con el mismo título en la base de datos
    db_manager = ManagerDataBase()
    query = f"SELECT * FROM libros WHERE titulo = '{titulo}' AND borrado = 0"
    resultado = db_manager.consultar(query)
    return len(resultado) > 0

def existe_socio_con_nombre(nombre):
    # Verificar si ya existe un libro con el mismo título en la base de datos
    db_manager = ManagerDataBase()
    query = f"SELECT * FROM socios WHERE nombre = '{nombre}' AND borrado = 0"
    resultado = db_manager.consultar(query)
    return len(resultado) > 0

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
    query = f"SELECT * FROM libros WHERE codigo = {codigo}"
    eliminacion = f"UPDATE libros SET borrado = 1 WHERE codigo = {codigo}"
    resultados = db_manager.consultar(query)
    if not resultados or (len(resultados) > 0 and resultados[0][4] == 1):
        return None
    libro_encontrado = resultados[0]
    libro: Libro = Libro(titulo= libro_encontrado[1], precioReposicion=libro_encontrado[2], codigo=libro_encontrado[0], estado=libro_encontrado[3])
    db_manager.actualizar(eliminacion)
    return libro

def buscar_libros_por_titulo(titulo):
    query = f"SELECT * FROM libros WHERE titulo = '{titulo}'"
    db_manager = ManagerDataBase()
    resultados = db_manager.consultar(query)
    libros = [Libro(codigo=row[0], titulo=row[1], precioReposicion=row[2], estado=row[3]) for row in resultados]
    
    if libros:
        return libros
    else:
        return None

def buscar_libro_por_codigo(codigo_libro):
    query = f"SELECT * FROM libros WHERE codigo = {codigo_libro}"
    db_manager = ManagerDataBase()
    resultados = db_manager.consultar(query)
    if not resultados or (len(resultados) > 0 and resultados[0][4] == 1):
        return None  
    libro_encontrado = resultados[0]
    libro: Libro = Libro(codigo=libro_encontrado[0] , titulo=libro_encontrado[1], precioReposicion=libro_encontrado[2], estado=libro_encontrado[3])
    return libro

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
    query = f"SELECT * FROM socios WHERE numeroSocio = {numeroSocio}"
    eliminacion = f"UPDATE socios SET borrado = 1 WHERE numeroSocio = {numeroSocio}"
    resultados = db_manager.consultar(query)
    if not resultados or (len(resultados) > 0 and resultados[0][2] == 1):
        return None
    socio_encontrado = resultados[0]
    socio: Socio = Socio(numeroSocio=socio_encontrado[0], nombre=socio_encontrado[1])
    db_manager.actualizar(eliminacion)
    return socio

def consultar_socio(numeroSocio):
    query = f"SELECT * FROM socios WHERE numeroSocio = {numeroSocio}"
    db_manager = ManagerDataBase()
    resultados = db_manager.consultar(query)

    # Verificar si no hay resultados o si la condición se cumple
    if not resultados or resultados[0][2] == 1:
        return None

    # Crear objeto Socio si se encuentran resultados
    socio_encontrado = resultados[0]
    socio = Socio(numeroSocio=socio_encontrado[0], nombre=socio_encontrado[1])
    return socio

def listar_socios():
    query = "SELECT * FROM socios"
    db_manager = ManagerDataBase()
    resultados = db_manager.consultar(query)
    socios = [Socio(numeroSocio=row[0], nombre=row[1]) for row in resultados]
    return socios


# Funciones para la registración de PRESTAMOS y DEVOLUCIONES
def buscar_prestamo( numeroSocio, codigoLibro):
    db_manager = ManagerDataBase()
    query = f"SELECT * FROM prestamos " \
                f"WHERE socio_numeroSocio = {numeroSocio} AND libro_codigo = {codigoLibro}"
    resultados = db_manager.consultar(query)

    # Verificar si hay resultados
    if resultados:
        # Devolver la información del préstamo
        return resultados[0]
    else:
        # No se encontró el préstamo
            return None


def registrar_prestamo(socio_id, libro_id, fecha_prestamo, fecha_devolucion):
    # Conectar a la base de datos
    db_manager = ManagerDataBase()
    # Crear y ejecutar la consulta SQL para registrar un préstamo
    query = f"INSERT INTO prestamos (socio_numeroSocio, libro_codigo, fechaPrestamo, fechaDevolucion, devuelto, borrado, diasRetraso) " \
            f"VALUES ({socio_id}, {libro_id}, '{fecha_prestamo}', '{fecha_devolucion}', 0, 0, 0)"
    db_manager.actualizar(query)

def registrar_devolucion(prestamo_id, fecha_devolucion, dias_retraso):
    db_manager = ManagerDataBase()
    query = f"UPDATE prestamos SET fechaPrestamo = '{fecha_devolucion}', diasRetraso = {dias_retraso}, devuelto = 1 " \
            f"WHERE idPrestamo = {prestamo_id}"
    db_manager.actualizar(query)

# Funciones para la actualización de préstamos

def actualizar_prestamo(idPrestamo, fechaPrestamo, fechaDevolucion, socio_numeroSocio, libro_codigo, devuelto, diasRetraso):
    # Conectar a la base de datos
    db_manager = ManagerDataBase()
    
    # Crear y ejecutar la consulta SQL para actualizar un préstamo
    query = f"UPDATE prestamos SET fechaPrestamo = '{fechaPrestamo}', fechaDevolucion = {fechaDevolucion}, " \
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
    return resultados[0][0] if resultados and resultados[0] and resultados[0][0] is not None else None

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
    
    solicitudes = []
    for i in resultados:
        socio: Socio = Socio(numeroSocio=i[0], nombre=i[1])
        solicitudes.append(socio)
        
    return solicitudes

def listar_prestamos_demorados():
    db_manager = ManagerDataBase()
    query = "SELECT p.idPrestamo, p.fechaPrestamo, p.fechaDevolucion, p.devuelto, " \
            "l.codigo AS codigo_libro, l.titulo AS titulo_libro, l.precioReposicion, l.estado, s.numeroSocio, s.nombre AS nombre_socio " \
            "FROM prestamos p " \
            "INNER JOIN libros l ON p.libro_codigo = l.codigo " \
            "INNER JOIN socios s ON p.socio_numeroSocio = s.numeroSocio"

    resultados = db_manager.consultar(query)
    print(resultados)
    prestamosDem = []
    for i in resultados:
        libro: Libro = Libro(titulo=i[5], precioReposicion=i[6], codigo=i[4], estado=i[7])
        socio: Socio = Socio(nombre=i[9], numeroSocio=i[8])
        prestamo: Prestamo = Prestamo(fechaDevolucion=datetime.strptime(i[2], '%Y-%m-%d %H:%M:%S'), libro=libro, socio=socio, idPrestamo=i[0], fechaPrestamo=datetime.strptime(i[1], '%Y-%m-%d %H:%M:%S'))
        if prestamo.diasRetraso > 0:
            prestamosDem.append(prestamo)

    # Verificar si la lista está vacía y devolver None en ese caso
    if not prestamosDem:
        return None

    return prestamosDem

def listar_prestamos_por_socio(numeroSocio):
    db_manager = ManagerDataBase()
    query = f"SELECT p.idPrestamo, p.fechaPrestamo, p.fechaDevolucion, p.devuelto, " \
            f"l.codigo AS codigo_libro, l.titulo AS titulo_libro, l.precioReposicion, l.estado " \
            f"FROM prestamos p " \
            f"INNER JOIN libros l ON p.libro_codigo = l.codigo " \
            f"WHERE p.socio_numeroSocio = {numeroSocio}"
    resultados = db_manager.consultar(query)
    
    # Verificar si no hay resultados
    if resultados is None or not resultados:
        return None

    # Verificar si no hay resultados
    if resultados is None or not resultados:
        return None

    prestamos = []
    socio = consultar_socio(numeroSocio=numeroSocio)
    for i in resultados:
        libro = Libro(titulo=i[5], precioReposicion=i[6], codigo=i[4], estado=i[7])
        prestamo = Prestamo(fechaDevolucion=datetime.strptime(i[2], '%Y-%m-%d %H:%M:%S'), libro=libro, socio=socio, idPrestamo=i[0], fechaPrestamo=datetime.strptime(i[1], '%Y-%m-%d %H:%M:%S'))
        prestamos.append(prestamo)
    return prestamos



def actualizar_estado_libro(libro: Libro, estado: str):
    db_manager = ManagerDataBase()
    query = f"UPDATE libros SET estado = '{estado}' WHERE codigo = {libro.codigo}"
    db_manager.actualizar(query)
    