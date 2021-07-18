# Distância de pontos
from math import sqrt
def entregador_mais_proximo(restaurante, entregadores):
  mais_proximo = 0
  xp = restaurante[0]
  yp = restaurante[1]

  distancia_base = sqrt((xp - entregadores[0][0])**2 + (yp - entregadores[0][1])**2)

  for c in entregadores:
    distancia = sqrt((xp - c[0])**2 + (yp - c[1])**2)
    if distancia < distancia_base:
      distancia_base = distancia
      mais_proximo = entregadores.index(c)

  return mais_proximo


restaurante = [15, 20]
entregadores = [
    [28, 4],
    [63, 87],
    [192, 643],
    [16, 19],
    [523, 32],
]

print(entregador_mais_proximo(restaurante, entregadores))