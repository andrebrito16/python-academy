# Contar a quantidade de bagagens que execedem o tamanho limite

# Altura, largura e profundidade

def filtra_bagagens(bagagens, hlim, larlim, proflim):
    excedentes = 0
    for bag in bagagens:
        if bag[0] > hlim or bag[1] > larlim or bag[2] > proflim:
            excedentes += 1
    
    return excedentes



bagagens =  [[43.2, 30.5, 20.1], [60.0, 20.0, 20.0], [10.0, 10.0, 10.0], [50.3, 30.2, 30.0], [54.0, 30.2, 22.1], [ [[43.2, 30.5, 20.1], [60.0, 20.0, 20.0], [10.0, 10.0, 10.0], [50.3, 30.2, 30.0], [54.0, 30.2, 22.1]], [55, 35, 25]]