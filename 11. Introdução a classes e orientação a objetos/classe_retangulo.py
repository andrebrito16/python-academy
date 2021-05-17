class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Retangulo:
  def __init__(self, vpie, vpsd):
    self.pie = vpie
    self.psd = vpsd

  def calcula_perimetro(self):
    a = self.psd.x - self.pie.x
    b = self.psd.y - self.pie.y

    return 2*(a+b)

  def calcula_area(self):
    a = self.psd.x - self.pie.x
    b = self.psd.y - self.pie.y

    return a*b

