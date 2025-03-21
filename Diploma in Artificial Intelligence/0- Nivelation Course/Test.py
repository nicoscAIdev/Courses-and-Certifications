#Ejercicio de porcentajes

#Juan tiene 3 manzanas y 1 pera Pedro tiene 2 manzanas y 4 peras

#¿Que porcentaje de frutas tienen en total?

import pandas as pd

df = pd.DataFrame({"manzanas": [3, 2], "peras": [1, 4]}, index=["Juan", "Pedro"])

print(df)
