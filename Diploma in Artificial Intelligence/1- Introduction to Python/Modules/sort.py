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