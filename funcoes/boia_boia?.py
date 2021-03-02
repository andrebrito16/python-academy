# R é o raio interno (em cm)

# r é o raio da seção transversal

# Peso P (Kg)

from math import pi
da = 0.997 # g/cm3

def will_it_float(p, R, r):
    volume = 2*(pi**2)*R*(r**2)
    densidade = (p*1000)/volume

    if densidade <=da:
        return True
    else:
        return False

