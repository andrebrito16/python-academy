

def apurando_votos(candidatos, votos):
  apuracao = {}
  apuracao['CANCELADA'] = 0
  # Inicializa a lista de votos
  for candidato in candidatos:
    apuracao[candidato] = 0

  mais_votos = -1
  vencedor = None

  # Contabiliza os votos
  for voto in votos:
    if voto in candidatos:
      apuracao[voto] += 1
      if apuracao[voto] > mais_votos:
        mais_votos = apuracao[voto]
        vencedor = voto
    else:
      apuracao['CANCELADA'] += 1
      if apuracao['CANCELADA'] > mais_votos:
        mais_votos = apuracao['CANCELADA']
        vencedor = 'CANCELADA'


  return vencedor
  
print(apurando_votos(['Joaquim', 'Gertrude'], 
      ['Paulo', 'Maria', 'Joana', 'Gertrude', 'Marcos', 'Lucas', 'Joana']))