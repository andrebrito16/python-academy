

def calcula_media(atletas, pais):
  soma_idades = 0
  atleas_nacionalidade = 0
  for atleta in atletas.values():
    if atleta['nacionalidade'] == pais:
      soma_idades += atleta['idade']
      atleas_nacionalidade += 1

  return soma_idades / atleas_nacionalidade  


