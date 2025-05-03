import re

# a- extraer números de una oración.
texto = "Mi nombre es Juan y mi teléfono es 1564232324"
regla_de_busqueda = "\d+"
# print(texto)
print(re.findall(regla_de_busqueda, texto))

