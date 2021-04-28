

def inverte_dicionario(dic):
    nomes = list()
    idades = list()
    dic_invertido = dict()
    for k, v in dic.items():
        if v not in idades:
            idades.append(v)

    idades.reverse()
    lista_idades = list()
    for e in idades:
        for k, v in dic.items():
            if v == e:
                lista_idades.append(k)

        dic_invertido[e] = lista_idades.copy()
        lista_idades.clear()
    
 
    return dic_invertido

nomes = {'Ana': 19, 'Bruno': 18, 'João': 19}

print(inverte_dicionario(nomes))