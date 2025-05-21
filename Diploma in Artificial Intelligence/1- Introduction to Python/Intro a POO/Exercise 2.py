# EJERCICIO II: Herencia de clases - Rectángulo, Cuadrado y Cubo

# 1. Crear una clase llamada 'Rectangulo'
#    - Atributos:
#        a. base (float o int)
#        b. altura (float o int)
#    - Métodos:
#        a. area(): devuelve el área del rectángulo (base * altura)
#        b. get_base(): devuelve la base

# 2. Crear una clase llamada 'Cuadrado'
#    - Debe heredar de la clase Rectangulo
#    - Constructor:
#        a. Recibe un solo parámetro: lado
#        b. Llama al constructor de Rectangulo usando lado como base y altura (porque en un cuadrado ambos son iguales)

# 3. Crear una clase llamada 'Cubo'
#    - Debe heredar de la clase Cuadrado
#    - Constructor:
#        a. Recibe un parámetro: lado
#        b. Llama al constructor de Cuadrado con ese lado
#    - Método:
#        a. volumen(): devuelve el volumen del cubo
#           (Debe calcularse como: área de una cara * lado)
#           → Podés usar el método area() heredado de Rectángulo/Cuadrado

# 4. Ejemplo de uso (fuera de las clases):
#    - Crear una instancia de Rectangulo y mostrar su área
#    - Crear una instancia de Cuadrado y mostrar su área
#    - Crear una instancia de Cubo y mostrar su volumen


class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        area = self.base * self.altura
        
        return area

    def get_base(self):
        return self.base


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


class Cubo(Cuadrado):
    def __init__(self, lado):
        super().__init__(lado)

    def volumen(self):
        volumen = self.area() * self.base

        return volumen
    
# Se instancia Rectangulo
rectangulo = Rectangulo(10, 25)
print(f"El area  del Rectangulo es {rectangulo.area()}.")

# Se instancia Cuadrado
cuadrado = Cuadrado(4)
print(f"El area  del Cuadrado es {cuadrado.area()}.")

# Se instancia Cubo
cubo = Cubo(4)

print(f"El Volumen del Cubo es {cubo.volumen()}.")

