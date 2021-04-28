
def mais_frequente(palavras):
    
    cont = 0
    mais_frequente = 0
    palavra_mais_frequente = ''
    while cont < len(palavras):
        indice = 0
        total = 0

        while indice < len(palavras):
            if palavras[indice] == palavras[cont]:
                total += 1
            indice += 1
        if total > mais_frequente:
            mais_frequente = total
            palavra_mais_frequente = palavras[cont]
        cont += 1

    return palavra_mais_frequente



palavras = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']    
print(mais_frequente(palavras))