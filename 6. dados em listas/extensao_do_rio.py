from math import sqrt

def calcula_extensao(x, y):
    c = 1
    soma = 0
    while c < len(x):
        soma += sqrt((x[c] - x[c-1])**2 + (y[c] - y[c-1])**2)
        c += 1

    return soma


x = [275, 290, 310, 390, 480]
y = [75, 180, 120, 110, 150]

print(calcula_extensao(x, y))