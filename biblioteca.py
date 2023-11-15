from libro import Libro
from socio import Socio
from sql import insertar_socio

class Biblioteca:

    def __init__(self):
        self._libros: [Libro] = []
        self._socios: [Socio] = []
        #No se si que los prestamos tengan socios o que los socios tengan prestamos
        #self._prestamos = ()
        
    def aggLibro(self, codigo, titulo, precioReposicion):
        libro: Libro = Libro(codigo=codigo, titulo=titulo, precioReposicion=precioReposicion)
        self._libros.append(libro)

    def buscarLibro(self, titulo):
        for i in self._libros:
            if i.titulo() == titulo:
                return i
        return 0
    
    def buscarSocio(self, numSocio):
        for i in self._socios:
            if i.numeroSocio() == numSocio:
                return i
        return 0
        
    def aggSocio(self, nombre: str):
        socio: Socio = Socio(nombre=nombre)
        self._socios.append(socio)
        insertar_socio(socio)
    
    def librosCadEstado(self):
        d = 0
        p = 0
        e = 0
        for i in self._libros:
            if i.estado() == "Disponible":
                d += 1
            elif i.estado() == "Prestado":
                p += 1
            elif i.estado() == "Extraviado":
                e += 1
        return f"Disponible:{d} \nPrestado:{p} \nExtraviado:{e}"
    
    def precioLibrosExtraviados(self):
        precio = 0
        for libro in self._libros:
            if libro.estado() == "Extraviado":
                precio += libro.precioReposicion()
        return f"Precio total para reposición de libros extraviados: ${precio}"
                
    
    def solicitantesDeLibro(self, titulo):
        l = []
        for i in self._socios:
            if i.pidioLibro(titulo) != None:
                l.append(i.pidioLibro(titulo))
        return l
        #Supongo que se refieren a los socios que se llevaron un mismo libro
        
    def listPrestamosDemorados(self):
        for i in self._socios:
            i.mostrarPrestamoDemorado()