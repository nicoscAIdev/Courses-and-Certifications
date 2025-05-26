# ----------------------------------------
# 1. Clase Sujeto
# ----------------------------------------
# Crea una clase Sujeto que tenga:
# - Un atributo `id` (identificador del sujeto)
# - Un diccionario `resultados` donde se irán guardando los resultados de los experimentos

class Sujeto:
    def __init__(self, id):
        pass

    def agregar_resultado(self, nombre_experimento, resultado):
        pass

    def get_resultados(self):
        pass

# ----------------------------------------
# 2. Clase abstracta Experimento
# ----------------------------------------
# Crea una clase abstracta Experimento con:
# - Un método `realizar(self, sujeto)` que DEBE ser implementado por las subclases

from abc import ABC, abstractmethod

class Experimento(ABC):
    @abstractmethod
    def realizar(self, sujeto):
        pass

# ----------------------------------------
# 3. Clase TiempoReaccion (hereda de Experimento)
# ----------------------------------------
# Este experimento mide el tiempo que el usuario tarda en reaccionar.
# - Debe implementar el método `realizar(self, sujeto)`
# - Simula un tiempo de espera aleatorio
# - Registra cuánto tiempo pasa desde que se muestra un mensaje hasta que se presiona Enter

import time
import random

class TiempoReaccion(Experimento):
    def realizar(self, sujeto):
        pass

# ----------------------------------------
# 4. Clase Cuestionario (hereda de Experimento)
# ----------------------------------------
# Esta clase implementa un cuestionario simple:
# - Implementa `realizar(self, sujeto)`
# - Hace preguntas al usuario y guarda las respuestas

class Cuestionario(Experimento):
    def __init__(self):
        pass

    def realizar(self, sujeto):
        pass

# ----------------------------------------
# 5. Clase Reporte
# ----------------------------------------
# Esta clase genera un resumen de los resultados:
# - Método `generar(self, sujeto)` que imprime o devuelve los resultados almacenados

class Reporte:
    def generar(self, sujeto):
        pass

# ----------------------------------------
# 6. Ejecución del experimento
# ----------------------------------------
# - Crear una instancia de `Sujeto`
# - Crear instancias de `TiempoReaccion` y `Cuestionario`
# - Llamar al método `realizar()` con el sujeto como parámetro
# - Generar el reporte con la clase `Reporte`

if __name__ == "__main__":
    sujeto = Sujeto("Nico")
    experimento_1 = TiempoReaccion()
    experimento_2 = Cuestionario()

    experimento_1.realizar(sujeto)
    experimento_2.realizar(sujeto)

    reporte = Reporte()
    reporte.generar(sujeto)
