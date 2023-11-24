from libro import Libro
from socio import Socio
from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, fechaDevolucion: datetime, libro: Libro, socio: Socio, idPrestamo=None, fechaPrestamo=None, devuelto: bool=False):
        if idPrestamo is None:
            # Inicialización cuando no se proporciona el ID del préstamo
            self._idPrestamo = None
            self._fechaPrestamo = datetime.now().replace(microsecond=0).date()
        else:
            # Inicialización cuando se proporciona el ID del préstamo
            self._idPrestamo = idPrestamo
            self._fechaPrestamo = fechaPrestamo

        # Resto de la inicialización común
        self._fechaDevolucion = fechaDevolucion
        self._diasRetraso = self.diasRetraso
        self._socio = socio
        self._devuelto = devuelto
        self._libro = libro
    
    def __str__(self) -> str:
        return f"Id de prestamo: {self._idPrestamo} Fecha de prestamo: {self._fechaPrestamo} Fecha Devolución {self._fechaDevolucion} Dias de Retraso {self._diasRetraso} /nLibro {self._libro}"
    
    @property
    def idPrestamo(self):
        return self._idPrestamo
    
    @property
    def fechaPrestamo(self):
        return self._fechaPrestamo
    
    @property
    def fechaDevolucion(self):
        return self._fechaDevolucion
    
    @property
    def diasRetraso(self):
        # Si la fecha de prestamo más los días que tiene para devolver es menor a la fecha actual no hay retraso
        if self.fechaDevolucion.date() >= datetime.now().date():
            return 0
        else:
            # El retraso se calcula como la fecha de hoy menos la fecha del prestamo más los días que nos dieron para devolverlo.
            retraso = datetime.now().date() - (self.fechaDevolucion.date())
            return int(retraso.days)
    
    @property
    def devuelto(self):
        return self._devuelto
    
    @property
    def socio(self):
        return self._socio
    
    @property
    def libro(self):
        return self._libro
    
    
    def nombreCoincideLibro(self, titulo):
        if self._libro.titulo() == titulo:
            return True
        else:
            return False
    
    def registrarDevoluvion(self):
        if self._devuelto == False:
            if self._libro.estado == "Prestado":
                self._libro.estadoDisponible
                self._devuelto = True
                
    def esSocio(self, numeroSocio):
        if numeroSocio == self._socio.numeroSocio:
            return True
        
    def solicitantesLibros(self, titulo):
        if self._libro.titulo == titulo:
            return self._socio