def calcula_porcentagens(erros):
    total = 0
    resultados = dict()

    # Cálculo do total
    for v in erros.values():
        total += v
    
    for k1, v1 in erros.items():
        resultados[k1] = v1*100/total  


    return resultados

erros = {
    'Erro de indentação': 493,
    'Erro de parênteses': 1102,
    'Variável inexistente': 405,
}

print(calcula_porcentagens(erros))