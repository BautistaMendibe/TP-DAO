from prestamo import Prestamo

class Socio:
    def __init__(self, nombre, numeroSocio):
        self._nombre = nombre
        self._numeroSocio = numeroSocio
        self._prestamosDeLibro: [Prestamo] = []
        
    @property
    def numeroSocio(self):
        return self._numeroSocio
    
    @property
    def nombre(self):
        return self._nombre
    
    def agregarPrestamo(self, prestamo: Prestamo):
        pass
        #Aca debería entrar a la bd y consultar por todos los prestamos asociados a este número de socio, ver si son 3 o si alguno esta con demora y no darselo
        #En realidad deberia registrar los prestamos en una lista y eso deberia estar guardado en la base de datos
        
    def registrarDevolucion(self, prestamo: Prestamo):
        pass
        #Aca deberia sacar el prestamo del socio
        
    def mostrarPrestamoDemorado(self):
        pass
        #Recorre todos los prestamos y devuelve los Pretamos con el atributo diasRetraso positivo