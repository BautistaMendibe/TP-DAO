import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

def mostrar_mensaje(accion):
    print(f"Realizando acción: {accion}")

def registrar_socio():
    ventana_registro_socio = tk.Toplevel()
    ventana_registro_socio.title("Registrar socio")
    ventana_registro_socio.geometry("400x250")

    # Estilo para la etiqueta del título
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("Titulo.TLabel", font=("Arial bold", 12))

    label_titulo = ttk.Label(ventana_registro_socio, text="Registrar socio", style="Titulo.TLabel")
    label_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Estilo para las etiquetas y la entrada
    estilo_widget = ttk.Style()
    estilo_widget.configure("Estilo.TLabel", padding=5)
    estilo_widget.configure("Estilo.TEntry", padding=(5, 5, 5, 5))

    label_nombre = ttk.Label(ventana_registro_socio, text="Nombre:", style="Estilo.TLabel")
    label_nombre.grid(column=0, row=2)

    entry_nombre = ttk.Entry(ventana_registro_socio, style="Estilo.TEntry")
    entry_nombre.grid(column=1, row=2, sticky="ew")  # 'ew' significa que se expandirá horizontalmente

    # Configuración de la columna para expandirse
    ventana_registro_socio.columnconfigure(1, weight=1)

    # Estilo para el botón
    estilo_boton = ttk.Style()
    estilo_boton.configure("Estilo.TButton", padding=(10, 5, 10, 5), font=('Arial', 10, 'bold'))

    boton_registrar = ttk.Button(ventana_registro_socio, text="Registrar", command=lambda: mostrar_mensaje("Registrar socio"), style="Estilo.TButton")
    boton_registrar.grid(column=0, row=3, columnspan=2, pady=10)

    ventana_registro_socio.mainloop()

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
    menu_socios.add_command(label="Registrar socio", command=registrar_socio)
    menu_socios.add_command(label="Eliminar socio", command=lambda: mostrar_mensaje("Eliminar socio"))
    menu_socios.add_command(label="Consultar socio", command=lambda: mostrar_mensaje("Consultar socio"))
    # Opciones del menú de libros
    menu_libros.add_command(label="Registrar libro", command=lambda: mostrar_mensaje("Registrar libro"))
    menu_libros.add_command(label="Eliminar libro", command=lambda: mostrar_mensaje("Eliminar libro"))
    menu_libros.add_command(label="Consultar libro", command=lambda: mostrar_mensaje("Consultar libro"))

    ventana.config(menu=barra_menu)
    ventana.mainloop()