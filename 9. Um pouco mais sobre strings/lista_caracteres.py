def lista_caracteres(palavra):
  palavras = []
  for p in str(palavra):
    if p not in palavras:

      palavras.append(p)

  return palavras

print(lista_caracteres("Abacate"))
