amigos = ['Mateo', 'Nico', 'Claudia', 'Ernestina', 'Paola']

#  indexación o acceso al indice
print(amigos[0])
""""Salida: Mateo"""

print(amigos[-1])
"""Salida: Paola"""

#  slicing [comienzo : final : intervalo]

# arranco en 0 hasta el final, con el paso default (1)
print(amigos[:]) 
""" Salida: 'Mateo', 'Nico', 'Claudia', 'Ernestina', 'Paola' """

# arranco en 0 y el primero sin incluir es el 1, con el paso default (1)
print(amigos[:1]) 
"""Salida: 'Mateo' """