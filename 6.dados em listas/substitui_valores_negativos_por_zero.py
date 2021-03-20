def zera_negativos(lista):
    n_lista = []
    c = 0
    
    for e in lista:
        if e < 0:
            n_lista.append(0)
        else:
            n_lista.append(e)

    return n_lista

lista = [0, 2, 4, 5, 6, -2, -4, -5]
print(zera_negativos(lista))