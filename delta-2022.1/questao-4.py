def imprime_cabecalho(n):
  print('+-'*n, end='')
  print('+')

def imprime_linha(n):
  print('| '*(n+1), end='')
  print()

def imprime_grade(n):
  imprime_cabecalho(n)
  for i in range(n):
    imprime_linha(n)
    imprime_cabecalho(n)



imprime_grade(1)