

def agrupa_por_nacionalidade(atletas):
  nacionalidades = {}
  for atleta, dados in atletas.items():
    nacionalidade = dados['nacionalidade']
    if nacionalidade in nacionalidades:
      prev_list = nacionalidades[nacionalidade]
      prev_list.append(atleta)
      nacionalidades[nacionalidade] = prev_list
    else:
      nacionalidades[nacionalidade] = [atleta]

  return nacionalidades
