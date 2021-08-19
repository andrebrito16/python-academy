def subtracao_de_listas(lista1, lista2):
    lista3 = []
    for e in lista1:
        if e not in lista2:
            lista3.append(e)

    return lista3

lista1 = [2, 7, 3.1, 'banana']
lista2 = [2, 'banana', 'carro']

print(subtracao_de_listas(lista1, lista2))