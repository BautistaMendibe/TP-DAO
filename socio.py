

class Socio:
    def __init__(self, nombre):
        self._numeroSocio = None
        self._nombre = nombre
        
    def __init__(self, numeroSocio, nombre):
        self._numeroSocio = numeroSocio
        self._nombre = nombre
    
    # def __init__(self, numeroSocio: int, nombre: str):
    #     self._numeroSocio = numeroSocio
    #     self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def numeroSocio(self):
        return self._numeroSocio
       
    def mostrarPrestamoDemorado(self):
        for i in self._prestamosDeLibro:
            if i.diasRetraso() > 0:
                print(i)
        #Recorre todos los prestamos y devuelve los Pretamos con el atributo diasRetraso positivo
        
            
    def listarPrestamos(self):
        for i in self._prestamosDeLibro:
            print(i)