# Algoritmo 1: Palíndromos

texto_1 = "ana"
texto_2 = "barrilete cosmico"
texto_3 = "yo hago yoga hoy"
texto_4 = "arriba la birra"
texto_5 = "arriba la barra"

# Recordemos el slicing:
print(texto_1[::-1])

"""
[::-1]
El primer ':' Significa desde el principio.
El segundo ':' Hasta el final. 
-1 desde atras para adelante
"""

# ¿Qué pasa en este ejemplo?
print(texto_3[::-1])

def enterText():
    return input("Ingrese el texto a analizar: ")

def es_palindromo(texto):
    texto = texto.replace(" ", "")  # Elimina los espacios
    return texto == texto[::-1]  # Compara con su versión invertida

# Pedir el texto al usuario y analizarlo
texto_ingresado = enterText()
resultado = es_palindromo(texto_ingresado)

print("Es palíndromo" if resultado else "No es palíndromo")
