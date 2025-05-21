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

def principal():
    lista1 = [0,3,5,8,9]
    lista2 = [4,5,6]

    resultado = merge_sorted(lista1, lista2)
    print(resultado)

principal()