from libro import Libro
from socio import Socio
from prestamo import Prestamo
from sql import *
from datetime import datetime

class Biblioteca:

    def __init__(self):
        self._libros: [Libro] = []
        self._socios: [Socio] = []
        self._prestamos: [Prestamo] = []
        
    def aggLibro(self, titulo, precioReposicion):
        libro: Libro = Libro(titulo=titulo, precioReposicion=precioReposicion)
        self._libros.append(libro)
        insertar_libro(libro)

    def consultarLibro(self, titulo):
        libro = buscar_libros_por_titulo(titulo)
        return libro
    
    def eliminarLibro(self, codigo: int):
        eliminar_libro(codigo)
    
    def consultarSocio(self, numSocio: int):
        socio = consultar_socio(numSocio)
        return socio
        
    def aggSocio(self, nombre: str):
        socio: Socio = Socio(nombre=nombre)
        self._socios.append(socio)
        insertar_socio(socio)
    
    def eliminarSocio(self, numeroSocio: int):
        eliminar_socio(numeroSocio)
    
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
        
    def registrarPrestamo(self, diasDevolucion: int, libro: str, numSocio: int):

        socio: Socio = consultar_socio(numSocio)
        libro: Libro = buscar_libros_por_titulo(libro)

        # Si el libro y el socio existen se registra el prestamo, si no no
        if (libro.titulo != None and socio.nombre != None):
            fecha_actual = datetime.now()

            prestamo: Prestamo = Prestamo(diasDevolucion=diasDevolucion, libro=libro, socio=socio)
            registrar_prestamo(numSocio, libro.codigo, fecha_actual, diasDevolucion)
            actualizar_estado_libro(libro, "Prestado")
        