def raiz_quadrada(n):
    c = 1
    soma = n
    raiz = 0
    while soma > 0:
        soma -= c
        c += 2
        raiz += 1
    return raiz
    

print(raiz_quadrada(48))
    