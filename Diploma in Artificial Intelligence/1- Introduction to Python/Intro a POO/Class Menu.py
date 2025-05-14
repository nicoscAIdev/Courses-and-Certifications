class Menu():
    def __init__(self, items):
        self.items = items

    def precio(self, lista_items):
        precio = 0
        for nombre_item in lista_items:
            precio = precio + self.items[nombre_item]
        return precio

    def tamaño(self):
        return len(self.items)
    

mi_menu = Menu({'latte':25, 'medialuna':15})
mi_menu.precio(['latte','medialuna','medialuna'])
print(mi_menu.tamaño())
