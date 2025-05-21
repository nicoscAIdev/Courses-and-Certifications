# EJERCICIO: Carrito de compras (Programación orientada a objetos)

# 1. Crear una clase llamada 'Item'
#    - Propiedades públicas:
#        a. nombre (str)
#        b. precio (float)
#        c. url_imagen (str, opcional - valor por defecto: '')
#    - El constructor (__init__) debe recibir nombre, precio y opcionalmente url_imagen.

# 2. Crear una clase llamada 'Carrito'
#    - Propiedad privada:
#        a. _lineas (lista de diccionarios). Cada diccionario representa una "línea del carrito".
#           Cada línea debe tener:
#               - "item": instancia de la clase Item
#               - "cantidad": número entero que indica cuántas unidades se agregan
#    - El constructor (__init__) debe inicializar la lista _lineas como vacía.

# 3. Método en la clase Carrito: agregar_item(item, cantidad)
#    - Recibe un ítem (objeto Item) y una cantidad.
#    - Agrega un diccionario a la lista _lineas con las claves:
#        - "item": el objeto Item recibido
#        - "cantidad": la cantidad recibida

# 4. Método en la clase Carrito: get_total()
#    - Recorre cada línea de _lineas.
#    - Calcula el total multiplicando precio * cantidad para cada línea.
#    - Devuelve la suma total del carrito.

# Ejemplo de uso (fuera de las clases):
#    - Crear instancias de Item
#    - Crear una instancia de Carrito
#    - Agregar ítems con distintas cantidades usando agregar_item
#    - Mostrar el total usando get_total()



class Item():
    def __init__(self, nombre, precio, url_imagen=''): 
        """ 
        Todas las propiedades del ítem son obligatorias menos url_imagen.
        En el ítem todas las propiedades son públicas.
        """
        self.nombre = nombre
        self.precio = precio
        self.url_imagen = url_imagen

class Carrito():


    def __init__(self): 
        """ 
        El Carrito siempre se inicializa con una lista de Ítems.
        En el carrito la única propiedad es privada. 
        """
        self._lista_productos= []


    def get_total(self):
        total = 0
        for detalle in self._lista_productos:
            total = total + (detalle['cantidad'] * detalle['item'].precio)
        return total


    def agregar_item(self, item, cantidad):
        detalle_producto = {
            'item': item,
            'cantidad': cantidad
        }
        self._lista_productos.append(detalle_producto)


# Parametrizacion
banana = Item("banana",49.5)
yoghurt = Item("yoghurt",32.5)
# Mostrar valores
print(banana)
print(banana.nombre ,banana.precio, yoghurt.nombre, yoghurt.precio)
print(yoghurt)
print(yoghurt.nombre, yoghurt.precio)

# Instanciar el carrito
carrito = Carrito()
print(carrito)

# Agregar productos
# Mostrar carrito
carrito.agregar_item(banana, 2) 
print(carrito.get_total())

carrito.agregar_item(yoghurt, 4)
print(carrito.get_total())