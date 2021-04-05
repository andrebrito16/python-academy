
def mais_populoso(dic):
    maior_populacao = 0
    mais_populoso = ""
    for k, v in dic.items():
        
        soma = 0
        for k1, v1 in v.items():
            soma += v1
        if soma > maior_populacao:
            maior_populacao = soma
            mais_populoso = k
        
            
    return mais_populoso

brasil = {
    "São Paulo": {"São Paulo": 21571281, "Campinas": 3224443},
    "Minas Gerais": {"Belo Horizonte": 2385639, "Uberlândia": 611903},
}

print(mais_populoso(brasil))