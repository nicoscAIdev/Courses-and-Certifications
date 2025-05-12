class Persona():
    def __init__(self, nombre, apellido, edad, contacto):
        # Este método puede tomar parámetros que asignamos a los atributos, que luego podemos acceder
        self.edad = edad # este es un atributo
        self.contacto = contacto # este es otro atributo
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        # este método muestra el nombre completo a partir del nombre y apellido
        nombre_completo = ', '.join([self.apellido,self.nombre])
        return nombre_completo

    def saludar(self):
        print(f'Hola mi nombre es {self.nombre_completo()}',
              f'y te dejo mi mail por si necesitás algo: {self.contacto}')

instancia_ejemplo = Persona('Matías Andrés','Ripley', 24, 'mati@rip.com')
instancia_ejemplo.saludar()


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