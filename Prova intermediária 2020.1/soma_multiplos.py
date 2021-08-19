

def soma_multiplos(n1, n2):
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    soma = 0
    for n in range(0, (maior*10)+1):
        if n % n1 == 0:
            soma += n
        if n % n2 == 0:
            soma += n
        if n % n2 ==0 and n % n1 == 0:
            soma -= n
    
    return soma


print(soma_multiplos(2, 5))