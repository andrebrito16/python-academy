

def interseccao_valores(dic1, dic2):
    valores = list()
    for v in set(dic1.values()) & set(dic2.values()):
        valores.append(v)

    return valores

dic1 = {
    'valor1': 1,
    'valor2': 2
}


dic2 = {
    'valor1': 3,
    'valor2': 2
}

print(interseccao_valores(dic1, dic2))

