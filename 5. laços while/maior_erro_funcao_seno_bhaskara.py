from math import sin, radians

def seno(teta):
    seno = sin(radians(teta))
    return seno

x = 0
diferenca = 0
maior = 0
while x <= 90:
    # Cálculo pela função Bhaskara
    sin_b = (4*x*(180-x))/(40500-x*(180-x))
    sin_m = seno(x)
    if abs(sin_m - sin_b) > diferenca:
        diferenca = abs(sin_m - sin_b)
        maior = x
    x += 1
print(maior)
