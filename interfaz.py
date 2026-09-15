"""
En este modulo se encuentra la implementacion de la interfaz grafica hehca con tkinter
se creo un menu interactivo con las funciones basicas para el usuario, para gestionar 
y ver la funcionalidd del sistema para utilizar de manera sencilla el gestor de 
persistencia de datos.

"""


import tkinter as tk
from tkinter import Menu, messagebox, filedialog, colorchooser

class VentanaConfiguracion(tk.Toplevel):
    """
    Ventana secundaria dedicada exclusivamente a la modificación de los ajustes de usuario.
    Objetivo: Permitir al usuario editar propiedades visuales y personales, disparando
    el almacenamiento persistente mediante el gestor de archivos.
    """
    
    def __init__(self, master, gestor_persistencia, callback_actualizar):
        """
        Inicializa la ventana de configuración y carga los datos actuales.
        Objetivo: Vincular la interfaz con los datos persistentes almacenados.
        """
        super().__init__(master)
        self.gestor = gestor_persistencia
        self.callback_actualizar = callback_actualizar
        
        self.title("Configuración de Usuario (Settings)")
        self.geometry("450x500")
        self.resizable(False, False)
        
        # Cargar los datos actuales desde el gestor de persistencia.
        self.datos_actuales = self.gestor.cargar_configuracion()
        
        self._crear_widgets()
        
    def _crear_widgets(self):
        """
        Crea y posiciona los elementos visuales de los ajustes (campos, etiquetas y botones).
        Objetivo: Proveer controles intuitivos para cada una de las opciones requeridas.
        """
        # Contenedor principal con margen interno.
        padding_frame = tk.Frame(self, padx=20, pady=20)
        padding_frame.pack(fill=tk.BOTH, expand=True)

        # 1. Nombre de usuario
        tk.Label(padding_frame, text="Nombre de usuario:", anchor="w").pack(fill=tk.X, pady=(0, 2))
        self.entry_usuario = tk.Entry(padding_frame)
        self.entry_usuario.pack(fill=tk.X, pady=(0, 10))
        self.entry_usuario.insert(0, self.datos_actuales.get("nombre_usuario", ""))

        # 2. Tema de interfaz (Claro / Oscuro)
        tk.Label(padding_frame, text="Tema de interfaz:", anchor="w").pack(fill=tk.X, pady=(0, 2))
        self.var_tema = tk.StringVar(value=self.datos_actuales.get("tema_interfaz", "claro"))
        frame_tema = tk.Frame(padding_frame)
        frame_tema.pack(fill=tk.X, pady=(0, 10))
        tk.Radiobutton(frame_tema, text="Claro", variable=self.var_tema, value="claro").pack(side=tk.LEFT, padx=(0, 15))
        tk.Radiobutton(frame_tema, text="Oscuro", variable=self.var_tema, value="oscuro").pack(side=tk.LEFT)
        
        
        # 3. Idioma
        tk.Label(padding_frame, text="Idioma:", anchor="w").pack(fill=tk.X, pady=(0, 2))
        self.var_idioma = tk.StringVar(value=self.datos_actuales.get("idioma", "es-ES"))
        self.combo_idioma = tk.Entry(padding_frame) # Simplificado para entrada de texto o selección
        self.combo_idioma.pack(fill=tk.X, pady=(0, 10))
        self.combo_idioma.insert(0, self.datos_actuales.get("idioma", "es-ES"))
        
        
        # 4. Tamaño de fuente (Número entero)
        tk.Label(padding_frame, text="Tamaño de fuente (entero):", anchor="w").pack(fill=tk.X, pady=(0, 2))
        self.spin_fuente = tk.Spinbox(padding_frame, from_=8, to=32)
        self.spin_fuente.pack(fill=tk.X, pady=(0, 10))
        self.spin_fuente.delete(0, tk.END)
        self.spin_fuente.insert(0, str(self.datos_actuales.get("tamanio_fuente", 12)))
        
        
        # 5. Colores (Barra de menú y Letra) mediante selectores nativos de la librería gráfica
        frame_colores = tk.Frame(padding_frame)
        frame_colores.pack(fill=tk.X, pady=(0, 10))
        
        self.color_menu_val = self.datos_actuales.get("color_barra_menu", "#f0f0f0")
        self.btn_color_menu = tk.Button(frame_colores, text="Color Barra Menú", bg=self.color_menu_val, command=self._seleccionar_color_menu)
        self.btn_color_menu.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        self.color_letra_val = self.datos_actuales.get("color_letra", "#000000")
        self.btn_color_letra = tk.Button(frame_colores, text="Color de Letra", bg=self.color_letra_val, fg="white" if self.color_letra_val=="#000000" else "black", command=self._seleccionar_color_letra)
        self.btn_color_letra.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))
        
        
        # 6. Foto de perfil (Seleccionada desde el sistema de archivos)
        tk.Label(padding_frame, text="Foto de perfil:", anchor="w").pack(fill=tk.X, pady=(0, 2))
        frame_foto = tk.Frame(padding_frame)
        frame_foto.pack(fill=tk.X, pady=(0, 15))
        
        self.lbl_ruta_foto = tk.Label(frame_foto, text=self.datos_actuales.get("foto_perfil", "Ninguna seleccionada"), fg="gray", anchor="w")
        self.lbl_ruta_foto.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        btn_examinar = tk.Button(frame_foto, text="Examinar...", command=self._seleccionar_foto)
        btn_examinar.pack(side=tk.RIGHT)

        # Botón para guardar cambios
        btn_guardar = tk.Button(padding_frame, text="Guardar Configuración", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self._guardar_cambios)
        btn_guardar.pack(fill=tk.X, pady=(10, 0))
        
        
        
    def _seleccionar_color_menu(self):
        """
        Abre el selector nativo de colores para la barra de menú.
        Objetivo: Facilitar la elección visual del color y actualizar la vista previa del botón.
        """
        color = colorchooser.askcolor(title="Seleccionar color de la barra de menú", initialcolor=self.color_menu_val)
        if color[1]:
            self.color_menu_val = color[1]
            self.btn_color_menu.config(bg=self.color_menu_val)
            
            
    def _seleccionar_color_letra(self):
        """
        Abre el selector nativo de colores para el texto.
        Objetivo: Permitir personalizar el color tipográfico de la interfaz.
        """
        color = colorchooser.askcolor(title="Seleccionar color de letra", initialcolor=self.color_letra_val)
        if color[1]:
            self.color_letra_val = color[1]
            self.btn_color_letra.config(bg=self.color_letra_val)
            
    def _seleccionar_foto(self):
        """
        Abre el explorador de archivos nativo del sistema para elegir una imagen de perfil.
        Objetivo: Obtener la ruta absoluta o relativa del archivo de imagen seleccionado.
        """
        ruta = filedialog.askopenfilename(
            title="Seleccionar foto de perfil",
            filetypes=[("Archivos de Imagen", "*.png *.jpg *.jpeg *.bmp"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            self.lbl_ruta_foto.config(text=ruta, fg="black")
            
            
    def _guardar_cambios(self):
        """
        Recopila los datos de los campos de la interfaz y solicita su almacenamiento seguro.
        Objetivo: Validar los tipos de datos (como el tamaño de fuente entero) y disparar el guardado.
        """
        try:
            tamanio = int(self.spin_fuente.get())
        except ValueError:
            messagebox.showerror("Error de Validación", "El tamaño de fuente debe ser un número entero válido.")
            return

        # Construir el diccionario con los nuevos valores, asegurando soporte para tildes y eñes (UTF-8).
        nuevos_datos = {
            "nombre_usuario": self.entry_usuario.get(),
            "tema_interfaz": self.var_tema.get(),
            "idioma": self.combo_idioma.get(),
            "tamanio_fuente": tamanio,
            "color_barra_menu": self.color_menu_val,
            "color_letra": self.color_letra_val,
            "foto_perfil": self.lbl_ruta_foto.cget("text") if self.lbl_ruta_foto.cget("text") != "Ninguna seleccionada" else ""
        }

        # Invocar al gestor de persistencia para realizar la escritura segura y atómica.
        exito = self.gestor.guardar_configuracion(nuevos_datos)
        
        if exito:
            messagebox.showinfo("Éxito", "Configuración guardada correctamente de forma segura.")
            self.callback_actualizar(nuevos_datos)
            self.destroy()
        else:
            messagebox.showerror("Error de Guardado", "No se pudo guardar la configuración debido a un problema de permisos o de disco.")
            
    
