from math import sqrt

# h2 = c1**2 + c2**2
def encontra_cateto(c1, h):
    c2 = sqrt((h**2)-(c1**2))
    return c2