from heapq import nlargest, nsmallest
lista = [-10, -20, 20, 1]
def maior_produto3(lista):

    maior = nlargest(3, lista)
    menor = nsmallest(2,lista)

    
    #Verificar qual é o maior entre três positivos ou um positivo e dois negativos
    maior_produto = max(maior[0] * maior[1] * maior[2], maior[0] * menor[0] * menor[1] )
    return maior_produto

print(maior_produto3(lista))