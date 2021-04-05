

# Chaves são nomes de pessoas, e valores são idades

def agrupa_por_idade(dic):
    crianca = []
    adolescente = []
    adulto = []
    idoso = []

    for k, v in dic.items():
        if v <=11:
            crianca.append(k)
        elif 12<= v <= 17:
            adolescente.append(k)
        elif 18 <= v <= 59:
            adulto.append(k)
        elif v >= 60:
            idoso.append(k)
        
    dic_agrupado = {
        'criança': crianca,
        'adolescente': adolescente,
        'adulto': adulto,
        'idoso': idoso
    }

    return dic_agrupado

dicionario = {'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}
print(agrupa_por_idade(dicionario))