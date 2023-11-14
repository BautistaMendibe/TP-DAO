from libro import Libro
from socio import Socio

class Biblioteca:
    def __init__(self):
        self._libros = ()
        self._socios = ()
        #No se si que los prestamos tengan socios o que los socios tengan prestamos
        #self._prestamos = ()
        
    def aggLibro(self, libro: Libro):
        self._libros.append(libro)

    def buscarLibro(self, titulo):
        pass
    
    def buscarSocio(self, numSocio):
        pass
        
    def aggSocio(self, socio: Socio):
        self._socios.append(socio)
    
    def librosCadEstado(self):
        pass
    
    def precioLibrosExtraviados(self):
        pass
    
    def solicitantesDeLibro(self):
        pass
        #Supongo que se refieren a los socios que se llevaron un mismo libro
        
    def listPrestamosDemorados(self):
        pass