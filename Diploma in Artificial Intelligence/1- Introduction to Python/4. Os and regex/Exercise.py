# EJERCICIO: Automatización de nombres de archivos

# Objetivo:
# Automatizar el renombramiento de archivos para que sigan un formato uniforme.

# Instrucciones:
# 1. Tienes una carpeta con archivos .txt que tienen nombres como:
#    "001_jose_garcia.txt", "002_ana_lopez.txt", etc.
# 2. Se desea renombrar todos los archivos en el directorio de forma que el nombre quede como:
#    "garcia_jose_001.txt", "lopez_ana_002.txt", etc.
# 3. Usar Python para automatizar este proceso usando el módulo os.

# Recomendaciones:
# - Usar funciones para mantener el código organizado.
# - Comprobar que el cambio no sobrescriba archivos.

# Esqueleto básico sugerido:

import os

def renombrar_archivos(directorio):

    archivos = os.listdir(directorio)
    for archivo in archivos: # Iterar sobre los archivos del directorio
        if archivo.endswith(".txt"): # Procesar solo archivos .txt
            
            pass

    # Separar cada parte del nombre (id, nombre, apellido)
    # Reordenar y renombrar el archivo
    

# Ejemplo de uso:
# renombrar_archivos("ruta/a/carpeta_con_archivos")
