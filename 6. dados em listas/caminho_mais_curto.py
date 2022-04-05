from math import sqrt

def caminho_mais_curto(caminhos):
  menor_distancia = -1
  caminho_mais_curto = []
  for caminho in caminhos:
    distancia = 0
    for i in range(len(caminho) - 1):
      distancia += sqrt((caminho[i+1][0] - caminho[i][0])**2 + (caminho[i+1][1] - caminho[i][1])**2)
    if distancia < menor_distancia or menor_distancia == -1:
      menor_distancia = distancia
      caminho_mais_curto = caminho
  
  return caminho_mais_curto