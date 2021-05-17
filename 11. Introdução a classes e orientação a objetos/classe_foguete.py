class Foguete:
  def __init__(self, velocidade):
    self.velocidade = velocidade/3.6 # Converte a velocidade para m/s
    self.distancia_percorrida = 0
  
  def atualizar(self, tempo_decorrido):
    self.tempo = 0
    
    self.tempo = tempo_decorrido - self.tempo
    # S = S0 + v0*t
    self.distancia_percorrida = self.distancia_percorrida + self.velocidade*self.tempo
    return self.distancia_percorrida/1000


foguete = Foguete(10000)
print(foguete.atualizar(9))
print(foguete.atualizar(18))