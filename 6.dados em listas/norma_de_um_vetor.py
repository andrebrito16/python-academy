from math import sqrt

def calcula_norma(vetor):
    soma_dos_valores = 0
    for e in vetor:
        soma_dos_valores += e**2

    norma = sqrt(soma_dos_valores)
    return norma
