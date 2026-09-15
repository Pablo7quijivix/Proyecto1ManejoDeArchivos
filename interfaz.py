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
