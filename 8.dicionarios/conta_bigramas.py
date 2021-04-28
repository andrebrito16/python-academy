def conta_bigramas(palavras):
    contador = dict()

    i = 0
    while i < len(palavras)-1:
        contador[palavras[i]+palavras[i+1]] = contador.get(f"{palavras[i]}{palavras[i+1]}", 0) + 1
    
        i += 1
    return contador


print(conta_letras("banana nanica"))