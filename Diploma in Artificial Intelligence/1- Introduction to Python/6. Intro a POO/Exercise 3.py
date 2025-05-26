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


import time # 1
import random # 2
import os # 3


#3) Debe guardarse un informe con el nombre del participante y 
# sus resultados. Para esto, crear una clase "CognitiveTest" 
# que gestione las tareas y el guardado del informe.

class CognitiveTest:
    
    def __init__(self, name):
        self.name = name
        self.resultados = {}
        

    def guardar_resultados(self):
        ruta_archivo = os.path.join("memory_test", "resultados_test.txt")
        with open(ruta_archivo, "w") as archivo:
            archivo.write(f"Test cognitivo de {self.name}!\n")
            for tarea, resultado in self.resultados.items():
                archivo.write(f"{tarea}: {resultado}\n")
        print("Ejecutado!")

#   Punto 1
    def reaction_time(self):
        print("Preparate...")
        time.sleep(3)

        start_time = time.time()
        input("Apreta Enter AHORA!")
        
        reaction_time = time.time() - start_time
        
    #   Guardamos resultados     
        self.resultados["reaction_time"] = round(reaction_time, 4)
        print(f"Tu tiempo de reacción es de {reaction_time:.4f} segundos.")
        return f"{round(reaction_time, 4)} segundos."


#   Punto 2
    def memory_test(self):
        
    #   Inicializamos     
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

    #   Declarar variable    
        lista_invertida = lista[::-1]

        if lista_invertida == entrada:
            self.resultados["memory_test"] = f"Test exitoso! Lista: {lista_invertida} | Entrada: {entrada}"
            print("Perfecto!!", lista_invertida, entrada)
        else:
            self.resultados["memory_test"] = f"Test fallado! Lista: {lista_invertida} | Entrada: {entrada}"
            print("Vuelve a intentarlo", lista_invertida, entrada)
    

if __name__ == "__main__":
    prueba = CognitiveTest('Nico')
    prueba.reaction_time()
    prueba.memory_test()
    prueba.guardar_resultados()
    



