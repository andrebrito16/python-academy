def junta_nomes(masculinos, femininos, sobrenomes):
  nomes = []
  for nome in masculinos:
    for sobrenome in sobrenomes:
      nomes.append(f"{nome} {sobrenome}")

  for nome in femininos:
    for sobrenome in sobrenomes:
      nomes.append(f"{nome} {sobrenome}")
  

  return nomes

print(junta_nomes(["Joao", "Jose"], ["Maria", "Maria"], ["Silva", "Pereira"]))