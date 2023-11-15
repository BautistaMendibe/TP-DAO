from libro import Libro
from socio import Socio
from sql import insertar_socio

class Biblioteca:

    def __init__(self):
        self._libros: [Libro] = []
        self._socios: [Socio] = []
        #No se si que los prestamos tengan socios o que los socios tengan prestamos
        #self._prestamos = ()
        
    def aggLibro(self, libro: Libro):
        self._libros.append(libro)

    def buscarLibro(self, titulo):
        pass
    
    def buscarSocio(self, numSocio):
        pass
        
    def aggSocio(self, nombre: str):
        socio: Socio = Socio(nombre=nombre)
        self._socios.append(socio)
        insertar_socio(socio)
    
    def librosCadEstado(self):
        pass
    
    def precioLibrosExtraviados(self):
        pass
    
    def solicitantesDeLibro(self, titulo):
        pass
        #Supongo que se refieren a los socios que se llevaron un mismo libro
        
    def listPrestamosDemorados(self):
        pass