def fatorial(n):
    cont = n 
    fatorial = 1
    while n > 0:
        fatorial *= n
        n -= 1
    return fatorial