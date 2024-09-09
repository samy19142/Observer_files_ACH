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
DATA_BASE = config['base_de_datos']
INTERVAL_SCANN = config['intervalo_escaneo']

def calculate_hash(path_file):
    hash_md5 = hashlib.md5()
    with open(path_file,'rb') as f:
        for chunk in iter(lambda:f.read(4096),b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def init_db():
    conn = sqlite3.connect(DATA_BASE)
    cursor= conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS archivos
    (nombre TEXT, hash TEXT UNIQUE, fecha_creacion TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

def add_file(name,hash_archivo):
    conn = sqlite3.connect(DATA_BASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO archivos (nombre, hash, fecha_creacion) VALUES (?, ?, datetime('now'))",
                       (name, hash_archivo))
        conn.commit()
        print(f"Archivo {name} agregado a la base de datos.")
    except sqlite3.IntegrityError:
        print(f"El archivo {name} ya existe en la base de datos.")
    finally:
        conn.close()

if __name__ == "__main__":
    print()