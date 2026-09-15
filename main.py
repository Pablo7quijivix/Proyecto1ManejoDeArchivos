"""
El objetivo de este archivo (modulo) es tener un punto de entrada principal 
para la ejecucion del programa, de esta manera por este modulo se inicializa 
el gestor de persistencia y llamamos por aca a la interfaz grafica que se ha
creado con tkinter. De esta manera tenemos organizado todo de manera modular 
para que todo sea facil de organizar y de entender.

"""
from persistencia import GestorPersistencia
from interfaz import AplicacionPrincipal

def main():
    """
    Función principal que orquesta el arranque del sistema.
    Objetivo: Instanciar las clases principales y poner en marcha el bucle de eventos gráfico.
    """
    # Definir el nombre del archivo de configuración JSON
    archivo_config = "config.json"
    
    # Inicializar el módulo de persistencia de archivos
    gestor = GestorPersistencia(archivo_config)
    
    # Inicializar y ejecutar la aplicación gráfica principal
    app = AplicacionPrincipal(gestor)
    app.mainloop()

if __name__ == "__main__":
    main()
