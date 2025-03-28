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

#Algoritmo 2:

# Opción 1: solución recursiva.
def F_n():
    n = int(input("Ingrese el valor de n: "))

    # sigamos la definición de la secuencia de Fibonacci
    if n == 0: # Si n es 0 entonces devuelvo 0
        return 0
    if n == 1:
        return 1 # Si n es 1 entonces devuelvo 1
    else:
        return F_n(n-1) + F_n(n-2) # En cualquier otro caso devuelvo la suma de los dos números de Fibonacci previos
F_n()

# Este algoritmo es mucho mas eficiente,
# ya que evita la ramificacion.

def fibo():
    """
    Inicializo a y b. En este caso "a" sería F_n-2 (F_0 al inicializarse)
    y "b" F_n-1 (F_1 al inicializarse)
    """
    n = int(input("Ingrese el valor de n: "))
    a, b = 0, 1
    secuencia = [a, b]

    if n == 0:
        return a
    elif n == 1:
        return b

    n_actual = 2 # número de iteración
    while n_actual < n:
        n_actual += 1 # sumo 1 a la iteración actual
        a, b = b, a + b # Este truquito es importante!
        secuencia.append(b) # guardo el nuevo b
    return secuencia
fibo()

# Algortimo 3

"""Solo destacamos el uso del '.pop(0)'
para guardar el elemento mas chico de una lista
en otra."""

# Algoritmo 4

def bubble_sort(lista):
    # n igual al largo de la lista
    n = len(lista)

    # Vamos a realizar una 'pasada' por cada elemento que tenemos en la lista.

    for i in range(n):

        # Creamos una variable que sirve como 'flag' para indicar si tuvimos que ordenar o no en la pasada actual
        # Esto lo podemos usar para terminar el algoritmo antes, ya que si no tuvimos que cambiar nada
        # en una pasada, tampoco lo vamos a tener que hacer en la siguiente

        ordenado = True

        # Vamos a comenzar recorriendo la lista de IZQUIERDA a DERECHA pero no hasta el final
        # Recordemos que con cada 'pasada' vamos a haber encontrado el valor más alto aún sin ordenar
        # Con lo cual, vamos a recorrer la lista desde el comienzo hasta el final menos los valores que ya ordenamos antes
        # Tip: recuerden que el índice de una lista tiene como máximo el valor de la longitud - 1 porque arranca en 0

        for j in range(n-i-1): # COMPLETAR: argumento de la función range()

            if lista[j] > lista[j+1]: # COMPLETAR: si el valor de la IZQUIERDA es mayor al de la derecha

                # Si es mayor, entonces vamos a intercambiar la posición del valor de la derecha con el de la izquierda

                # COMPLETAR: cambiar el valor de la izquierda por el de la derecha
                lista[j], lista[j+1] = lista[j+1], lista[j]

                # Como tuvimos que ordenar un par de elementos entonces tenemos que cambiar el flag
                # COMPLETAR: cambiar ordenado a False
                ordenado = False


        # Si no tuvimos que ordenar, salimos del loop
        if ordenado:
            # COMPLETAR: frenar loop
            break

    return lista