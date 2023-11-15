import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from socio import Socio
from biblioteca import Biblioteca

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

    boton_registrar = ttk.Button(ventana_registro_socio, text="Registrar", command=lambda: btn_registrar_socio(entry_nombre), style="Estilo.TButton")
    boton_registrar.grid(column=0, row=3, columnspan=2, pady=10)

    ventana_registro_socio.mainloop()

def btn_registrar_socio(entry_nombre: Entry):
    nombre = entry_nombre.get()
    biblioteca: Biblioteca = Biblioteca()
    biblioteca.aggSocio(nombre)
    
def eliminar_socio():
    ventana_registro_socio = tk.Toplevel()
    ventana_registro_socio.title("Eliminar socio")
    ventana_registro_socio.geometry("400x250")

    # Estilo para la etiqueta del título
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("Titulo.TLabel", font=("Arial bold", 12))

    label_titulo = ttk.Label(ventana_registro_socio, text="Eliminar socio", style="Titulo.TLabel")
    label_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Estilo para las etiquetas y la entrada
    estilo_widget = ttk.Style()
    estilo_widget.configure("Estilo.TLabel", padding=5)
    estilo_widget.configure("Estilo.TEntry", padding=(5, 5, 5, 5))

    label_numeroSocio = ttk.Label(ventana_registro_socio, text="Número de Socio:", style="Estilo.TLabel")
    label_numeroSocio.grid(column=0, row=2)

    entry_numeroSocio = ttk.Entry(ventana_registro_socio, style="Estilo.TEntry")
    entry_numeroSocio.grid(column=1, row=2, sticky="ew")  # 'ew' significa que se expandirá horizontalmente

    # Configuración de la columna para expandirse
    ventana_registro_socio.columnconfigure(1, weight=1)

    # Estilo para el botón
    estilo_boton = ttk.Style()
    estilo_boton.configure("Estilo.TButton", padding=(10, 5, 10, 5), font=('Arial', 10, 'bold'))

    boton_registrar = ttk.Button(ventana_registro_socio, text="Eliminar", command=lambda: btn_eliminar_socio(entry_numeroSocio), style="Estilo.TButton")
    boton_registrar.grid(column=0, row=3, columnspan=2, pady=10)

    ventana_registro_socio.mainloop()

def btn_eliminar_socio(entry_numeroSocio: Entry):
    numeroSocio = entry_numeroSocio.get()
    biblioteca: Biblioteca = Biblioteca()
    biblioteca.eliminarSocio(numeroSocio)
    
def consultar_socio():
    ventana_consultar_socio = tk.Toplevel()
    ventana_consultar_socio.title("Consultar socio")
    ventana_consultar_socio.geometry("400x250")

    # Estilo para la etiqueta del título
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("Titulo.TLabel", font=("Arial bold", 12))

    label_titulo = ttk.Label(ventana_consultar_socio, text="Consultar socio", style="Titulo.TLabel")
    label_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Estilo para las etiquetas y la entrada
    estilo_widget = ttk.Style()
    estilo_widget.configure("Estilo.TLabel", padding=5)
    estilo_widget.configure("Estilo.TEntry", padding=(5, 5, 5, 5))

    label_numeroSocio = ttk.Label(ventana_consultar_socio, text="Número de Socio:", style="Estilo.TLabel")
    label_numeroSocio.grid(column=0, row=2)

    entry_numeroSocio = ttk.Entry(ventana_consultar_socio, style="Estilo.TEntry")
    entry_numeroSocio.grid(column=1, row=2, sticky="ew")  # 'ew' significa que se expandirá horizontalmente

    # Configuración de la columna para expandirse
    ventana_consultar_socio.columnconfigure(1, weight=1)

    # Estilo para el botón
    estilo_boton = ttk.Style()
    estilo_boton.configure("Estilo.TButton", padding=(10, 5, 10, 5), font=('Arial', 10, 'bold'))

    boton_consultar = ttk.Button(ventana_consultar_socio, text="Consultar", command=lambda: btn_consultar_socio(ventana_consultar_socio, entry_numeroSocio), style="Estilo.TButton")
    boton_consultar.grid(column=0, row=3, columnspan=2, pady=10)

    ventana_consultar_socio.mainloop()

# Función que se ejecuta al hacer clic en el botón "Consultar"
def btn_consultar_socio(ventana_consultar_socio, entry_numeroSocio: Entry):
    numeroSocio = entry_numeroSocio.get()
    biblioteca: Biblioteca = Biblioteca()
    socio = biblioteca.consultarSocio(numeroSocio)
    
    # Crear etiquetas para mostrar la información del socio
    label_info_nombre = ttk.Label(ventana_consultar_socio, text=f"Nombre: " + socio.nombre, style="Estilo.TLabel")
    label_info_nombre.grid(column=0, row=4, columnspan=2, pady=5)
    
    boton_consultar = ttk.Button(ventana_consultar_socio, text="Consultar", command=btn_consultar_socio, style="Estilo.TButton")
    boton_consultar.grid(column=0, row=3, columnspan=2, pady=10)

    ventana_consultar_socio.mainloop()

    
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
    menu_socios.add_command(label="Eliminar socio", command=eliminar_socio)
    menu_socios.add_command(label="Consultar socio", command=consultar_socio)
    # Opciones del menú de libros
    menu_libros.add_command(label="Registrar libro", command=lambda: mostrar_mensaje("Registrar libro"))
    menu_libros.add_command(label="Eliminar libro", command=lambda: mostrar_mensaje("Eliminar libro"))
    menu_libros.add_command(label="Consultar libro", command=lambda: mostrar_mensaje("Consultar libro"))

    ventana.config(menu=barra_menu)
    ventana.mainloop()
    
inicio()