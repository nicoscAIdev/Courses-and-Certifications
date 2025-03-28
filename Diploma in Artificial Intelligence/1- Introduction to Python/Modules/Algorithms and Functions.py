# Algoritmo 1: Palíndromos

texto_1 = "ana"
texto_2 = "barrilete cosmico"
texto_3 = "yo hago yoga hoy"
texto_4 = "arriba la birra"
texto_5 = "arriba la barra"

# Recordemos el slicing:
print(texto_1[::-1])


# ------Opción 1:--------
#     usar slicing
def es_palindromo():
    texto = input("Ingrese alguno de los textos: ")
    texto = texto.replace(" ", "")
    # vean cómo podemos hacer slicing por un string, en sentido inverso, recorriendo la lista de atrás para adelante.
    if texto == texto[::-1]:
        return print("Es palindromo")
    else: 
        return print("No es palindromo")
es_palindromo()

def es_palindromo():
    texto = input("Ingrese alguno de los textos: ")
    texto = texto.replace(" ", "")
    # vean cómo podemos hacer slicing por un string, en sentido inverso, recorriendo la lista de atrás para adelante.
    if texto == "".join(reversed(texto)):
        return print("Es palindromo")
    else: 
        return print("No es palindromo")
es_palindromo()
