from libro import Libro

class Biblioteca:
    def __init__(self):
        self._libros = ()
        
    def aggLibro(self, libro: Libro):
        self._libros.append(libro)
    