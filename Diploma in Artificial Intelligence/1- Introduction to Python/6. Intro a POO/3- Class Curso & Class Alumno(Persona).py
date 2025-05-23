class Curso:
    max_alumnos = 35 # definimos variable de clase

    def __init__(self, nombre, duracion, alumnos = None, costo=10):
        self.nombre = nombre
        self.duracion = duracion
        if alumnos is None:
            self.alumnos = []
        else:
            self.alumnos = alumnos
        self.costo = costo # costo tiene un valor por default

    def inscribir_alumno(self, nombre):
        self.alumnos.append(nombre) # para poder llamar a alumnos tengo que usar self.
        print(f'Se agregó al alumno/a {nombre}')

    def tomar_lista(self):
        for a in self.alumnos:
            print(f'Alumno: {a}')

    def resumen(self):
        print(f'Curso {self.nombre}, {self.duracion} clases pensadas para {len(self.alumnos)} alumnos\n'
              f'Por el muy módico precio de {self.costo} rupias.',
              # llamo variable de clase:
              f'La ocupación actual es del {round(len(self.alumnos)/self.max_alumnos,2)*100}%')

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

class Alumno(Persona):
    def __init__(self, curso: Curso, *args):
        """
        Alumno pertence a un Curso (una instancia de la clase Curso) y, además, tiene otros atributos que pasaremos
        a la clase previa
        """
        self.curso = curso
        super().__init__(*args) # inicializamos la clase 'madre'. La llamamos usando super() y ejecutamos el constructor
        # Nótese también que desempacamos args

    def saludar(self): # Sobrecarga de métodos, ver abajo
        super().saludar() # ejecutamos el método de Persona .saludar() y agregamos más cosas a este método
        print('Estoy cursando:')
        self.curso.resumen()

    def estudiar(self, dato): # También podemos definir nuevos métodos
        self.conocimiento = dato

curso_python = Curso('Python', 6)

scott = Alumno(curso_python, 'Scott', 'Henderson', 49, 'sh@mail.com')
scott.saludar()