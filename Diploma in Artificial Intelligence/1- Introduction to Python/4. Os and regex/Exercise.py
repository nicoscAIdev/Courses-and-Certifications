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
    
    for archivo in archivos:
        print(archivo)
        if archivo.endswith(".txt"):
            # Separar nombre sin extensión
            nombre_sin_ext, ext = os.path.splitext(archivo)
            
            # Separar partes del nombre original
            partes = nombre_sin_ext.split("_")
            if len(partes) != 3:
                print(f"Nombre no compatible: {archivo}")
                continue

            id_archivo, nombre, apellido = partes

            # Nuevo nombre con formato correcto
            nuevo_nombre = f"{apellido}_{nombre}_{id_archivo}{ext}"

            # Rutas completas
            ruta_vieja = os.path.join(directorio, archivo)
            ruta_nueva = os.path.join(directorio, nuevo_nombre)

            # Comprobamos que no exista un archivo con el mismo nombre
            if os.path.exists(ruta_nueva):
                print(f"Ya existe: {ruta_nueva}, omitiendo...")
                continue

            # Renombrar
            os.rename(ruta_vieja, ruta_nueva)
            print(f"Renombrado: {archivo} → {nuevo_nombre}")

# Ejemplo de uso (reemplaza esta ruta con la carpeta real):
# renombrar_archivos("/ruta/a/la/carpeta")

renombrar_archivos("../4. Os and regex")

with open("garcia_jose_001.txt", 'w') as ar:
    datos = "Datos ingresados en el archivo"
    ar.write(datos)

