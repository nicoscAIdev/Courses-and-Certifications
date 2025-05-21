# Armando una evaluación cognitiva con Python
# Han sido contratados por un hospital para programar una batería de evaluación 
# cognitiva ampliamente utilizada en la clínica de salud mental. 
# La misma debe tener las siguientes tareas:

#1) Tarea de tiempo de reacción:

#Cuando el participante reciba la indicación, debe apretar una 
# tecla lo más rápido posible. Registrar el tiempo de reacción.

#2) Tarea de memoria
# El participante debe recibir una lista de números por 
# unos segundos, y luego debe recordarlos de atrás hacia
# adelante (es decir, dar vuelta mentalmente la lista de números)

#3) Debe guardarse un informe con el nombre del participante y 
# sus resultados. Para esto, crear una clase "CognitiveTest" 
# que gestione las tareas y el guardado del informe.

#BONUS:
#4) Tarea de vocabulario: el participante es presentado con una palabra y debe elegir su definición de un grupo de opciones.



# 1) Tarea de tiempo de reacción
# Pista: la función input('mensaje') le muestra al usuario el mensaje y espera su input

import time # 1
import random # 2

def reaction_time():
    print("Preparate...")
    time.sleep(3)

    start_time = time.time()
    input("Apreta Enter AHORA!")
    reaction_time = time.time() - start_time

    print(f"Tu tiempo de reacción es de {reaction_time:.4f} segundos.")

    return f"{round(reaction_time, 4)} segundos."



#2) Tarea de memoria
def memory_test():
    lista = [] 

    print("La prueba de memoria comenzara en unos segundos...")
    time.sleep(5)

#   Generamos la Lista
    for i in range(5):
        lista.append(random.randint(1, 10))
    print(lista)

#   Limpia el output de la celda para que el usuario deje de ver la lista de números presentada
    time.sleep(5)
    print("\n" * 50)

#   Pedimos la entrada
    entrada = input("Ingrese la lista invertida, separada por espacios: ")
    entrada = [int(num) for num in entrada.split()]

    
#   Comparar    
    lista_invertida = lista[::-1]
    if lista_invertida == entrada:
        return print("Perfecto!!", lista_invertida, entrada)
    else:
        return print("Vuelve a intentarlo", lista_invertida, entrada)

memory_test()