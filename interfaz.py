import tkinter
from tkinter import *

def mostrar_mensaje(accion):
    print(f"Realizando acción: {accion}")

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
    menu_socios.add_command(label="Registrar socio", command=lambda: mostrar_mensaje("Registrar socio"))
    menu_socios.add_command(label="Eliminar socio", command=lambda: mostrar_mensaje("Eliminar socio"))
    menu_socios.add_command(label="Consultar socio", command=lambda: mostrar_mensaje("Consultar socio"))
    # Opciones del menú de libros
    menu_libros.add_command(label="Registrar libro", command=lambda: mostrar_mensaje("Registrar libro"))
    menu_libros.add_command(label="Eliminar libro", command=lambda: mostrar_mensaje("Eliminar libro"))
    menu_libros.add_command(label="Consultar libro", command=lambda: mostrar_mensaje("Consultar libro"))

    ventana.config(menu=barra_menu)
    ventana.mainloop()