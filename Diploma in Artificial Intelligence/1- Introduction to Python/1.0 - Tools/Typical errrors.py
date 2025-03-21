"""
Errores comunes en Python

Este archivo contiene una lista de errores comunes en Python, junto con su definición y un ejemplo de código.
"""

# 1. SyntaxError: Ocurre cuando el código tiene un error de sintaxis
print("Hola Mundo")  # Falta la comilla de cierre

# 2. IndentationError: Se produce cuando la indentación del código es incorrecta
edad = 20
if edad > 18:
    print("Mayor de edad")  # Falta la sangría

# 3. NameError: Sucede cuando se usa una variable que no ha sido definida
# print(valor)  # 'valor' no está definido

# 4. TypeError: Ocurre cuando se intenta realizar una operación con tipos incompatibles
# resultado = "El resultado es: " + 10  # No se puede concatenar string y número

# 5. IndexError: Se produce al acceder a un índice fuera del rango de una lista
lista = [1, 2, 3]
# print(lista[5])  # Índice fuera del rango

# 6. KeyError: Sucede cuando se intenta acceder a una clave inexistente en un diccionario
diccionario = {'a': 1, 'b': 2}
# print(diccionario['c'])  # 'c' no está en el diccionario

# 7. AttributeError: Ocurre al intentar acceder a un atributo o método que no existe en un objeto
texto = "Hola Mundo"
# texto.append("!")  # Las cadenas no tienen el método append

# 8. ValueError: Se produce cuando se usa un valor incorrecto para un tipo de dato
# numero = int("abc")  # No se puede convertir 'abc' a entero

# 9. ZeroDivisionError: Sucede al intentar dividir un número por cero
# resultado = 10 / 0  # División por cero no permitida

# 10. ImportError: Ocurre cuando un módulo no puede ser importado
# import modulo_inexistente  # El módulo no existe