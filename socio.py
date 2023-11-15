from prestamo import Prestamo
from libro import Libro

class Socio:
    def __init__(self, nombre):
        self._numeroSocio = None
        self._nombre = nombre
        self._prestamosDeLibro: [Prestamo] = []
    
    # def __init__(self, numeroSocio: int, nombre: str):
    #     self._numeroSocio = numeroSocio
    #     self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def numeroSocio(self):
        return self._numeroSocio
    
    def agregarPrestamo(self, diasDevolucion, libro: Libro):
        if self._prestamosDeLibro.length() > 3:
            for i in self._prestamosDeLibro:
                if i.diasRetraso() == 0:
                    prestamo: Prestamo = Prestamo(diasDevolucion = diasDevolucion, libro = libro)
                    self._prestamosDeLibro.append(prestamo)
                else:
                    print("Tiene prestamos con demora")
                    break
        else:
            print("No puede tener 3 prestamos activos a la vez")
        #Aca debería entrar a la bd y consultar por todos los prestamos asociados a este número de socio, ver si son 3 o si alguno esta con demora y no darselo
        #En realidad deberia registrar los prestamos en una lista y eso deberia estar guardado en la base de datos
        
    def registrarDevolucion(self, prestamo: Prestamo):
        for i in self._prestamosDeLibro:
            if i.idPrestamo() == prestamo.idPrestamo():
                i.registrarDevolucion()
                
        #Aca deberia cambiar el estado del libro del prestamo del socio y cambiar el estado del prestamo
        
    def mostrarPrestamoDemorado(self):
        for i in self._prestamosDeLibro:
            if i.diasRetraso() > 0:
                print(i)
        #Recorre todos los prestamos y devuelve los Pretamos con el atributo diasRetraso positivo
        
    def pidioLibro(self, titulo):
        for i in self._prestamosDeLibro:
            if i.nombreCoincideLibro(titulo):
                return self._nombre
            
    def listarPrestamos(self):
        for i in self._prestamosDeLibro:
            print(i)