
# Argumentos: (dia, mês e ano)

# True se a data for válida, false se não for

# Verificar se o ano possui 29/2

def valida_data(dia, mes, ano):
    # Verificar se o ano é bissexto:
    if ano % 400 == 0:
        bissexto = True
    elif ano % 4 == 0 and ano % 100 != 0:
        bissexto = True
    else:
        bissexto = False
    
    if bissexto:
        meses = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Buscar o mês pelo índice na lista

    if mes > 12:
        return False
  
    if dia > meses[mes-1]:
        valido = False
    else:
        valido = True
    
    

    return valido


print(valida_data(32, 13, 2020))