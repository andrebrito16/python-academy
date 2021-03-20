def soma_impares(lista):
    soma = 0
    for n in lista:
        if n % 2 == 1:
            soma += n
    
    return soma
