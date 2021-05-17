class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

from math import sqrt

class Circulo:
  def __init__(self, centro, raio):
    self.centro = centro
    self.raio = raio

  def contem(self, ponto):
    if sqrt((self.centro.x - ponto.x)**2 + \
  (self.centro.y - ponto.y)**2) < self.raio:
      return True
    else:
      return False
