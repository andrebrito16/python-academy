from math import sqrt
def calcula_pi(n):
    c = 1
    pi_2 = 0
    while c <= n:
        pi_2 += 6/c**2
        c += 1
    pi = sqrt(pi_2) 
    return pi
    