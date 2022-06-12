def posicoes_minusculas(string):
  posicoes = []
  for i in range(len(string)):
    if string[i].islower():
      posicoes.append(i)
  return posicoes

# Do jeito difícil
def posicoes_minusculas(string):
  posicoes = []
  for i in range(len(string)):
    if string[i] >= 'a' and string[i] <= 'z':
      posicoes.append(i)
  return posicoes