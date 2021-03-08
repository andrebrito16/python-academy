from math import factorial
def calcula_euler(x, n):
    #Quero o valor de e^x
    c = 0
    ex = 0
    while c < n:
        ex += x**c/factorial(c)
        c += 1
    return ex

