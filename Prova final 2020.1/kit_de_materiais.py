# Agrupar pela inicial e por turma

# Rece dicionário de turmas chaves são nomes de turmas 
# e valores listas com os nomes de alunos

# Devolve dic chaves são iniciais e valores nomes

# NOMES SEMPRE COM LETRA UPPER


def separa_por_inicial(turmas):
  iniciais = []
  nomes = []
  filtrado = {}

  for v in turmas.values():
    for nome in v:
      if nome not in nomes:
        nomes.append(nome)
        if nome[0] not in iniciais:
          iniciais.append(nome[0])
  # Iniciais já são as chaves do dicionário
  print(iniciais)
  print(nomes)

  for i in iniciais:
    flag = False
    for n in nomes:
      if n[0] == i:
        print(i, n, "Teste")
        if flag:
          filtrado[i].append(n)
        else:
          filtrado[i] = [n]
          flag = True

  return filtrado
exepmlo = {
    "Turma A": ["Ana", "Beatriz", "Jorge"],
    "Turma B": ["Cecília", "João"],
    "Turma C": ["Amanda", "Joana", "Lucas"],
}

print(separa_por_inicial(exepmlo))