

def apurando_votos(candidatos, votos):
  resultado = "CANCELADA"
  maior_numero_votos = 0

  for candidato in candidatos:
    votos_validos = 0
    votos_nao_validos = 0
    for voto in votos:
      if voto not in candidatos:
        votos_nao_validos += 1
      else:
        if voto == candidato:
          votos_validos += 1
    
    if votos_validos > maior_numero_votos:
      maior_numero_votos = votos_validos
      resultado = candidato
    elif votos_nao_validos > maior_numero_votos:
      maior_numero_votos = votos_nao_validos
      resultado = "CANCELADA"
    elif votos_validos == maior_numero_votos or votos_nao_validos == maior_numero_votos:
      resultado = "CANCELADA"

  return resultado
  
print(apurando_votos(['Joaquim', 'Gertrude'], 
      ['Paulo', 'Maria', 'Joana', 'Gertrude', 'Marcos', 'Lucas', 'Joana']))