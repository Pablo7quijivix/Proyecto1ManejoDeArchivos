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
