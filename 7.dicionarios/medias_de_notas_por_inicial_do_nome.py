

def medias_por_inicial(dic):
    iniciais = list()
    medias = dict()
    for k, v in dic.items():
        if k[0] not in iniciais:
            iniciais.append(k[0])

    for e in iniciais:
 
        soma = 0
        cont = 0

        for k1, v1 in dic.items():
            if k1[0] == e:
                print(k1, v)
                soma += v1
                cont += 1
        media = soma/cont
        medias[e] = media
        

    return medias
    

nomes = {'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}

print(medias_por_inicial(nomes))