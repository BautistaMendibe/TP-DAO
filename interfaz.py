import tkinter
from tkinter import *

def x():
        print(f"Realizando acción:")

def inicio():
    ventana = Tk()
    ventana.title("Biblioteca UTN-FRC")
    ventana.geometry("800x500")

    barra_menu = Menu(ventana)

    menu_socios = Menu(barra_menu)
    barra_menu.add_cascade(label="Administración de socios", menu=menu_socios)
    menu_libros = Menu(barra_menu)
    barra_menu.add_cascade(label="Administración de libros", menu=menu_libros)
    menu_prestamos_devolucion = Menu(barra_menu)
    barra_menu.add_cascade(label="Registración de préstamos y devoluciones", menu=menu_prestamos_devolucion)

    # Opciones del menú de socios
    menu_socios.add_command(label="Registrar socio", command=x)
    menu_socios.add_command(label="Eliminar socio", command=x)
    menu_socios.add_command(label="Consultar socio", command=x)
    # Opciones del menú de libros
    menu_libros.add_command(label="Registrar libro", command=x)
    menu_libros.add_command(label="Eliminar libro", command=x)
    menu_libros.add_command(label="Consultar libro", command=x)

    

    ventana.mainloop()