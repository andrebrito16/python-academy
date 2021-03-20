# 9 quesitos e 4 avaliações

def calcula_escola(notas):
    soma = 0
    for a in notas:
        pos_min = a.index(min(a))
        del a[pos_min]
    
    for n in notas:
        for nota in n:
            soma += nota

    return soma

tom_maior = [[9.9, 9.9, 10, 9.9], [10, 9.9, 9.8, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 9.9, 9.9, 9.8]]

print(calcula_escola(tom_maior))