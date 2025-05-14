#Ejercicio: Vamos a mejorar la clase anterior... En lugar de que el método precio reciba 
# una lista de strings, hagamos que reciba una lista de diccionarios cada uno con dos claves 
# nombre y cantidad que querríamos ordenar ¿Cuántos cuestan 10 lattes y 30 medialunas?

class Menu():
    def __init__(self, items):
        self.items = items

    def precio(self, lista_items):
        precio_total = 0
        for lista_pedido in lista_items:
          print(lista_pedido)  # <-- esto te muestra cada ítem
          nombre_producto = lista_pedido['nombre']
          precio_producto = self.items[nombre_producto]
          cantidad = lista_pedido['cantidad']
          precio_total = precio_total + precio_producto * cantidad
        return precio_total

    def tamaño(self):
        return len(self.items)
    

pedido = [
    {"nombre": "latte", "cantidad": 10},
    {"nombre": "medialuna", "cantidad": 30}
]


mi_menu = Menu({'latte': 25, 'medialuna': 15})
print(mi_menu.precio(pedido))
