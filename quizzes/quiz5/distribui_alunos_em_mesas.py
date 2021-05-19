

with open('alunosEmbaralhados.txt', 'r') as arquivo:
  conteudo = arquivo.readlines()

  numero_alunos_mesas = int(input("Quantos alunos por mesa? ").strip())
  # numero_alunos_mesas = 1
  
  mesa = 1
  cont = 0
  linhas = []
  for nome in conteudo:
    if cont < numero_alunos_mesas:
      # print(mesa, nome.split('\n')[0])
      linhas.append(f"{mesa} {nome}")
      cont += 1
    else:
      mesa += 1
      cont = 1
      linhas.append(f"{mesa} {nome}")
  print(linhas)
  with open('mesas.txt', 'w') as arquivo_saida:
    arquivo_saida.writelines(linhas)
    