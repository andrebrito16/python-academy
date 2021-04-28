def apaga_repetidos(palavras):
  ocorrencias = []
  for p in palavras:
    if p not in ocorrencias:
      ocorrencias.append(p)
    else:
      ocorrencias.append("*")
  
  return "".join(ocorrencias)

print(apaga_repetidos('banana'))