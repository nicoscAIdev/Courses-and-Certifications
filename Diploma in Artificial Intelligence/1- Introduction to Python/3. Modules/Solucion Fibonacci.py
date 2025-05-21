import time

def F_n(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return F_n(n-1) + F_n(n-2)

def fibo(n):
    a, b = 0, 1
    secuencia = [a, b]

    if n == 0:
        return a
    elif n == 1:
        return b

    n_actual = 2
    while n_actual < n:
        n_actual += 1
        a, b = b, a + b
        secuencia.append(b)
    return secuencia

def principal():

#   Entrada
    n = int(input("Ingrese el valor de n: "))
    punto1 = F_n(n)

    # Medir el tiempo de fibo(n)
    tiempo_inicio = time.time()
    punto2 = fibo(n)
    tiempo_fin = time.time()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio

#   Salida
    print(f"El resultado de F_n({n}) es: {punto1}")
    print(f"La secuencia de Fibonacci hasta {n} es: {punto2}")
    print(f"Tiempo de ejecución de fibo({n}): {tiempo_ejecucion} segundos")
    
principal()
