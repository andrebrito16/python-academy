def junta_nome_sobrenome(nome, sobrenome):
    junto = []
    c = 0
    while c < len(nome):
        junto.append(f'{nome[c]} {sobrenome[c]}')
        c += 1
    
    return junto