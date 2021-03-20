def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    crescente = False
    descrecente = False
    c = 1
    while c < len(lista):
        if lista[c] > lista[c-1]:
            crescente = True
        elif lista[c] < lista[c-1]:
            descrecente = True
        c += 1
        
    if descrecente and crescente:
        return "nenhum"
    elif descrecente:
        return "decrescente"
    elif crescente:
        return "crescente"
    else:
        return "nenhum"

lista = [1, 5, 2, 7, 3, 7, 4]

print(classifica_lista(lista))