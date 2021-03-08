remessa = [ [4,1,20],[4,2,20],[4,3,20],[4,4,20] ]

def pacotes_correio(remessa):
    total = len(remessa)
    controle = 0
    print(total)
    tamanho = remessa[0][2]
    while controle+1 <= len(remessa):
        #Vendo se a ordem está errada:
        if controle+1 != remessa[controle][1]:
            return "ordem errada"

        #Verificando o tamanho:
        if remessa[controle][2] != tamanho:
            return "tamanho errado"

        controle += 1
    # Comparação do número na posição 0 e o número na posição 1
    if remessa[len(remessa)-1][0] != remessa[len(remessa)-1][1]:
        return "pacote perdido"

    return "tudo certo"
    

print(pacotes_correio(remessa))