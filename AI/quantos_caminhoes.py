

def quantos_caminhoes(lista):
    # Máximo de 2000Kg em cada caminhão
    soma = 0
    total = 1
    for n in lista:
        if soma+n <= 2000:
            soma += n
        else:
            total += 1
            soma = 0
            soma += n
    
                


    
    
   

    return total

lista = [1000, 500, 400, 200, 50, 450, 1300, 500, 1450, 100]
print(quantos_caminhoes(lista))