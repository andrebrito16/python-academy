
def define_vencedores(numeros_sorteados, cartelas):
  mais_pontos_marcados = 0
  lista_jogadores_mais_marcaram = []
  for v in cartelas.values():
    pontos_jogador = 0
    for n in v:
      if n in numeros_sorteados:
        pontos_jogador += 1
    if pontos_jogador > mais_pontos_marcados:
      mais_pontos_marcados = pontos_jogador

  if mais_pontos_marcados == 0:
    return list(cartelas.keys())

  # Percorre tudo de novo e appenda os jogadores que marcaram mais pontos
  for k, v in cartelas.items():
    pontos_jogador = 0
    for n in v:
      if n in numeros_sorteados:
        pontos_jogador += 1
    if pontos_jogador == mais_pontos_marcados:
      lista_jogadores_mais_marcaram.append(k)
  
  return lista_jogadores_mais_marcaram