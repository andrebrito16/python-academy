def encontra_maximo(matrix):
    maior_valor = 0
    for linha in matrix:
        for n in linha:
            if abs(n) > maior_valor:
                maior_valor = abs(n)

    return maior_valor

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(encontra_maximo(lista))