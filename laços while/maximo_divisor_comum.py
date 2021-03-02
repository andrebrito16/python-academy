
def maximo_divisor_comum(n1, n2):
    c = 2
    maximo = 1
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    while c < maior:
        # c < 6
        if n1 % c == 0 and n2 % c == 0:
            maximo = c
        
        c += 1

    return maximo
        

print(maximo_divisor_comum(24, 19))