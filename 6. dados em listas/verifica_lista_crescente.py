

def eh_crescente(lista):
    crescente = True
    c = 1
    while c < len(lista):
        if lista[c] > lista[c-1]:
            crescente = True
        else:
            return False
        
        c += 1
    return crescente


lista = [1, 3, 2, 7, 9]
print(eh_crescente(lista))