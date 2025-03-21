"""
I/O en Python

Ejemplos de cómo abrir, leer y escribir archivos en Python usando la sentencia with.
"""

# Leer un archivo
txt_file = "corpus.txt"
with open(txt_file, 'r') as inp:
    string_contenido = inp.read()

# Modos de apertura de archivos:
# 'r': read, lectura
# 'w': write, escritura
# 'a': append, agregar al final del archivo

# Escribir en un archivo
outpath = "nuevo.txt"
with open(outpath, 'w') as f:
    f.write("ejemplo de escritura")

# Leer el contenido del archivo escrito
with open(outpath, 'r') as f:
    contenido = f.read()
    print(contenido)  # Salida esperada: ejemplo de escritura

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