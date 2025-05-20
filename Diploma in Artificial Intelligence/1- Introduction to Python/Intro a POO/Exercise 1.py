#Programación orientada a objetos
#En este ejercicio vamos a programar un carrito de compras.

#Para esto vamos a escribir dos clases: Carrito e Item.

#El ítem va a tener como propiedades un nombre, un precio
# y una url de la imágen que lo representa. Por default, la url se inicializa en blanco.

#El Carrito tiene como propiedad una lista de diccionarios, la variable _lineas.

#Los carritos se inicializan vacíos y luego se agregan líneas
# utilizando el método agregar_línea(). Cada línea es un diccionario 
# con dos claves: "ítem" que contiene un objeto de tipo ítem y "cantidad"
# según la cantidad que queremos agregar al carrito.

#Por último los carritos tienen un método get_total() que devuelve la suma 
# de los precios de los ítems, multiplicados por las cantidades que hay en cada línea.

class Carrito:
    
    def __init__(self):
        self._lineas = []
        pass

class Item:
    
    def __init__(self, nombre, precio, url):
        self.url = ""
        pass
    pass