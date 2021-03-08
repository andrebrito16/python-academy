def pedra_papel_tesoura(j1, j2):
    if j1 not in "pedrapapeltesoura":
        return "Escolha pedra, papel ou tesoura para jogar"
        
    if j2 not in "pedrapapeltesoura":
        return "Escolha pedra, papel ou tesoura para jogar"
       
    if j1 == "pedra" and j2 == "tesoura":
        return "um"
    elif j1 == "tesoura" and j2 == "papel":
        return "um"
    elif j1 == "papel" and j2 == "pedra":
        return "um"
    elif j1 == j2:
        return "empate"
    else:
        return "dois"