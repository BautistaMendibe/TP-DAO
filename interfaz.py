import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from socio import Socio
from biblioteca import Biblioteca
from libro import Libro
from tkinter import Tk, Menu, Button, Frame

def mostrar_mensaje(accion):
    print(f"Realizando acción: {accion}")


def registrar_prestamo():
    ventana_registro_prestamo = tk.Toplevel()
    ventana_registro_prestamo.title("Registrar préstamo")
    ventana_registro_prestamo.geometry("400x250")

    # Estilo para la etiqueta del título
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("Titulo.TLabel", font=("Arial bold", 12))

    label_titulo = ttk.Label(ventana_registro_prestamo, text="Registrar préstamo", style="Titulo.TLabel")
    label_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Estilo para las etiquetas y la entrada
    estilo_widget = ttk.Style()
    estilo_widget.configure("Estilo.TLabel", padding=5)
    estilo_widget.configure("Estilo.TEntry", padding=(5, 5, 5, 5))

    label_numero_socio = ttk.Label(ventana_registro_prestamo, text="Número de Socio:", style="Estilo.TLabel")
    label_numero_socio.grid(column=0, row=2)

    entry_numero_socio = ttk.Entry(ventana_registro_prestamo, style="Estilo.TEntry")
    entry_numero_socio.grid(column=1, row=2, sticky="ew")  

    label_titulo_libro = ttk.Label(ventana_registro_prestamo, text="Título del Libro:", style="Estilo.TLabel")
    label_titulo_libro.grid(column=0, row=3)

    entry_titulo_libro = ttk.Entry(ventana_registro_prestamo, style="Estilo.TEntry")
    entry_titulo_libro.grid(column=1, row=3, sticky="ew")

    label_dias = ttk.Label(ventana_registro_prestamo, text="Días para devolución:", style="Estilo.TLabel")
    label_dias.grid(column=0, row=3)

    entry_dias = ttk.Entry(ventana_registro_prestamo, style="Estilo.TEntry")
    entry_dias.grid(column=1, row=3, sticky="ew")

    # Configuración de la columna para expandirse
    ventana_registro_prestamo.columnconfigure(1, weight=1)

    # Estilo para el botón
    estilo_boton = ttk.Style()
    estilo_boton.configure("Estilo.TButton", padding=(10, 5, 10, 5), font=('Arial', 10, 'bold'))

    boton_registrar = ttk.Button(ventana_registro_prestamo, text="Registrar", command=lambda: btn_registrar_prestamo(entry_numero_socio, entry_titulo_libro, entry_dias), style="Estilo.TButton")
    boton_registrar.grid(column=0, row=4, columnspan=2, pady=10)

    ventana_registro_prestamo.mainloop()

def btn_registrar_prestamo(entry_numero_socio: Entry, entry_titulo_libro: Entry, entry_dias: Entry):
    numero_socio = entry_numero_socio.get()
    titulo_libro = entry_titulo_libro.get()
    dias_devolucion = entry_dias.get()

    biblioteca: Biblioteca = Biblioteca()
    biblioteca.registrarPrestamo(diasDevolucion=dias_devolucion, )

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


def registrar_libro():
    ventana_registro_libro = tk.Toplevel()
    ventana_registro_libro.title("Registrar libro")
    ventana_registro_libro.geometry("400x250")

    # Estilo para la etiqueta del título
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("Titulo.TLabel", font=("Arial bold", 12))

    label_titulo = ttk.Label(ventana_registro_libro, text="Registrar libro", style="Titulo.TLabel")
    label_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Estilo para las etiquetas y la entrada
    estilo_widget = ttk.Style()
    estilo_widget.configure("Estilo.TLabel", padding=5)
    estilo_widget.configure("Estilo.TEntry", padding=(5, 5, 5, 5))

    label_nombre = ttk.Label(ventana_registro_libro, text="Nombre:", style="Estilo.TLabel")
    label_nombre.grid(column=0, row=2)

    entry_nombre = ttk.Entry(ventana_registro_libro, style="Estilo.TEntry")
    entry_nombre.grid(column=1, row=2, sticky="ew")  

    label_precio_reposicion = ttk.Label(ventana_registro_libro, text="Precio de Reposición:", style="Estilo.TLabel")
    label_precio_reposicion.grid(column=0, row=3)

    entry_precio_reposicion = ttk.Entry(ventana_registro_libro, style="Estilo.TEntry")
    entry_precio_reposicion.grid(column=1, row=3, sticky="ew")

    # Configuración de la columna para expandirse
    ventana_registro_libro.columnconfigure(1, weight=1)

    # Estilo para el botón
    estilo_boton = ttk.Style()
    estilo_boton.configure("Estilo.TButton", padding=(10, 5, 10, 5), font=('Arial', 10, 'bold'))

    boton_registrar = ttk.Button(ventana_registro_libro, text="Registrar", command=lambda: btn_registrar_libro(entry_nombre, entry_precio_reposicion), style="Estilo.TButton")
    boton_registrar.grid(column=0, row=4, columnspan=2, pady=10)

    ventana_registro_libro.mainloop()

def btn_registrar_libro(entry_nombre: Entry, entry_precio_reposicion: Entry):
    nombre = entry_nombre.get()
    precio_reposicion = entry_precio_reposicion.get()

    try:
        precio_reposicion = float(precio_reposicion)
    except ValueError:
        # Manejar el caso en el que la entrada no sea un número válido
        messagebox.showerror("Error", "Por favor, ingrese un precio de reposición válido.")
        return

    biblioteca: Biblioteca = Biblioteca()
    biblioteca.aggLibro(titulo=nombre, precioReposicion=precio_reposicion)
    

def eliminar_libro():
    ventana_eliminar_libro = tk.Toplevel()
    ventana_eliminar_libro.title("Eliminar libro")
    ventana_eliminar_libro.geometry("400x250")

    # Estilo para la etiqueta del título
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("Titulo.TLabel", font=("Arial bold", 12))

    label_titulo = ttk.Label(ventana_eliminar_libro, text="Eliminar libro", style="Titulo.TLabel")
    label_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Estilo para las etiquetas y la entrada
    estilo_widget = ttk.Style()
    estilo_widget.configure("Estilo.TLabel", padding=5)
    estilo_widget.configure("Estilo.TEntry", padding=(5, 5, 5, 5))

    label_codigo = ttk.Label(ventana_eliminar_libro, text="Código:", style="Estilo.TLabel")
    label_codigo.grid(column=0, row=2)

    entry_codigo = ttk.Entry(ventana_eliminar_libro, style="Estilo.TEntry")
    entry_codigo.grid(column=1, row=2, sticky="ew")  # 'ew' significa que se expandirá horizontalmente

    # Configuración de la columna para expandirse
    ventana_eliminar_libro.columnconfigure(1, weight=1)

    # Estilo para el botón
    estilo_boton = ttk.Style()
    estilo_boton.configure("Estilo.TButton", padding=(10, 5, 10, 5), font=('Arial', 10, 'bold'))

    boton_eliminar = ttk.Button(ventana_eliminar_libro, text="Eliminar", command=lambda: btn_eliminar_libro(entry_codigo), style="Estilo.TButton")
    boton_eliminar.grid(column=0, row=3, columnspan=2, pady=10)

    ventana_eliminar_libro.mainloop()

# Función que se ejecuta al hacer clic en el botón "Eliminar"
def btn_eliminar_libro(entry_codigo: Entry):
    codigo_libro = entry_codigo.get()
    biblioteca: Biblioteca = Biblioteca()
    biblioteca.eliminarLibro(codigo_libro)
    messagebox.showinfo("Exito", "Libro eliminado con éxito")

# Función para crear la interfaz
def inicio():
    ventana = Tk()
    ventana.title("Biblioteca UTN-FRC")
    ventana.geometry("800x500")
    ventana.configure(bg="lightblue")

    barra_menu = Menu(ventana)

    menu_socios = Menu(barra_menu)
    barra_menu.add_cascade(label="Administración de socios", menu=menu_socios)
    menu_libros = Menu(barra_menu)
    barra_menu.add_cascade(label="Administración de libros", menu=menu_libros)

    # Opciones del menú de socios
    menu_socios.add_command(label="Registrar socio", command=registrar_socio)
    menu_socios.add_command(label="Eliminar socio", command=eliminar_socio)
    menu_socios.add_command(label="Consultar socio", command=consultar_socio)

    # Opciones del menú de libros
    menu_libros.add_command(label="Registrar libro", command=registrar_libro)
    menu_libros.add_command(label="Eliminar libro", command=eliminar_libro)
    menu_libros.add_command(label="Consultar libro", command=lambda: mostrar_mensaje("Consultar libro"))
    # Opciones del menú de libros
    menu_prestamos_devolucion.add_command(label="Registrar prestamo de libro", command=registrar_libro)
    menu_prestamos_devolucion.add_command(label="Registrar devolución de libro", command=eliminar_libro)

    ventana.config(menu=barra_menu)

    # Crear dos marcos (frames) para organizar los botones
    frame_socios = Frame(ventana, bg="lightblue")  # Fondo de color lightblue
    frame_socios.pack(side="top", pady=50)

    frame_libros = Frame(ventana, bg="lightblue")  # Fondo de color lightgreen
    frame_libros.pack(side="top", pady=50)

    # Botones para administración de socios
    btn_admin_socios = Button(frame_socios, text="Administración de Socios", command=lambda: mostrar_botones_socios(frame_socios), bg="blue", fg="white", width=20)  # Fondo azul, texto blanco
    btn_admin_socios.pack(side="top", pady=10)

    # Botones para administración de libros
    btn_admin_libros = Button(frame_libros, text="Administración de Libros", command=lambda: mostrar_botones_libros(frame_libros), bg="green", fg="white", width=20)  # Fondo verde, texto blanco
    btn_admin_libros.pack(side="top", pady=10)

    ventana.mainloop()

# Función para mostrar botones específicos para administración de socios
def mostrar_botones_socios(frame):
    # Limpiar el frame antes de mostrar nuevos botones
    for widget in frame.winfo_children():
        widget.destroy()

    btn_registrar_socio = Button(frame, text="Registrar socio", command=registrar_socio, bg="lightblue", fg="black", width=20)  # Fondo lightblue, texto negro
    btn_registrar_socio.pack(side="top", pady=5)

    btn_eliminar_socio = Button(frame, text="Eliminar socio", command=eliminar_socio, bg="lightblue", fg="black", width=20)  # Fondo lightblue, texto negro
    btn_eliminar_socio.pack(side="top", pady=5)

    btn_consultar_socio = Button(frame, text="Consultar socio", command=consultar_socio, bg="lightblue", fg="black", width=20)  # Fondo lightblue, texto negro
    btn_consultar_socio.pack(side="top", pady=5)

# Función para mostrar botones específicos para administración de libros
def mostrar_botones_libros(frame):
    # Limpiar el frame antes de mostrar nuevos botones
    for widget in frame.winfo_children():
        widget.destroy()

    btn_registrar_libro = Button(frame, text="Registrar libro", command=registrar_libro, bg="lightgreen", fg="black", width=20)  # Fondo lightgreen, texto negro
    btn_registrar_libro.pack(side="top", pady=5)

    btn_eliminar_libro = Button(frame, text="Eliminar libro", command=eliminar_libro, bg="lightgreen", fg="black", width=20)  # Fondo lightgreen, texto negro
    btn_eliminar_libro.pack(side="top", pady=5)

    btn_consultar_libro = Button(frame, text="Consultar libro", bg="lightgreen", fg="black", width=20)  # Fondo lightgreen, texto negro
    btn_consultar_libro.pack(side="top", pady=5)

# Llamada a la función de inicio
inicio()