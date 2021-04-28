def nomes_com_vogais(nomes):
  vogais = ["A", "E", "I", "O", "U"]
  # Nomes que começam com vogais
  comecam = 0
  n_comecam = 0
  for nome in nomes:
    if nome[0] in vogais:
      comecam += 1
    else:
      n_comecam += 1

  return [comecam, n_comecam]
    

print(nomes_com_vogais(["André", "Carlos", "João", "Otavio", "Thiago"]))
