from libro import Libro
from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, diasDevolucion, libro: Libro):
        self._idPrestamo = None
        self._fechaPrestamo = datetime.now().date
        self._diasDevolucion = diasDevolucion
        self._diasRetraso = 0
        self._devuelto = False
        self._libro = libro
    
    def __str__(self) -> str:
        return f"Id de prestamo: {self._idPrestamo} Fecha de prestamo: {self._fechaPrestamo}  
    Dias Devolucion {self._diasDevolucion} Dias de Retraso {self._diasRetraso} /nLibro {self._libro}"
    
    @property
    def idPrestamo(self):
        return self._idPrestamo
    
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