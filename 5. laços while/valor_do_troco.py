

# Compra de 4,50 e pagou com 10.
# Retorna uma lista ['1 nota(s) de R$5', '1 moeda(s) de R$0.5']
notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]


def calcula_troco(compra, pago, notas):
    lista_troco = []
    troco = pago - compra
    valor_cedula = int(troco)
    valor_moeda = troco - int(troco)
    
    total_cedula = 0
    #Contadores de cédulas
    cont_100 = 0
    cont_50 = 0
    cont_20 = 0
    cont_10 = 0
    cont_5 = 0 
    cont_2 = 0

    #Contadores de moedas
    cont_1 = 0
    cont_05 = 0
    cont_025 = 0
    cont_01 = 0
    cont_005 = 0

    # Cálculo de cédulas
    for nota in notas:
        if valor_cedula >= nota and nota >= 1:
            while valor_cedula >= nota:
                valor_cedula -= nota
                if nota == 100:
                    cont_100 += 1
                if nota == 50:
                    cont_50 += 1
                if nota == 20:
                    cont_20 += 1
                if nota == 10:
                    cont_10 += 1
                if nota == 5:
                    cont_5 += 1
                if nota == 2:
                    cont_2 += 1
                # Excessão da moeda
                if nota == 1:
                    cont_1 += 1

    if cont_100 > 0:
        lista_troco.append(f'{cont_100} nota(s) de R$ 100')
    if cont_50 > 0:
        lista_troco.append(f"{cont_50} nota(s) de R$ 50")
    if cont_20 > 0:
        lista_troco.append(f"{cont_20} nota(s) de R$ 20")
    if cont_10 > 0:
        lista_troco.append(f"{cont_10} nota(s) de R$ 10")
    if cont_5 > 0:
        lista_troco.append(f"{cont_5} nota(s) de R$ 5")
    if cont_2 > 0:
        lista_troco.append(f"{cont_2} nota(s) de R$ 2")

    #Calculo de moedas
    for moeda in notas:
        if valor_moeda >= moeda and moeda > 0:
            while valor_moeda >= moeda:
                print("MOEDA", moeda)
                valor_moeda -= moeda
                if moeda == 0.5:
                    cont_05 += 1
                if moeda == 0.25:
                    cont_025 += 1
                if moeda == 0.1:
                    cont_01 += 1
                if moeda == 0.05:
                    cont_005 += 1

    if cont_1 > 0:
        lista_troco.append(f"{cont_1} moeda(s) de R$ 1")
    if cont_05 > 0:
        lista_troco.append(f"{cont_05} moeda(s) de R$ 0.5")
    if cont_025 > 0:
        lista_troco.append(f"{cont_025} moeda(s) de R$ 0.25")
    if cont_01 > 0:
        lista_troco.append(f'{cont_01} moeda(s) de R$ 0.1')
    if cont_005 > 0:
        lista_troco.append(f'{cont_005} moeda(s) de R$ 0.05')
    
    
    return lista_troco


print(calcula_troco(25, 28, notas))
