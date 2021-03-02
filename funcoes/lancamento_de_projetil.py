from math import sin, radians, sqrt
g = 9.8

def calcula_distancia_do_projetil(v, teta, y0):
    t2 = (1 + sqrt(1 + ((2*g*y0)/(v**2*(sin(teta))**2)))  )
    d = (v**2)/(2*g)*t2*sin(2*teta)
    return d
