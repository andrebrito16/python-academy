def primos_entre(a, b):
    lista = []
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    c = menor
    
    cont = 0
    
    while c <= maior:
        divisores = 0
        for d in range (1, c+1):
            if c % d == 0:
                divisores += 1
        if divisores == 2:
            lista.append(c)
            cont += 1
        c += 1
    return lista