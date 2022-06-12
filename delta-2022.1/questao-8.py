# def ocorrencias_letras(string):
#   letras = {}
#   for i in string:
#     if i in letras:
#       letras[i] += 1
#     else:
#       letras[i] = 1
#   return letras

# Without using if and else
def ocorrencias_letras(string):
  letras = {}
  for i in string:
    letras[i] = letras.get(i, 0) + 1

  return letras

print(ocorrencias_letras("banana"))
