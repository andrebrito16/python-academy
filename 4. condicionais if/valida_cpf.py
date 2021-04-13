

def valida_cpf(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11):
    valido = True

    if n1 == n2 == n3 == n4 == n5 == n6 == n7 == n8 == n9 == n10 == n11:
        return False

    calc1 = ((n1*10 + n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2)*10) % 11
    if calc1 == 10:
        if 0 == n10:
            valido = True
        else:
            valido == False
    else:
        if calc1 == n10:
            valido = True
        else:
            valido = False

    
    calc2 = ((n1*11 + n2*10 + n3*9 + n4*8 + n5*7 + n6*6 + n7*5 + n8*4 + n9*3 + n10*2)*10) % 11

    if calc2 == 10:
        if 0 == n11:
            valido = True
        else:
            valido = False
    else:
        if calc2 == n11:
            valido = True
        else:
            valido = False
    
    return valido

print(valida_cpf(5, 2, 9, 9, 8, 2, 2, 4, 7, 2, 5))