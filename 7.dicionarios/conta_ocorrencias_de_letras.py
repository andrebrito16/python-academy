def conta_letras(palavras):
    contador = dict()


    for e in palavras:
        contador[e] = contador.get(e, 0) + 1
    
    return contador


print(conta_letras("banana nanica"))