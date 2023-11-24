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
        # Verificar si ya existe un libro con el mismo título
        if existe_libro_con_titulo(titulo):
            return False
        else:
            insertar_libro(libro)
            return True

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
        
    def registrarPrestamo(self, numSocio: int, codigoLibro: int, diasDevolucion):

        socio: Socio = consultar_socio(numSocio)
        libro: Libro = buscar_libro_por_codigo(codigoLibro)
        diasDevolucion = int(diasDevolucion)

        # Si el libro y el socio existen se registra el prestamo, si no no
        if (libro != None and socio!= None and libro.estado == "Disponible"):
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
            else:
                messagebox.showerror("Error", "No se pudo registrar el préstamo. El Socio no existe")
                return False
