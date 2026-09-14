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
        
    