from tkinter import messagebox
from libro import Libro
from socio import Socio
from prestamo import Prestamo
from sql import *
from datetime import datetime, timedelta

class Biblioteca:

    def __init__(self):
        self._libros: [Libro] = []
        self._socios: [Socio] = []
        self._prestamos: [Prestamo] = []
        
    def aggLibro(self, titulo, precioReposicion):
        libro: Libro = Libro(titulo=titulo, precioReposicion=precioReposicion)
        self._libros.append(libro)
        insertar_libro(libro)

    def consultarLibro(self, codigo):
        libro = buscar_libro_por_codigo(codigo)
        return libro
    
    def consultarLibroxTitulo(self, titulo):
        libro = buscar_libros_por_titulo(titulo)
        return libro
    
    def eliminarLibro(self, codigo: int):
        libro = eliminar_libro(codigo)
        return libro
    
    def consultarSocio(self, numSocio: int):
        socio = consultar_socio(numSocio)
        return socio
        
    def aggSocio(self, nombre: str):
        socio: Socio = Socio(nombre=nombre)
        self._socios.append(socio)
        # Verificar si ya existe un socio con el mismo nombre
        if existe_socio_con_nombre(nombre):
            return False
        else:
            insertar_socio(socio)
            return True
    
    def eliminarSocio(self, numeroSocio: int):
        socio = eliminar_socio(numeroSocio)
        return socio
    
    def librosCadEstado(self):
        return listar_cantidad_libros_estado()
    
    def precioLibrosExtraviados(self):
        return sumatoria_precio_reposicion_librExtraviados()
                
    def solicitantesDeLibro(self, titulo):
        return solicitantes_por_titulo_libro(titulo)
        
    def listarPrestamosDemorados(self):
        return listar_prestamos_demorados()
            
    def prestamosDeSocio(self, numSocio):
        return listar_prestamos_por_socio(numeroSocio=numSocio)
    
    def actualizar_estado_libro(libro, estado: str):
        actualizar_estado_libro(libro, estado)
        
    def registrarDevolucion(self, numSocio: int, codigoLibro: int):
        socio: Socio = consultar_socio(numSocio)
        libro: Libro = buscar_libro_por_codigo(codigoLibro)
        
        if (buscar_prestamo(numeroSocio=numSocio, codigoLibro=codigoLibro) and libro.estado != "Disponible"):
            respuesta = buscar_prestamo(numeroSocio=numSocio, codigoLibro=codigoLibro)
            prestamo: Prestamo = Prestamo(idPrestamo=respuesta[0], fechaPrestamo=datetime.strptime(respuesta[1], '%Y-%m-%d %H:%M:%S'), fechaDevolucion=datetime.strptime(respuesta[2], '%Y-%m-%d %H:%M:%S'), libro=libro, socio=socio)
            actualizar_estado_libro(prestamo.libro, "Disponible")
            registrar_devolucion(prestamo.idPrestamo, prestamo.fechaDevolucion, prestamo.diasRetraso)
            return True
        else:
            return False
        
    def registrarPrestamo(self, numSocio: int, codigoLibro: int, diasDevolucion):

        socio: Socio = consultar_socio(numSocio)
        libro: Libro = buscar_libro_por_codigo(codigoLibro)
        diasDevolucion = int(diasDevolucion)

        prestamos = listar_prestamos_por_socio(numeroSocio=numSocio)
        count = 0
        for prestamo in prestamos:
            if prestamo.devuelto == False:
                count += 1
        # Si el libro y el socio existen se registra el prestamo, si no no
        if (libro != None and socio!= None and libro.estado == "Disponible" and count < 3):
            fecha_actual = datetime.now().replace(microsecond=0)
            fecha_devolucion = fecha_actual + timedelta(days=diasDevolucion)
            #prestamo: Prestamo = Prestamo(diasDevolucion, libro, socio)
            registrar_prestamo(numSocio, libro.codigo, fecha_actual, fecha_devolucion)
            actualizar_estado_libro(libro, "Prestado")
            return True
        else:
            if libro == None:
                messagebox.showerror("Error", "No se pudo registrar el préstamo. El Libro no existe")
                return False

            elif libro.estado != "Disponible":
                messagebox.showerror("Error", f"No se pudo registrar el préstamo. El libro {libro.titulo} no está disponible")
                return False
            elif count == 3:
                messagebox.showerror("Error", f"No se pudo registrar el préstamo. El socio {socio.nombre} Ya tiene 3 prestamos no devueltos")
                return False
            else:
                messagebox.showerror("Error", "No se pudo registrar el préstamo. El Socio no existe")
                return False
            
    def regitrar_extraviado(self):
        prestamos = listar_prestamos_demorados()
        # Verificar si la lista está vacía
        if prestamos is not None:
            for prestamo in prestamos:
                if prestamo.diasRetraso >= 30:
                    actualizar_estado_libro(prestamo.libro, "Extraviado")
            return True
        else:
            return False
    