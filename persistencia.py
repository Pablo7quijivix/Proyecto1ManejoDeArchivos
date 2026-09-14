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
        
    def cargar_configuracion(self):
        """
        Lee la configuración desde el archivo JSON utilizando codificación UTF-8.
        Objetivo: Recuperar los ajustes previos del usuario de forma segura, manejando
        excepciones por archivo ausente, corrupción o problemas de permisos.
        """
        
        #verificacion si el archivo principal de configuracion
        #existe fisicamente en el disco
        
        if not os.path.exists(self.ruta_archivo):
            print("[AVISO] Archivo de configuración ausente. Cargando valores por defecto.")
            return self.config_por_defecto.copy()
        
        try:
            # Apertura explícita del archivo en modo lectura con codificación UTF-8 para tildes y eñes.
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                # Validar que el contenido decodificado sea un diccionario válido.
                if not isinstance(datos, dict):
                    raise ValueError("El contenido del archivo JSON no es un diccionario válido.")
                return datos
            
        except (json.JSONDecodeError, ValueError) as e:
            # Manejo específico para archivos corruptos o con formato JSON inválido.
            print(f"[ERROR CRÍTICO] El archivo de configuración está corrupto ({e}).")
            print("[INFO] Intentando restaurar desde el archivo de respaldo (.bak)...")
            return self._restaurar_desde_respaldo()
        
        except PermissionError:
            # Manejo de errores ante la falta de permisos de lectura en el sistema operativo.
            print("[ERROR] No hay permisos de lectura sobre el archivo de configuración.")
            print("[INFO] Degradando al comportamiento por defecto.")
            return self.config_por_defecto.copy()
        
            
        
        
        