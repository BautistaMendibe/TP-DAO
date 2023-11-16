class Libro:
    def __init__(self, titulo, precioReposicion, codigo=None, estado=None):
        if codigo is None:
            # Inicialización cuando no se proporciona el código
            self._codigo = None
            self._estado = "Disponible"
        else:
            # Inicialización cuando se proporciona el código
            self._codigo = codigo
            self._estado = estado
        # Resto de la inicialización común
        self._titulo = titulo
        self._precioReposicion = precioReposicion
        
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def precioReposicion(self):
        return self._precioReposicion
    
    @property
    def estado(self):
        return self._estado
    
    def __str__(self) -> str:
        return f"Datos del Libro:\n\tCódigo: {self.codigo}\n\tTítulo: {self.titulo}\n\tPrecio de Reposición: ${str(self.precioReposicion)}\n\tEstado: {self.estado}"

        
    #para ver si esta extraviado tenemos que ingresar a bd y verificar si hay algun prestamo con su codigo y que más de 30 días de demora.
    