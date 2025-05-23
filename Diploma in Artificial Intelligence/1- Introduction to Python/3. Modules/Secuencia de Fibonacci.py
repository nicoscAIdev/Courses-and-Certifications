"""La secuencia de Fibonacci es la famosa secuencia que se define como:

F0=0 
F1=1 
Fn=Fn−1+Fn−2  para  n>1 
Esto nos da como resultado:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Ahora bien, ¿cómo podemos programar un algoritmo que compute esta serie hasta el número de Fibonacci 
en la posición n? Noten, que para obtener el número de Fibonacci n debemos antes computar el n-1 y el n-2, 
es decir, para tener un valor de la secuencia de Fibonacci debemos computar los previos. 
Cuando una función requiere llamarse a sí misma para poder realizar un cómputo decimos que la función es recursiva.

Entonces, tratemos de encarar el problema "traduciendo" la definición de la secuencia a código Python..."""

# Opción 1: solución recursiva.
def Fibonacci(n):
    # sigamos la definición de la secuencia de Fibonacci
    if n == 0: # Si n es 0 entonces devuelvo 0
        return 0
    if n == 1:
        return 1 # Si n es 1 entonces devuelvo 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2) # En cualquier otro caso devuelvo la suma de los dos números de Fibonacci previos


def recorrido(n):
    for i in range(n):
        print(Fibonacci(i))
        
def principal():
#   Entrada
    n = int(input("Ingrese un numero: "))

#   Proceso:
    Fibonacci(n)

#   Salida
    recorrido(n)
principal()


"""
def F_n_2(n): # borro las condiciones
    return F_n_2(n-1) + F_n_2(n-2)

F_n_2(5)

Salida:
maximum recursion depth exceeded

¿Por que?
borro las condiciones

"""
