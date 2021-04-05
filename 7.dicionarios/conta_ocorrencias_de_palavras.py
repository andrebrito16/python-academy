

def conta_ocorrencias(palavras):
    ocorrencias = dict()
    for p in palavras:
        ocorrencias[p] = ocorrencias.get(p, 0) + 1

    return ocorrencias

palavras = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']

print(conta_ocorrencias(palavras))