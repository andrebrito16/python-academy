# n -> n/2 ( se n for par)
# n -> 3*n + 1 (se n for ímpar)

# Mais número menor que 1000 que gera a sequencia mais longa
# Sequência termina em 1
c = 1


maior_sequencia = []
numero_gerador = 0

while c < 1000:
    sequencia = []
    n = c
    sequencia.append(n)
    while n != 1:
        if n % 2 == 0:
            n /= 2
            sequencia.append(n)
        else:
            n = 3*n + 1
        
            sequencia.append(n)
    if len(sequencia) > len(maior_sequencia):
        maior_sequencia = sequencia
        numero_gerador = c
    c += 1

print(numero_gerador)


