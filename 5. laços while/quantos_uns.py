def quantos_uns(n):
    cont = 0
    for alg in str(n):
        if alg == '1':
            cont += 1
    return cont