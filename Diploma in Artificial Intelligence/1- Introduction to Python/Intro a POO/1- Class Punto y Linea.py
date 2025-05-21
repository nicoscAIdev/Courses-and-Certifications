class Punto:
  pass
  def __init__(self, x, y):
    self.x = x
    self.y = y


  def __str__(self):
     return f"({self.x}X, {self.y}Y)"
    
#Agregar un método 'largo' que permita calcular el largo de la línea. 
# Para ello vale la pena recordar que ésta se puede calcular como 
# la hipotenusa del triángulo rectángulo que se forma con los dos puntos.

class Linea():
    def __init__(self, p1:Punto, p2:Punto):
        self.p1= p1
        self.p2 = p2
    
    def largo(self):
        largo = ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)**(1/2)
        return largo
  
p1 = Punto(4,1)
p2 = Punto(7,5)

l = Linea(p1,p2)

print(l.largo())