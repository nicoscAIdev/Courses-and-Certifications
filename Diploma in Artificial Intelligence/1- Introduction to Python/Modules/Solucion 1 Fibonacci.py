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

"""La recursividad es esta propiedad por la cual una función se llama a sí misma. 
Toda función recursiva necesita tener un punto de corte, para ponerle un fin a esta llamada. 
De lo contrario vamos a tener un error.

Más adelante vamos a ejecutar varias veces la función F_n, 
generando la lista de valores de Fibonacci... 

¿qué creen que va a pasar?

recursividad: se necesita un punto de corte, de lo contrario veamos qué pasa."""

def F_n_2(n): # borro las condiciones
    return F_n_2(n-1) + F_n_2(n-2)
"""
F_n_2(5) 
Salida: 
Maximum recursion depth exceeded
"""
import timeit

timeit.fibo(10)

"""
Salida: 
893 ns ± 5.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
"""

