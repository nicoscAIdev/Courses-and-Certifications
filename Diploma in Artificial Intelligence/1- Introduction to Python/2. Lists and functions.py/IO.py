"""
I/O en Python

Ejemplos de cómo abrir, leer y escribir archivos en Python usando la sentencia with.
"""

# Modos de apertura de archivos:
# 'r': read, lectura
# 'w': write, escritura
# 'a': append, agregar al final del archivo

"""----------------------------------------------------------------------------------------------------------"""

# Leer un archivo
txt_file = "corpus.txt"
with open(txt_file, 'r') as inp:    # Lo que significa: con el archivo "corpus.txt" abierto en modo lectura
    string_contenido = inp.read()   # ("r" de read) con el alias inp, definimos la variable contenido usando
                                    # el método .read() para leer el archivo
"""-----------------------------------------------------------------------------------------------------------"""

# Escribir en un archivo
outpath = "nuevo.txt"
with open(outpath, 'w') as f:       # Lo que significa: con el archivo "corpus.txt" abierto en modo escritura
    f.write("ejemplo de escritura") # ("w" de write) con el alias inp, definimos la variable contenido usando
                                    # el método .write() para escribir el archivo
"""-----------------------------------------------------------------------------------------------------------"""

# Pedir input al usuario con validación
test = True
while test:
    usuario_dijo = input("Ingrese un numero: ")
    try:
        num = int(usuario_dijo)
        test = False
    except ValueError:
        print("No anduvo, intente de nuevo")

print(f"Su numero fue {num}! :D")