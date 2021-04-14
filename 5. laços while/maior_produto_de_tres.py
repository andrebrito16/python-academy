# from heapq import nlargest, nsmallest

# def maior_produto3(lista):

#     maior = nlargest(3, lista)
#     menor = nsmallest(2,lista)

    
#     #Verificar qual é o maior entre três positivos ou um positivo e dois negativos
#     maior_produto = max(maior[0] * maior[1] * maior[2], maior[0] * menor[0] * menor[1] )
#     return maior_produto

def maior_produto3(lista):

    menores = []
    maiores = []
    # Pegando os dois menores
    for i in range(0, len(lista)):
        if i < 0:
            menores.append(min(lista))
            del lista[lista.index(min(lista))]

        maiores.append(max(lista))
        del lista[lista.index(max(lista))]

   

    if len(menores) == 0:
        return maiores[0] * maiores[1] *maiores[2]
    else:
        return max(maiores[0] * menores[0] * menores[1], maiores[0] * maiores[1] * maiores[2])

    
lista = [-1, -1, 4, 2, 1]
print(maior_produto3(lista))