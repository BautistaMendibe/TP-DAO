import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from socio import Socio
from biblioteca import Biblioteca
from libro import Libro
from tkinter import Tk, Menu, Button, Frame


def validar_nombre(nombre):
    # Verificar si el nombre no está vacío
    if not nombre:
        messagebox.showerror("Error", "Por favor, ingrese un nombre.")
        return False

    # Verificar si el nombre contiene solo letras (no es un valor numérico)
    if not nombre.isalpha():
        messagebox.showerror("Error", "El nombre no puede contener números ni caracteres especiales.")
        return False

    return True

def validar_numero_socio(numero_socio):
    # Verificar si el número de socio no está vacío
    if not numero_socio:
        messagebox.showerror("Error", "Por favor, ingrese un número de socio.")
        return False

    # Verificar si el número de socio contiene solo dígitos
    if not numero_socio.isdigit():
        messagebox.showerror("Error", "El número de socio debe ser un valor numérico.")
        return False

    return True


def mostrar_mensaje(accion):
    print(f"Realizando acción: {accion}")

def cargar_imagen(ruta):
    imagen = PhotoImage(file=ruta)
    return imagen

def registrar_prestamo():
    ventana_registro_prestamo = tk.Toplevel()
    ventana_registro_prestamo.title("Registrar préstamo")
    ventana_registro_prestamo.geometry("400x250")
    ventana_registro_prestamo.grab_set()  # Hace que la ventana principal sea no interactiva

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
    label_numero_socio.grid(column=0, row=1)

    entry_numero_socio = ttk.Entry(ventana_registro_prestamo, style="Estilo.TEntry")
    entry_numero_socio.grid(column=1, row=1, sticky="ew")

    label_titulo_libro = ttk.Label(ventana_registro_prestamo, text="Título del Libro:", style="Estilo.TLabel")
    label_titulo_libro.grid(column=0, row=2)

    entry_titulo_libro = ttk.Entry(ventana_registro_prestamo, style="Estilo.TEntry")
    entry_titulo_libro.grid(column=1, row=2, sticky="ew")

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
    biblioteca.registrarPrestamo(diasDevolucion=dias_devolucion, numSocio=numero_socio, libro=titulo_libro)

def registrar_socio():
    ventana_registro_socio = tk.Toplevel()
    ventana_registro_socio.title("Registrar socio")
    ventana_registro_socio.geometry("400x250")
    ventana_registro_socio.grab_set()  # Hace que la ventana principal sea no interactiva

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

    boton_registrar = ttk.Button(ventana_registro_socio, text="Registrar", command=lambda: btn_registrar_socio(ventana_registro_socio, entry_nombre), style="Estilo.TButton")
    boton_registrar.grid(column=0, row=3, columnspan=2, pady=10)

    ventana_registro_socio.mainloop()

def btn_registrar_socio(ventana_registro_socio, entry_nombre: Entry):
    nombre = entry_nombre.get()
    biblioteca: Biblioteca = Biblioteca()
    biblioteca.aggSocio(nombre)
    
    # Validar el nombre antes de registrar al socio
    if validar_nombre(nombre):
        biblioteca: Biblioteca = Biblioteca()
        biblioteca.aggSocio(nombre)
        # Mostrar pop-up de éxito
        messagebox.showinfo("Registrar socio", "El socio se ha registrado con éxito.")
        
        ventana_registro_socio.destroy()


    
def eliminar_socio():
    ventana_eliminar_socio = tk.Toplevel()
    ventana_eliminar_socio.title("Eliminar socio")
    ventana_eliminar_socio.geometry("400x250")
    ventana_eliminar_socio.grab_set()  # Hace que la ventana principal sea no interactiva

    # Estilo para la etiqueta del título
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("Titulo.TLabel", font=("Arial bold", 12))

    label_titulo = ttk.Label(ventana_eliminar_socio, text="Eliminar socio", style="Titulo.TLabel")
    label_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Estilo para las etiquetas y la entrada
    estilo_widget = ttk.Style()
    estilo_widget.configure("Estilo.TLabel", padding=5)
    estilo_widget.configure("Estilo.TEntry", padding=(5, 5, 5, 5))

    label_numeroSocio = ttk.Label(ventana_eliminar_socio, text="Número de Socio:", style="Estilo.TLabel")
    label_numeroSocio.grid(column=0, row=2)

    entry_numeroSocio = ttk.Entry(ventana_eliminar_socio, style="Estilo.TEntry")
    entry_numeroSocio.grid(column=1, row=2, sticky="ew")  # 'ew' significa que se expandirá horizontalmente

    # Configuración de la columna para expandirse
    ventana_eliminar_socio.columnconfigure(1, weight=1)

    # Estilo para el botón
    estilo_boton = ttk.Style()
    estilo_boton.configure("Estilo.TButton", padding=(10, 5, 10, 5), font=('Arial', 10, 'bold'))

    boton_registrar = ttk.Button(ventana_eliminar_socio, text="Eliminar", command=lambda: btn_eliminar_socio(ventana_eliminar_socio, entry_numeroSocio), style="Estilo.TButton")
    boton_registrar.grid(column=0, row=3, columnspan=2, pady=10)

    ventana_eliminar_socio.mainloop()

def btn_eliminar_socio(ventana_eliminar_socio, entry_numeroSocio: Entry):
    numeroSocio = entry_numeroSocio.get()
    # Validar el número de socio antes de eliminar al socio
    if validar_numero_socio(numeroSocio):
        biblioteca: Biblioteca = Biblioteca()
        biblioteca.eliminarSocio(numeroSocio)
        messagebox.showinfo("Eliminar Socio", "El socio se ha eliminado con éxito.")
        
        ventana_eliminar_socio.destroy()


def consultar_socio():
    ventana_consultar_socio = tk.Toplevel()
    ventana_consultar_socio.title("Consultar socio")
    ventana_consultar_socio.geometry("400x250")
    ventana_consultar_socio.grab_set()  # Hace que la ventana principal sea no interactiva

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
    # Validar el número de socio antes de consultar al socio
    if validar_numero_socio(numeroSocio):
        biblioteca: Biblioteca = Biblioteca()
        socio = biblioteca.consultarSocio(numeroSocio)

        # Verificar si el socio existe antes de mostrar la información
        if socio:
            # Crear etiquetas para mostrar la información del socio
            label_info_nombre = ttk.Label(ventana_consultar_socio, text=f"Nombre: " + socio.nombre, style="Estilo.TLabel")
            label_info_nombre.grid(column=0, row=4, columnspan=2, pady=5)
        else:
            messagebox.showinfo("Consultar socio", "El socio no existe.")
            
    ventana_consultar_socio.mainloop()


def registrar_libro():
    ventana_registro_libro = tk.Toplevel()
    ventana_registro_libro.title("Registrar libro")
    ventana_registro_libro.geometry("400x250")
    ventana_registro_libro.grab_set()  # Hace que la ventana principal sea no interactiva


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
    ventana_eliminar_libro.grab_set()  # Hace que la ventana principal sea no interactiva

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
    
    # Cargar la imagen usando la ruta relativa
    imagen_logo_utn = cargar_imagen("Imagenes/logoutn.png")
    
    # Crear un widget Label para mostrar la imagen
    label_imagen = Label(ventana, image=imagen_logo_utn, bg="lightblue")
    # Posicionar en la esquina superior derecha
    label_imagen.pack(pady=10)

    barra_menu = Menu(ventana)

    menu_socios = Menu(barra_menu)
    barra_menu.add_cascade(label="Administración de socios", menu=menu_socios)
    menu_libros = Menu(barra_menu)
    barra_menu.add_cascade(label="Administración de libros", menu=menu_libros)
    menu_prestamos_devolucion = Menu(barra_menu)
    barra_menu.add_cascade(label="Registro de préstamos y devoluciones", menu=menu_prestamos_devolucion)

    # Opciones del menú de socios
    menu_socios.add_command(label="Registrar socio", command=registrar_socio)
    menu_socios.add_command(label="Eliminar socio", command=eliminar_socio)
    menu_socios.add_command(label="Consultar socio", command=consultar_socio)

    # Opciones del menú de libros
    menu_libros.add_command(label="Registrar libro", command=registrar_libro)
    menu_libros.add_command(label="Eliminar libro", command=eliminar_libro)
    menu_libros.add_command(label="Consultar libro", command=lambda: mostrar_mensaje("Consultar libro"))


    # Opciones del menú de libros
    menu_prestamos_devolucion.add_command(label="Registrar prestamo de libro", command=registrar_prestamo)
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

# Función para crear la interfaz
def inicio():
    ventana = Tk()
    ventana.title("Biblioteca UTN-FRC")
    ventana.geometry("800x500")
    ventana.configure(bg="lightblue")

    # Crear el menú horizontal en la parte izquierda
    menu_frame = Frame(ventana, bg="#1f3a6e", width=int(ventana.winfo_screenwidth() * 0.3), height=ventana.winfo_screenheight())
    menu_frame.pack(side="left", fill="y")

    # Cargar las imágenes de los íconos
    icono_socios = cargar_imagen("Imagenes/icono_socios.png")
    icono_libros = cargar_imagen("Imagenes/icono_libros.png")
    icono_prestamos = cargar_imagen("Imagenes/icono_prestamos.png")

    # Crear el encabezado con una imagen
    imagen_encabezado = cargar_imagen("Imagenes/logoutn4.png")
    label_encabezado = Label(menu_frame, image=imagen_encabezado, bg="#1f3a6e")
    label_encabezado.pack(pady=10)

    # Crear etiquetas con íconos en el menú
    label_socios = Label(menu_frame, image=icono_socios, text="Administración de socios", compound="left", bg="#1f3a6e", fg="white", padx=10)
    label_socios.pack(pady=10)

    label_libros = Label(menu_frame, image=icono_libros, text="Administración de libros", compound="left", bg="#1f3a6e", fg="white", padx=10)
    label_libros.pack(pady=10)

    label_prestamos = Label(menu_frame, image=icono_prestamos, text="Registro de préstamos \ny devoluciones", compound="left", bg="#1f3a6e", fg="white", padx=10)
    label_prestamos.pack(pady=10)

    # Configurar eventos al pasar el cursor sobre las etiquetas
    label_socios.bind("<Enter>", lambda event: label_socios.config(bg="#003366"))
    label_socios.bind("<Leave>", lambda event: label_socios.config(bg="#1f3a6e"))

    label_libros.bind("<Enter>", lambda event: label_libros.config(bg="#003366"))
    label_libros.bind("<Leave>", lambda event: label_libros.config(bg="#1f3a6e"))

    label_prestamos.bind("<Enter>", lambda event: label_prestamos.config(bg="#003366"))
    label_prestamos.bind("<Leave>", lambda event: label_prestamos.config(bg="#1f3a6e"))

    # Texto con información del grupo debajo de las opciones del menú
    info_grupo = """
    Grupo 15 - DAO:
    Bautista Mendibe - 89249
    Débora Sandobal - 85543
    Ramiro Hosman - 87013
    Valentino Di Fulvio - 87424
    DAO - Desarrollo de Aplicaciones con Objetos"""

    label_info_grupo = Label(menu_frame, text=info_grupo, bg="#1f3a6e", fg="white", justify="left")
    label_info_grupo.pack(pady=10)

    ventana.mainloop()

# Función para cargar imágenes
def cargar_imagen(ruta):
    return PhotoImage(file=ruta)

# Llamada a la función de inicio
inicio()