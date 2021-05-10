def palavras_sao_iguais(palavras):
  p1 = palavras.split("-")
  if len(p1) < 2:
    return False
  modelo = p1[0]

  iguais = True

  for p in p1:
    if p != modelo:
      iguais = False


  return iguais


print(palavras_sao_iguais('abobrinha'))

# 'pega-pega', 'cri-cri', 'zum-zum'