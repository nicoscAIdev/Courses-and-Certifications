import re

# a- extraer números de una oración.
texto = "Mi nombre es Juan y mi teléfono es 1564232324"
regla_de_busqueda = "\d+"
# print(texto)
print(re.findall(regla_de_busqueda, texto))

texto = "Mi nombre es Carlos y mi teléfono es 114232324 154232324"
regla_de_busqueda = "(?:15|11)\d+"
re.findall(regla_de_busqueda,texto)

texto = "Mi nombre es asfasfeaf33 y mi teléfono es 11 6423-2324"
regla_de_busqueda = "(?:15|11)[0-9\s-]{6,10}"
re.findall(regla_de_busqueda,texto)

texto = "REPORTE DE PERFOMANCE - MES DE julio y agosto"
regla_de_busqueda = "(MES DE (?:JULIO|AGOSTO|JUNIO))"
re.findall(regla_de_busqueda,texto, flags=re.IGNORECASE)