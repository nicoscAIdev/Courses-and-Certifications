# EJERCICIO IV: Herencia con Figuras geométricas

# 1. Crear una clase llamada 'Circulo'
#    - Atributo:
#        a. radio (float)
#    - Métodos:
#        a. area(): devuelve el área del círculo (π * radio^2)
#        b. get_radio(): devuelve el valor del radio

# 2. Crear una clase llamada 'Cilindro'
#    - Debe heredar de la clase Circulo
#    - Constructor:
#        a. Recibe dos parámetros: radio y altura
#        b. Llama al constructor de Circulo para inicializar el radio
#        c. Guarda la altura como atributo
#    - Método:
#        a. volumen(): calcula el volumen del cilindro (área de la base * altura)

# 3. Ejemplo de uso:
#    - Crear una instancia de Circulo y mostrar su área
#    - Crear una instancia de Cilindro y mostrar su volumen

import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2
    
    def get_radio(self):
        return self.radio

class Cilindro(Circulo):
    
    def __init__(self, radio, altura):
        super().__init__(radio)
        self.altura = altura

    def volumen(self):
        return self.area() * self.altura
    
if __name__ == "__main__":
    
    mi_circulo = Circulo(4.12)
    print(f"Área del círculo: {mi_circulo.area():.2f}")
    print(f"Radio del círculo: {mi_circulo.get_radio()}")

    mi_cilindro = Cilindro(4.12, 10)
    print(f"Volumen del cilindro: {mi_cilindro.volumen():.2f}")
