def imprime_tabuada(n):
  for i in range(1, n+1):
    for j in range(1, n+1):
      print(i*j, end=' ')
    print()

imprime_tabuada(2)