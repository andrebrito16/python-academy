from math import sqrt

def encontra_uma_raiz(a, b, c):
    x = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    return x

print(encontra_uma_raiz(1, 1, -90))