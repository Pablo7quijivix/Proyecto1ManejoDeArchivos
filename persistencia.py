'''
Modulo de persistenica de Datos
Drescripcion:Este modulo se encarga de la persistencia de datos de la configuracion 
del usuario almacenado en archivos JSON.

Objetivo de este modulo: Garantiza la escritura y lectura de manera segura, creando respaldos (.bak)
contiene escritura mediante archivos temporales (.temp), cuenta con manejo robusto de errores como 
(ausencia, corrupcion, permisos) y codificacion UTF-8
'''

import json
import os 
import shutil 


class GestorPersistencia: 
    '''
    Esta clase se encarga de administrar el ciclo de vida del archivo de configuracion,
    de esta manera estamos asegurando la integridad de los datos cuando se presenten 
    datos corruptos o posibles fallos de escritura.
    '''
    
    def __init__(self, ruta_archivo= "config.json"):
        """
        Inicializa el gestor de persistencia con la ruta del archivo de configuración.
        Objetivo: Definir las rutas base para el archivo principal, temporal y de respaldo.
        """
        self.ruta_archivo = ruta_archivo
        self.ruta_temporal = ruta_archivo + ".temp"
        self.ruta_respaldo = ruta_archivo + ".bak"
        
        #Definiendo la configuracion por defecto ante cualquier problama o archivo ausente.
        self.config_por_defecto = {
            "nombre_usuario": "Usuario",
            "tema_interfaz":"claro",
            "idioma":"es-Es",
            "tamanio_fuente":"12",
            "color_barra_menu":"#f0f0f0",
            "color_letra":"#000000",
            "foto_perfil":""
            
        }
        
        
        
        
    