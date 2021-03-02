from math import pi, e, sqrt

def calcula_gaussiana(x, mi, sigma):
    f = (1/(sigma*sqrt(2*pi))) * e**(-0.5*((x-mi)/sigma)**2)
    return f