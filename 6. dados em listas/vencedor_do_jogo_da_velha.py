# Ganhadores na vertical
            # [0][0] = [1][0] = [2][0]
            # [0][1] = [1][1] = [2][1]
            # [0][2] = [1][2] = [2][2]

# Ganhadores na horizontal:
            # [0][0] = [0][1] = [0][2]
            # [1][0] = [1][1] = [1][2]
            # [2][0] = [2][1] = [2][2]
            # [0][0] = [1][1] = [2][2]

# Na diagonal:
            # [0][2] = [1][1] = [2][0]
            # 
def verifica_jogo_da_velha(tab):
    for linha in tab:

        #Verificação por linha (HORIZONTAL)
        if linha[0] == linha[1] and linha[1] == linha[2] and linha[0] == linha[2]:
            return linha[0]
    
    # Verificação na diagonal:
    if tab[0][2] == tab[1][1] == tab[2][0]:
        return tab[0][2]
    if tab[0][0] == tab[1][1] == tab[2][2]:
        return tab[0][0]
    
    # Verificação na VERTICAL:
    if tab[0][0] == tab[1][0] == tab[2][0]:
        return tab[0][0]
    elif tab[0][1] == tab[1][1] == tab[2][1]:
        return tab[0][1]
    elif tab[0][2] == tab[1][2] == tab[2][2]:
        return tab[0][2]
    else:
        return "V"

        


tab = [
    ['O', '.', 'X'],
    ['X', 'O', 'O'],
    ['.', 'X', 'O']
]
print(verifica_jogo_da_velha(tab))