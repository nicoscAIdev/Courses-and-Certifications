

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

def merge_sorted(lista_1,lista_2):
    resultado = []
    while len(lista_1) > 0 or len(lista_2) > 0: # mientras alguna lista tenga valores
        # Vamos a recorrer las listas hasta que no queden más elementos en ninguna.
        if len(lista_1) > 0: # si la primera lista tiene valores
            if len(lista_2) > 0:
                # Este es el caso donde quedan elementos en las dos listas.
                # Aquí elegimos el menor de los primeros elementos
                if lista_1[0] <= lista_2[0]:
                    resultado.append(lista_1.pop(0))
                else:
                    resultado.append(lista_2.pop(0))
            else:
                # Este es el caso donde lista_1 todavía tiene elementos pero lista_2 no
                resultado.append(lista_1.pop(0))
        else:
            # Si no quedan elementos en la lista_1 pero seguimos dentro del while loop,
            # es porque quedan elementos en la lista2
            resultado.append(lista_2.pop(0))
    return resultado


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