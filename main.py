from interfaz import inicio
from managerDB import ManagerDataBase

if __name__ == "__main__":
    # Crear una instancia de ManagerDataBase
    db_manager = ManagerDataBase()

    # Crear las tablas en la base de datos si no existen
    db_manager.crear_tablas()
    
    inicio()