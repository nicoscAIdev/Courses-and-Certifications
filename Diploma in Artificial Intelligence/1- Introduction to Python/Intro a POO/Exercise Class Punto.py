class Punto:
  pass
  def __init__(self, x, y, c):
    self.x = x
    self.y = y
    self.c = c

  def __str__(self):
     return f"({self.x}X, {self.y}Y, {self.c})"
    
  print(Punto(3,2,1))