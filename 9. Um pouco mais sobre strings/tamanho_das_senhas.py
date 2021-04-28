def tamanho_minimo(texto, nMin):
  palavras = texto.split()
  senhas = list()

  for p in palavras:
    if len(str(p)) > nMin:
      senhas.append(p)

  return senhas

print(tamanho_minimo("frase para a função que filtra as palavaras", 5))
