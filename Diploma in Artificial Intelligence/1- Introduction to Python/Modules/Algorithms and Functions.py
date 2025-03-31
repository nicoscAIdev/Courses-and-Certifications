

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

