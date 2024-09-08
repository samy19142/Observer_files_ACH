import os
import time
import hashlib
import  sqlite3
import json
from watchdog.observers import Observer
from watchdog.events    import FileSystemEventHandler

#Leer Configuraciones
def init_configuration():
    pathConfig = os.path.join('configuraciones','config.json')
    with open(pathConfig,'r') as file_config:
        return json.load(file_config)
    
#Cargando Configuraciones globales
config = init_configuration()
#Desestructurar configuraciones
SHARED_FOLDER = config['carpeta_compartida']


if __name__ == "__main__":
    print(init_configuration())