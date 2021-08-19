def inverte_lista(lista):
    n_lista = []

    c = len(lista)-1
    while c >= 0:
        n_lista.append(lista[c])
        c -= 1


    return n_lista


lista = [1, 4, 5, 7, 9, 5, 3, 6, 7, 4, 0]
print(inverte_lista(lista))