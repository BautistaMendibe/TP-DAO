import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from socio import Socio
from biblioteca import Biblioteca
<<<<<<< Updated upstream
=======
from libro import Libro
from tkinter import Tk, Menu, Button, Frame
from tkcalendar import DateEntry

#Variables globales
labels_socio = []
labels_libro = []


# Función para limpiar las etiquetas
def limpiar_etiquetas(lista_etiquetas):
    for etiqueta in lista_etiquetas:
        etiqueta.destroy()
        

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

def validar_codigo_libro(codigo_libro):
    # Verificar si el número de socio no está vacío
    if not codigo_libro:
        messagebox.showerror("Error", "Por favor, ingrese un código de libro.")
        return False

    # Verificar si el número de socio contiene solo dígitos
    if not codigo_libro.isdigit():
        messagebox.showerror("Error", "El código de libro debe ser un valor numérico.")
        return False

    return True

def validar_precio_libro(precio_libro):
    # Verificar si el número de socio no está vacío
    if not precio_libro:
        messagebox.showerror("Error", "Por favor, ingrese un precio de reposición para el libro")
        return False

    # Verificar si el número de socio contiene solo dígitos
    if not precio_libro.isdigit():
        messagebox.showerror("Error", "El precio de reposición del libro debe ser un valor numérico.")
        return False

    return True

>>>>>>> Stashed changes

def mostrar_mensaje(accion):
    print(f"Realizando acción: {accion}")

<<<<<<< Updated upstream
def registrar_socio():
    ventana_registro_socio = tk.Toplevel()
    ventana_registro_socio.title("Registrar socio")
    ventana_registro_socio.geometry("400x250")
=======
def cargar_imagen(ruta):
    imagen = PhotoImage(file=ruta)
    return imagen

# Función que se ejecuta al hacer clic en el botón "Registrar"
def btn_registrar_socio(entry_nombre: Entry):
    nombre = entry_nombre.get()
    # Validar el nombre antes de registrar al socio
    if validar_nombre(nombre):
        biblioteca: Biblioteca = Biblioteca()
        biblioteca.aggSocio(nombre)
        # Mostrar pop-up de éxito
        messagebox.showinfo("Registrar socio", "El socio se ha registrado con éxito.")
        entry_nombre.delete(0, END)
        
# Función que se ejecuta al hacer clic en el botón "Consultar"
def btn_consultar_socio(entry_numeroSocio: Entry, frame):
    # Limpiar las etiquetas existentes antes de mostrar nueva información
    limpiar_etiquetas(labels_socio)
    numeroSocio = entry_numeroSocio.get()
    # Validar el número de socio antes de consultar al socio
    if validar_numero_socio(numeroSocio):
        biblioteca: Biblioteca = Biblioteca()
        socio = biblioteca.consultarSocio(numeroSocio)

        # Verificar si el socio existe antes de mostrar la información
        if socio:
            # Crear etiquetas para mostrar la información del socio
            label_info_nombre = ttk.Label(frame, text=f"Nombre: " + socio.nombre, style="Estilo.TLabel")
            label_info_nombre.pack(pady=5)
            label_info_nombre.configure(font=("Helvetica", 14, "bold"), background="white")
            
             # Almacenar las etiquetas en la lista global
            labels_socio.extend([label_info_nombre])

        else:
            messagebox.showinfo("Consultar socio", "El socio no existe.")

# Función que se ejecuta al hacer clic en el botón "Eliminar"
def btn_eliminar_socio(entry_numeroSocio: Entry):
    numeroSocio = entry_numeroSocio.get()
    # Validar el número de socio antes de eliminar al socio
    if validar_numero_socio(numeroSocio):
        biblioteca: Biblioteca = Biblioteca()
        socio = biblioteca.eliminarSocio(numeroSocio)
        # Verificar si el socio existe antes de mostrar la información
        if socio:
            messagebox.showinfo("Eliminar Socio",  f"El socio {socio.nombre} se ha eliminado con éxito.")
            entry_numeroSocio.delete(0, END)
        else:
            messagebox.showinfo("Eliminar socio", "El socio no existe.")


def btn_registrar_libro(entry_nombre: Entry, entry_precio_reposicion: Entry):
    nombre = entry_nombre.get()
    precio_reposicion = entry_precio_reposicion.get()
    
    if nombre:
        if validar_precio_libro(precio_reposicion):
            biblioteca: Biblioteca = Biblioteca()
            biblioteca.aggLibro(nombre, precio_reposicion)
            
            # Mostrar pop-up de éxito
            messagebox.showinfo("Registrar libro", "El libro se ha registrado con éxito")
            
            entry_nombre.delete(0, END)
            entry_precio_reposicion.delete(0, END)
    else:
        messagebox.showerror("Error", "Por favor, ingrese un nombre.")
        
def btn_consultar_libro(entry_codigo_libro: Entry, frame):
    # Limpiar las etiquetas existentes antes de mostrar nueva información
    limpiar_etiquetas(labels_libro)
    codigoLibro = entry_codigo_libro.get()
    # Validar el código del libro antes de consultar al libro
    if validar_codigo_libro(codigoLibro):
        biblioteca: Biblioteca = Biblioteca()
        libro = biblioteca.consultarLibro(codigoLibro)

        # Verificar si el libro existe antes de mostrar la información
        if libro:
            # Crear etiquetas para mostrar la información del libro
            label_info_nombre = ttk.Label(frame, text=f"Nombre: " + libro.titulo, style="Estilo.TLabel")
            label_info_nombre.pack(pady=5)
            label_info_nombre.configure(font=("Helvetica", 14, "bold"), background="white")
            
            label_info_precio = ttk.Label(frame, text=f"Precio de Reposición: $" + str(libro.precioReposicion), style="Estilo.TLabel")
            label_info_precio.pack(pady=5)
            label_info_precio.configure(font=("Helvetica", 14, "bold"), background="white")
            
            label_info_estado = ttk.Label(frame, text=f"Estado: " + libro.estado, style="Estilo.TLabel")
            label_info_estado.pack(pady=5)
            label_info_estado.configure(font=("Helvetica", 14, "bold"), background="white")
            
            # Almacenar las etiquetas en la lista global
            labels_libro.extend([label_info_nombre, label_info_precio, label_info_estado])
        else:
            messagebox.showinfo("Consultar libro", "El libro no existe.")

# Función que se ejecuta al hacer clic en el botón "Eliminar"
def btn_eliminar_libro(entry_codigo_libro: Entry):
    codigo_libro = entry_codigo_libro.get()
    if validar_codigo_libro(codigo_libro):
        biblioteca: Biblioteca = Biblioteca()
        libro = biblioteca.eliminarLibro(codigo_libro)
        # Verificar si el socio existe antes de mostrar la información
        if libro:
            messagebox.showinfo("Eliminar Libro",  f"El libro {libro.titulo} se ha eliminado con éxito.")
            entry_codigo_libro.delete(0, END)
        else:
            messagebox.showinfo("Eliminar socio", "El libro no existe.")

def registrar_prestamo():
    ventana_registro_prestamo = tk.Toplevel()
    ventana_registro_prestamo.title("Registrar préstamo")
    ventana_registro_prestamo.geometry("400x250")
    ventana_registro_prestamo.grab_set()  # Hace que la ventana principal sea no interactiva
>>>>>>> Stashed changes

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
    socio = bibli oteca.consultarSocio(numeroSocio)
    
    # Crear etiquetas para mostrar la información del socio
    label_info_nombre = ttk.Label(ventana_consultar_socio, text=f"Nombre: {socio[1]}", style="Estilo.TLabel")
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
    
<<<<<<< Updated upstream
=======
    frame_submenu2 = tk.Frame(frame, background="lightblue")
    frame_submenu2.pack(pady=100)

    if opcion == "Administración de socios":
        # Estilo para los botones del submenú
        estilo_boton_submenu = ttk.Style()
        estilo_boton_submenu.configure("Estilo.TButton", background="lightblue", foreground="black", padding=(10, 5, 10, 5), font=('Helvetica', 10, 'bold'))

        # Botón Registrar Socio
        boton_registrar_socio = ttk.Button(frame_submenu, text="Registrar Socio", command=lambda: mostrar_contenido_pestana("Registrar Socio", frame_submenu2), style="Estilo.TButton")
        boton_registrar_socio.pack(fill="y", side="left", padx = 10)

        # Botón Modificar Socio (puedes añadir la funcionalidad correspondiente)
        boton_consultar_socio = ttk.Button(frame_submenu, text="Consultar Socio", command=lambda: mostrar_contenido_pestana("Consultar Socio", frame_submenu2), style="Estilo.TButton")
        boton_consultar_socio.pack(fill="y", side="left", padx = 10)

        # Botón Eliminar Socio (puedes añadir la funcionalidad correspondiente)
        boton_eliminar_socio = ttk.Button(frame_submenu, text="Eliminar Socio", command=lambda: mostrar_contenido_pestana("Eliminar Socio", frame_submenu2), style="Estilo.TButton")
        boton_eliminar_socio.pack(fill="y", side="left", padx = 10)

    elif opcion == "Administración de libros":
        # Estilo para los botones del submenú
        estilo_boton_submenu = ttk.Style()
        estilo_boton_submenu.configure("Estilo.TButton", background="lightblue", foreground="black", padding=(10, 5, 10, 5), font=('Helvetica', 10, 'bold'))

        # Botón Registrar Libro
        boton_registrar_libro = ttk.Button(frame_submenu, text="Registrar Libro", command=lambda: mostrar_contenido_pestana("Registrar Libro", frame_submenu2), style="Estilo.TButton")
        boton_registrar_libro.pack(fill="x", side="left", padx = 10)

        # Botón Modificar Libro (puedes añadir la funcionalidad correspondiente)
        boton_modificar_libro = ttk.Button(frame_submenu, text="Consultar Libro", command=lambda: mostrar_contenido_pestana("Consultar Libro", frame_submenu2), style="Estilo.TButton")
        boton_modificar_libro.pack(fill="x", side="left", padx = 10)

        # Botón Eliminar Libro (puedes añadir la funcionalidad correspondiente)
        boton_eliminar_libro = ttk.Button(frame_submenu, text="Eliminar Libro", command=lambda: mostrar_contenido_pestana("Eliminar Libro", frame_submenu2), style="Estilo.TButton")
        boton_eliminar_libro.pack(fill="x",side="left", padx=10)

    elif opcion == "Registro de préstamos y devoluciones":
        # Estilo para los botones del submenú
        estilo_boton_submenu = ttk.Style()
        estilo_boton_submenu.configure("Estilo.TButton", background="lightblue", foreground="black", padding=(10, 5, 10, 5), font=('Helvetica', 10, 'bold'))

        # Botón Registrar Prestamo
        boton_registrar_prestamo = ttk.Button(frame_submenu, text="Registrar Prestamo", command=lambda: mostrar_contenido_pestana("Registrar Prestamo", frame_submenu2), style="Estilo.TButton")
        boton_registrar_prestamo.pack(side="left", padx = 10)

        # Botón registrar Devolucion
        boton_registar_devolucion = ttk.Button(frame_submenu, text="Registrar Devolucion", command=lambda: mostrar_contenido_pestana("Registrar Devolucion", frame_submenu2), style="Estilo.TButton")
        boton_registar_devolucion.pack(fill="x", side="left", padx = 10)
    
    elif opcion == "Reportes":
        # Estilo para los botones del submenú
        estilo_boton_submenu = ttk.Style()
        estilo_boton_submenu.configure("Estilo.TButton", background="lightblue", foreground="black", padding=(10, 5, 10, 5), font=('Helvetica', 10, 'bold'))

        # Botón Registrar Prestamo
        boton_registrar_prestamo = ttk.Button(frame_submenu, text="Reportes", command=lambda: mostrar_contenido_pestana("REPORTES", frame_submenu2), style="Estilo.TButton")
        boton_registrar_prestamo.pack(side="left", padx = 10)

        # Botón registrar Devolucion
        boton_registar_devolucion = ttk.Button(frame_submenu, text="Reportes", command=lambda: mostrar_contenido_pestana("Registrar Devolucion", frame_submenu2), style="Estilo.TButton")
        boton_registar_devolucion.pack(fill="x", side="left", padx = 10)
        
def mostrar_contenido_pestana(opcion, frame):
    for widget in frame.winfo_children():
        widget.destroy()
        
    # Estilo para las etiquetas y la entrada
        estilo_widget = ttk.Style()
        estilo_widget.configure("Estilo.TLabel", padding=5)
        estilo_widget.configure("Estilo.TEntry", padding=(5, 5, 5, 5))
    
    # Estilo para el botón
        estilo_boton = ttk.Style()
        estilo_boton.configure("Estilo.TButton", padding=(10, 5, 10, 5), font=('Arial', 10, 'bold'))
        
    if opcion == "Registrar Socio":
        
        label_codigo_libro = ttk.Label(frame, text="Nombre:", style="Estilo.TLabel")
        label_codigo_libro.pack()

        entry_nombre = ttk.Entry(frame, style="Estilo.TEntry")
        entry_nombre.pack(fill="x", pady=5)

        boton_registrar = ttk.Button(frame, text="Registrar", command=lambda: btn_registrar_socio(entry_nombre), style="Estilo.TButton")
        boton_registrar.pack(fill="x", pady=10)
    
    elif opcion == "Consultar Socio":
        label_codigo_libro = ttk.Label(frame, text="Número de Socio:", style="Estilo.TLabel")
        label_codigo_libro.pack()

        entry_numeroSocio = ttk.Entry(frame, style="Estilo.TEntry")
        entry_numeroSocio.pack(fill="x", pady=5)

        boton_consultar = ttk.Button(frame, text="Consultar", command=lambda: btn_consultar_socio(entry_numeroSocio, frame), style="Estilo.TButton")
        boton_consultar.pack(fill="x", pady=10)
    
    elif opcion == "Eliminar Socio":

        label_codigo_libro = ttk.Label(frame, text="Número de Socio:", style="Estilo.TLabel")
        label_codigo_libro.pack()

        entry_nombre = ttk.Entry(frame, style="Estilo.TEntry")
        entry_nombre.pack(fill="x", pady=5)

        boton_eliminar = ttk.Button(frame, text="Eliminar", command=lambda: btn_eliminar_socio(entry_nombre), style="Estilo.TButton")
        boton_eliminar.pack(fill="x", pady=10)
    
    elif opcion == "Registrar Libro":

        label_codigo_libro = ttk.Label(frame, text="Nombre:", style="Estilo.TLabel")
        label_codigo_libro.pack()

        entry_nombre = ttk.Entry(frame, style="Estilo.TEntry")
        entry_nombre.pack(fill="x", pady=5)
        
        label_precio = ttk.Label(frame, text="Costo de Reposicion:", style="Estilo.TLabel")
        label_precio.pack()
        
        entry_precio_reposicion = ttk.Entry(frame, style="Estilo.TEntry")
        entry_precio_reposicion.pack(fill="x", pady=5)

        boton_registrar = ttk.Button(frame, text="Registrar", command=lambda: btn_registrar_libro(entry_nombre, entry_precio_reposicion), style="Estilo.TButton")
        boton_registrar.pack(fill="x", pady=10)
        
    elif opcion == "Consultar Libro":
        label_codigo_libro = ttk.Label(frame, text="Codigo de Libro:", style="Estilo.TLabel")
        label_codigo_libro.pack()

        entry_codigo_libro = ttk.Entry(frame, style="Estilo.TEntry")
        entry_codigo_libro.pack(fill="x", pady=5)

        boton_consultar = ttk.Button(frame, text="Consultar", command=lambda: btn_consultar_libro(entry_codigo_libro, frame), style="Estilo.TButton")
        boton_consultar.pack(fill="x", pady=10)
    
    elif opcion == "Eliminar Libro":
        label_codigo_libro = ttk.Label(frame, text="Codigo de Libro:", style="Estilo.TLabel")
        label_codigo_libro.pack()

        entry_nombre = ttk.Entry(frame, style="Estilo.TEntry")
        entry_nombre.pack(fill="x", pady=5)

        boton_eliminar = ttk.Button(frame, text="Eliminar", command=lambda: btn_eliminar_libro(entry_nombre), style="Estilo.TButton")
        boton_eliminar.pack(fill="x", pady=10)
    
    elif opcion == "Registrar Prestamo":
        
        label_fecha_prestamo = ttk.Label(frame, text="Fecha de Préstamo:", style="Estilo.TLabel")
        label_fecha_prestamo.pack(fill="x")

        # Usa el widget DateEntry para permitir al usuario seleccionar la fecha
        entry_fecha_prestamo = DateEntry(frame, style="Estilo.TEntry", date_pattern="dd/mm/yyyy")
        entry_fecha_prestamo.pack(fill="x")

        label_numero_socio = ttk.Label(frame, text="Número de Socio:", style="Estilo.TLabel")
        label_numero_socio.pack(fill="x")

        entry_numero_socio = ttk.Entry(frame, style="Estilo.TEntry")
        entry_numero_socio.pack(fill="x")

        label_titulo_libro = ttk.Label(frame, text="Título del Libro:", style="Estilo.TLabel")
        label_titulo_libro.pack(fill="x")

        entry_titulo_libro = ttk.Entry(frame, style="Estilo.TEntry")
        entry_titulo_libro.pack(fill="x")

        label_dias = ttk.Label(frame, text="Días para devolución:", style="Estilo.TLabel")
        label_dias.pack(fill="x")

        entry_dias = ttk.Entry(frame, style="Estilo.TEntry")
        entry_dias.pack(fill="x")

        boton_registrar = ttk.Button(frame, text="Registrar", command=lambda: btn_registrar_prestamo(entry_numero_socio, entry_titulo_libro, entry_dias), style="Estilo.TButton")
        boton_registrar.pack(fill="x")
    
    elif opcion == "Registrar Devolucion":
        pass
    

# Llamada a la función de inicio
>>>>>>> Stashed changes
inicio()