from libro import Libro
from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, idPrestamo, fechaPrestamo, diasDevolucion, diasRetraso, devuelto, libro: Libro):
        self._idPrestamo = idPrestamo
        self._fechaPrestamo = fechaPrestamo
        self._diasDevolucion = diasDevolucion
        self._diasRetraso = diasRetraso
        self._devuelto = devuelto
        self._libro = libro
    
    @property
    def fechaPrestamo(self):
        return self._fechaPrestamo
    
    @property
    def diasDevolucion(self):
        return self._diasDevolucion
    
    @property
    def diasRetraso(self):
        # Si la fecha de prestamo más los días que tiene para devolver es menor a la fecha actual no hay retraso
        if self.fechaPrestamo.date + timedelta(days=self.diasDevolucion) <= datetime.now().date:
            return 0
        else:
            # El retraso se calcula como la fecha de hoy menos la fecha del prestamo más los días que nos dieron para devolverlo.
            retraso = datetime.now().date - (self.fechaPrestamo.date + timedelta(days=self.diasDevolucion))
            return retraso.days
    
    @property
    def devuelto(self):
        return self._devuelto
    
    
        
        
    

        
        
        