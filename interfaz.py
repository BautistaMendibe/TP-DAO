import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from socio import Socio
from biblioteca import Biblioteca
from libro import Libro
from tkinter import Tk, Menu, Button, Frame

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


def mostrar_mensaje(accion):
    print(f"Realizando acción: {accion}")

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


def btn_registrar_prestamo(entry_numero_socio: Entry, entry_codigo_libro: Entry, entry_dias: Entry):
    numero_socio = entry_numero_socio.get()
    codigo_libro = entry_codigo_libro.get()
    dias_devolucion = entry_dias.get()

    biblioteca: Biblioteca = Biblioteca()
    biblioteca.registrarPrestamo(numero_socio, codigo_libro, dias_devolucion)

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
    icono_prestamos = cargar_imagen("Imagenes/pedir-prestamo.png")
    icono_reportes = cargar_imagen("Imagenes/reportes.png")


    # Crear el encabezado con una imagen
    imagen_encabezado = cargar_imagen("Imagenes/logoutn4.png")
    label_encabezado = Label(menu_frame, image=imagen_encabezado, bg="#1f3a6e")
    label_encabezado.pack(pady=10)

    # Crear etiquetas con íconos en el menú sin margen horizontal
    label_socios = Label(menu_frame, image=icono_socios, text="  Administración de socios", compound="left", bg="#1f3a6e", fg="white", padx=0, highlightthickness=0, bd=0)
    label_socios.pack(fill=X, expand=True, pady=10)
    label_socios.bind("<Button-1>", lambda event: mostrar_contenido("Administración de socios", contenido_frame))

    label_libros = Label(menu_frame, image=icono_libros, text="  Administración de libros", compound="left", bg="#1f3a6e", fg="white", padx=0, highlightthickness=0, bd=0)
    label_libros.pack(fill=X, expand=True, pady=10)
    label_libros.bind("<Button-1>", lambda event: mostrar_contenido("Administración de libros", contenido_frame))

    label_prestamos = Label(menu_frame, image=icono_prestamos, text="  Registro de préstamos \ny devoluciones", compound="left", bg="#1f3a6e", fg="white", padx=0, highlightthickness=0, bd=0)
    label_prestamos.pack(fill=X, expand=True, pady=10)
    label_prestamos.bind("<Button-1>", lambda event: mostrar_contenido("Registro de préstamos y devoluciones", contenido_frame))
    
    label_reportes = Label(menu_frame, image=icono_reportes, text="  Reportes                          ", compound="left", bg="#1f3a6e", fg="white", padx=0, highlightthickness=0, bd=0)
    label_reportes.pack(fill=X, expand=True, pady=10)
    label_reportes.bind("<Button-1>", lambda event: mostrar_contenido("Reportes", contenido_frame))

    # Configurar eventos al pasar el cursor sobre las etiquetas
    label_socios.bind("<Enter>", lambda event: label_socios.config(bg="#003366"))
    label_socios.bind("<Leave>", lambda event: label_socios.config(bg="#1f3a6e"))

    label_libros.bind("<Enter>", lambda event: label_libros.config(bg="#003366"))
    label_libros.bind("<Leave>", lambda event: label_libros.config(bg="#1f3a6e"))

    label_prestamos.bind("<Enter>", lambda event: label_prestamos.config(bg="#003366"))
    label_prestamos.bind("<Leave>", lambda event: label_prestamos.config(bg="#1f3a6e"))

    label_reportes.bind("<Enter>", lambda event: label_reportes.config(bg="#003366"))
    label_reportes.bind("<Leave>", lambda event: label_reportes.config(bg="#1f3a6e"))

    # Texto con información del grupo debajo de las opciones del menú
    info_grupo = """
    Grupo 15:
    Bautista Mendibe - 89249
    Débora Sandobal - 85543
    Ramiro Hosman - 87013
    Valentino Di Fulvio - 87424
    DAO - Desarrollo de Aplicaciones con Objetos"""

    label_info_grupo = Label(menu_frame, text=info_grupo, bg="#1f3a6e", fg="white", justify="left")
    label_info_grupo.pack(pady=10)

    # Título en la pantalla principal
    titulo_principal = Label(ventana, text="Sistema de gestión de Bibliotecas", bg="#1f3a6e", fg="white", font=("Helvetica", 16, "bold"))
    titulo_principal.pack(fill="x", pady=0)

    # Contenido debajo del título
    contenido_frame = Frame(ventana, bg="lightblue")
    contenido_frame.pack(fill="both", expand=True)

    # Mostrar por defecto el contenido de "Administración de socios"
    mostrar_contenido("Administración de socios", contenido_frame)

    ventana.mainloop()

def btn_libros_x_estado(frame):
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    biblioteca: Biblioteca = Biblioteca()
    resultados = biblioteca.librosCadEstado()
    
    # Crear un árbol para mostrar la tabla
    tree = ttk.Treeview(frame, columns=("Estado", "Cantidad"), show="headings")

    # Configurar las columnas
    tree.heading("Estado", text="Estado")
    tree.heading("Cantidad", text="Cantidad")

    # Insertar los datos en el árbol
    for resultado in resultados:
        tree.insert("", "end", values=resultado)

    # Estilo para la tabla
    style = ttk.Style()
    style.configure("Treeview", font=('Arial', 12), rowheight=25)

    # Configurar tamaño de la tabla
    tree.pack(expand=True, fill=tk.BOTH)

def btn_precio_libros_extr(frame):
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    biblioteca: Biblioteca = Biblioteca()
    resultados = biblioteca.precioLibrosExtraviados()
    
    columnas = ["Sumatoria Precio Reposición"]

   # Crear un árbol para mostrar la tabla
    tree = ttk.Treeview(frame, columns=columnas, show="headings")

    # Configurar las columnas
    for col in columnas:
        tree.heading(col, text=col)
    
    if resultados:
        # Insertar los datos en el árbol
        tree.insert("", "end", values=resultados)
    else:
        # Mostrar mensaje si no hay resultados
        tree.insert("", "end", values=["No hay libros extraviados"])

    # Estilo para la tabla
    style = ttk.Style()
    style.configure("Treeview", font=('Arial', 12), rowheight=25)

    # Configurar tamaño de la tabla
    tree.pack(expand=True, fill=tk.BOTH)

def btn_socios_piden_libro(entry, frame):
    titulo = entry.get()
    
    biblioteca: Biblioteca = Biblioteca()
    if biblioteca.consultarLibroxTitulo(titulo) != None:
        for widget in frame.winfo_children():
            widget.destroy()
        
        solicitantes = biblioteca.solicitantesDeLibro(titulo)
        
        # Crear un árbol para mostrar la tabla
        tree = ttk.Treeview(frame, columns=("Número de Socio", "Nombre"), show="headings")

        # Configurar las columnas
        tree.heading("Número de Socio", text="Número de Socio")
        tree.heading("Nombre", text="Nombre")
    
        if solicitantes:
            # Insertar los datos en el árbol
            for solicitante in solicitantes:
                tree.insert("", "end", values=(solicitante.numeroSocio, solicitante.nombre))
        else:
            # Mostrar mensaje si no hay solicitantes
            tree.insert("", "end", values=["No hay solicitantes para el libro"])

        # Estilo para la tabla
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', 12), rowheight=25)

        # Configurar tamaño de la tabla
        tree.pack(expand=True, fill=tk.BOTH)
    else:
        messagebox.showerror("Error", "Por favor, ingrese el titulo de un libro que este registrado")
    
# Función para mostrar el contenido en el frame
def mostrar_contenido(opcion, frame):
    # Limpiar el contenido actual
    for widget in frame.winfo_children():
        widget.destroy()

    # Crear el contenido para la opción seleccionada
    contenido_label = tk.Label(frame, text=f"{opcion}", bg="#1f3a6e", fg="white", font=("Helvetica", 12, "bold"))
    contenido_label.pack(fill="x", pady=0)

    # Crear un frame para el submenú
    frame_submenu = tk.Frame(frame, background="lightblue")
    frame_submenu.pack()
    
    frame_submenu2 = tk.Frame(frame, background="lightblue")
    frame_submenu2.pack(pady=100)

    if opcion == "Administración de socios":
        # Estilo para los botones del submenú
        estilo_boton_submenu = ttk.Style()
        estilo_boton_submenu.configure("Estilo.TButton", background="lightblue", foreground="#1f3a6e", padding=(10, 5, 10, 5), font=('Helvetica', 10, 'bold'))

        # Botón Registrar Socio
        boton_registrar_socio = ttk.Button(frame_submenu, text="Registrar Socio", command=lambda: mostrar_contenido_pestana("Registrar Socio", frame_submenu2), style="Estilo.TButton")
        boton_registrar_socio.pack(fill="y", side="left", padx = 10, pady=10)

        # Botón Modificar Socio (puedes añadir la funcionalidad correspondiente)
        boton_consultar_socio = ttk.Button(frame_submenu, text="Consultar Socio", command=lambda: mostrar_contenido_pestana("Consultar Socio", frame_submenu2), style="Estilo.TButton")
        boton_consultar_socio.pack(fill="y", side="left", padx = 10, pady=10)

        # Botón Eliminar Socio (puedes añadir la funcionalidad correspondiente)
        boton_eliminar_socio = ttk.Button(frame_submenu, text="Eliminar Socio", command=lambda: mostrar_contenido_pestana("Eliminar Socio", frame_submenu2), style="Estilo.TButton")
        boton_eliminar_socio.pack(fill="y", side="left", padx = 10, pady=10)

        # Mostrar por defecto el contenido de "Registrar socios"
        mostrar_contenido_pestana("Registrar Socio", frame_submenu2)

    elif opcion == "Administración de libros":
        # Estilo para los botones del submenú
        estilo_boton_submenu = ttk.Style()
        estilo_boton_submenu.configure("Estilo.TButton", background="lightblue", foreground="#1f3a6e", padding=(10, 5, 10, 5), font=('Helvetica', 10, 'bold'))

        # Botón Registrar Libro
        boton_registrar_libro = ttk.Button(frame_submenu, text="Registrar Libro", command=lambda: mostrar_contenido_pestana("Registrar Libro", frame_submenu2), style="Estilo.TButton")
        boton_registrar_libro.pack(fill="x", side="left", padx = 10, pady=10)

        # Botón Modificar Libro (puedes añadir la funcionalidad correspondiente)
        boton_modificar_libro = ttk.Button(frame_submenu, text="Consultar Libro", command=lambda: mostrar_contenido_pestana("Consultar Libro", frame_submenu2), style="Estilo.TButton")
        boton_modificar_libro.pack(fill="x", side="left", padx = 10)

        # Botón Eliminar Libro (puedes añadir la funcionalidad correspondiente)
        boton_eliminar_libro = ttk.Button(frame_submenu, text="Eliminar Libro", command=lambda: mostrar_contenido_pestana("Eliminar Libro", frame_submenu2), style="Estilo.TButton")
        boton_eliminar_libro.pack(fill="x",side="left", padx=10)

        mostrar_contenido_pestana("Registrar Libro", frame_submenu2)

    elif opcion == "Registro de préstamos y devoluciones":
        # Estilo para los botones del submenú
        estilo_boton_submenu = ttk.Style()
        estilo_boton_submenu.configure("Estilo.TButton", background="lightblue", foreground="#1f3a6e", padding=(10, 5, 10, 5), font=('Helvetica', 10, 'bold'))

        # Botón Registrar Prestamo
        boton_registrar_prestamo = ttk.Button(frame_submenu, text="Registrar Prestamo", command=lambda: mostrar_contenido_pestana("Registrar Prestamo", frame_submenu2), style="Estilo.TButton")
        boton_registrar_prestamo.pack(side="left", padx = 10, pady=10)

        # Botón registrar Devolucion
        boton_registar_devolucion = ttk.Button(frame_submenu, text="Registrar Devolucion", command=lambda: mostrar_contenido_pestana("Registrar Devolucion", frame_submenu2), style="Estilo.TButton")
        boton_registar_devolucion.pack(fill="x", side="left", padx = 10)
    
    elif opcion == "Reportes":
        # Estilo para los botones del submenú
        estilo_boton_submenu = ttk.Style()
        estilo_boton_submenu.configure("Estilo.TButton", background="lightblue", foreground="#1f3a6e", padding=(10, 5, 10, 5), font=('Helvetica', 10, 'bold'))

        # Botón mostrar libros por estado
        boton_libros_por_estado = ttk.Button(frame_submenu, text="Libros por Estado", command=lambda: btn_libros_x_estado(frame_submenu2), style="Estilo.TButton")
        boton_libros_por_estado.pack(side="left", padx = 10, pady=10)

        # Botón muestra sumatoria de costo de reposicion
        boton_libros_reposicion = ttk.Button(frame_submenu, text="Precios de Extraviados", command=lambda: btn_precio_libros_extr(frame_submenu2), style="Estilo.TButton")
        boton_libros_reposicion.pack(fill="x", side="bottom", padx = 10)
        
        # Boton muestra los nombres que solicictaron un libro
        boton_socio_libro = ttk.Button(frame_submenu, text="Socios que pidieron libro", command=lambda: mostrar_contenido_pestana("Socios que pidieron libro", frame_submenu2), style="Estilo.TButton")
        boton_socio_libro.pack(fill="x", side="bottom", padx = 10)
        
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

        label_numero_socio = ttk.Label(frame, text="Número de Socio:", style="Estilo.TLabel")
        label_numero_socio.pack()

        entry_numero_socio = ttk.Entry(frame, style="Estilo.TEntry")
        entry_numero_socio.pack()

        label_codigo_libro = ttk.Label(frame, text="Código del Libro:", style="Estilo.TLabel")
        label_codigo_libro.pack()

        entry_codigo_libro = ttk.Entry(frame, style="Estilo.TEntry")
        entry_codigo_libro.pack()

        label_dias = ttk.Label(frame, text="Días para devolución:", style="Estilo.TLabel")
        label_dias.pack()

        entry_dias = ttk.Entry(frame, style="Estilo.TEntry")
        entry_dias.pack()

        boton_registrar = ttk.Button(frame, text="Registrar", command=lambda: btn_registrar_prestamo(entry_numero_socio, entry_codigo_libro, entry_dias), style="Estilo.TButton")
        boton_registrar.pack()
        
    elif opcion == "Registrar Devolucion":
        pass
    
    elif opcion == "Socios que pidieron libro":
        label_nombre_libro = ttk.Label(frame, text="Titulo de Libro:", style="Estilo.TLabel")
        label_nombre_libro.pack()

        entry_nombre_libro = ttk.Entry(frame, style="Estilo.TEntry")
        entry_nombre_libro.pack(fill="x", pady=5)

        boton_consultar = ttk.Button(frame, text="Buscar", command=lambda: btn_socios_piden_libro(entry_nombre_libro, frame), style="Estilo.TButton")
        boton_consultar.pack(fill="x", pady=10)
    

# Llamada a la función de inicio
inicio()