def calcula_total_da_nota(precos, quantidade):
    soma = 0
    c = 0
    while c <= len(precos)-1:
        soma += precos[c]*quantidade[c]
        c += 1

    return soma
