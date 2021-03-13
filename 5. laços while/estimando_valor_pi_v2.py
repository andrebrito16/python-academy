def PiWallis(n):
    # 2/1 x 2/3 x 4/3 x 4/5 x 6/5 x 6/7
    # 1     2      3     4    5     6
    c = 2
    numerador = 2
    denominador = 1
    pi_2 = numerador/denominador
    
    while c <= n:
        if c % 2 == 0:
            denominador += 2
            pi_2 *= numerador/denominador
        else:
            numerador += 2
            pi_2 *= numerador/denominador
        c += 1
    return pi_2*2

print(PiWallis(2))