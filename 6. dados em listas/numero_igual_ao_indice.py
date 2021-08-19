def numero_no_indice(lista):
    n_lista = []
    c = 0
    while c < len(lista):
        if lista[c] == c:
            n_lista.append(c)
        c += 1
    return n_lista

lista = [0, 10, 2, 30, 4]

print(numero_no_indice(lista))