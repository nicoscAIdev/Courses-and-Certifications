"""Para anticipar y manejar los errores, 
podemos usar la clausula **try** y **except**"""

try:
    print(a+b)
except Exception as e:
    print(f"El error fue {e}")


"""También podemos especificar qué hacer 
para distintos tipos de error:"""

lista_tuplas = [('3', 8),
                (5, 0),
                (3, ),
                (4, 6)]

for t in lista_tuplas:
    print(f"la tupla es {t}")

    try:
        print("intento dividir...")
        print(t[0] / t[1])
        print("éxito!")
    except IndexError:
        print('El largo está mal')
    except TypeError:
        print('Error en el tipo de datos')
    except ZeroDivisionError:
        print("No se puede dividir por cero")