def junta_listas(listas):
    planarizada = []
    for lista in listas:
        for e in lista:
            planarizada.append(e)

    return planarizada



lista = [[1, 2, 3], [4, 5, 6], [7, 8], [9], [10]]

print(junta_listas(lista))