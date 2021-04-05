
def primeiras_ocorrencias(palavra):
    indices = dict()
    letras = list()

    for p in palavra:
        if p not in letras:
            letras.append(p)

    for l in letras:
        indices[l] = palavra.find(l)
    

    return indices


palavra = 'abracadabra'

print(primeiras_ocorrencias(palavra))