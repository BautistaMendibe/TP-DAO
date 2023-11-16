from libro import Libro
from socio import Socio
from prestamo import Prestamo
from sql import *

class Biblioteca:

    def __init__(self):
        self._libros: [Libro] = []
        self._socios: [Socio] = []
        self._prestamos: [Prestamo] = []
        
    def aggLibro(self, titulo, precioReposicion):
        libro: Libro = Libro(titulo=titulo, precioReposicion=precioReposicion)
        self._libros.append(libro)
        insertar_libro(libro)

    def buscarLibro(self, titulo):
        for i in self._libros:
            if i.titulo() == titulo:
                return i
        return 0
    
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
        for i in self._prestamos:
            if i.solicitantesLibro() != None:
                l.append(i.solicitantesLibro())
        return l
        #Supongo que se refieren a los socios que se llevaron un mismo libro
        
    def listarPrestamosDemorados(self):
        l = []
        for i in self._prestamos:
            if i.diasRetraso() > 0:
                return l.append(i)
            
    def prestamosDeSocio(self, numSocio):
        listaPrestamos = []
        for i in self._prestamos:
            if i.esSocio(numSocio):
                listaPrestamos.append(i)
        if listaPrestamos.length > 0:
            return listaPrestamos
        else:
            print("No tiene prestamos")
        
    def registrarPrestamo(self, diasDevolucion: int, libro: str, socio: int):

        

        prestamo: Prestamo = Prestamo(diasDevolucion=diasDevolucion, libro=libro, socio=socio)
        self._prestamos.append(prestamo)