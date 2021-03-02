def calcula_posicao(s0, v0, a, t):
    s = s0 + (v0*t) + (a*(t**2)/2)
    return s