# Opción 2: armamos loop while que va a iterar n veces, donde n es la cantidad de elementos de la secuencia

def fibo(n):
    n = int(input("Ingrese el valor de n: "))
    """
    Inicializo a y b. En este caso "a" sería F_n-2 (F_0 al inicializarse)
    y "b" F_n-1 (F_1 al inicializarse)
    """

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

"""
fibo(10)
Salida:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

%timeit fibo(10)
Salida:
893 ns ± 5.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

(Menos tiempo que la solucion 1) 
"""