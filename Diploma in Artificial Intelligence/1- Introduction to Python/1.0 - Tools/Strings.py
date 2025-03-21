# Strings
texto = "programación en python"
print(texto)

# Todo en mayuscula
print(texto.upper())
"""Salida: 'PROGRAMACIÓN EN PYTHON'"""

#También podemos usar los índices para traer más de un elemento al mismo tiempo, 
#                           usando el slicing
#  lleva tres parámetros: comienzo (start), final (stop) e intervalo o paso (step).
#       [comienzo : final : intervalo] (en inglés es [start : stop : step] )
# programación en python
# 1234567890123456789012
#               -(654321)
print(texto[-6:23:1])
""""Salida: 'Python'"""

# En formato titulo
print(texto.title())
"""Salida: 'Programación En Python'"""

 # Devuelve una lista
print(texto.split())
"""Salida: 'programación', 'en', 'python'"""

#Verifica que es digito
print("1000".isdigit())
"""Salida: 'True'"""

# Reemplaza el texto del primer valor del parentesis por el segundo
print(texto.replace(' ', '...'))
"""Salida: 'programación...en...python'"""

# Se utiliza para verificar si todos los elementos son letras
print(texto.isalpha())
"""Salida: 'False'""" #Porque hay un espacio