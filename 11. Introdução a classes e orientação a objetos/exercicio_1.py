from math import sqrt

class Point:
  def __init__(self, vx, vy):
    self.x = vx
    self.y = vy

class Retangulo:
  def __init__(self, p1, p2):
    self.pie = p1
    self.psd = p2

  def perimetro(self):
    a = self.psd.x - self.pie.x
    b = self.psd.y - self.pie.y

    return 2*(a+b)

  def area(self):
    a = self.psd.x - self.pie.x
    b = self.psd.y - self.pie.y

    return a*b

pa = Point(2, 3)
pb = Point(4, 5)

r = Retangulo(pa, pb)

print(r.perimetro())
print(r.area())