from math import sqrt

class Point:
  
  def __init__(self, vx, vy):
    self.x = vx
    self.y = vy

  def distance_to(self, other_point):
    return sqrt((self.x - other_point.x)**2 + \
    (self.y - other_point.y)**2)

class Circulo:
  def __init__(self, centro, raio):
      self.centro = centro
      self.raio = raio

  def dentro(self, ponto):
    if self.centro.distance_to(ponto) < self.raio:
      return True
    else:
      return False

c = Point(2, 3)
R = 10

p = Point(4, 5)
q = Point(1000, 2000)

circ = Circulo(c, R)

print(circ.dentro(p))
print(circ.dentro(q))