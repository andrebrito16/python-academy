from math import sin, radians, asin, degrees


def snell_descartes(n1, n2, teta1):
    # n1*sin(teta1) = n2 * sin(teta2)
    # teta2 = n1
    teta2 = (n1 * sin(radians(teta1)))/n2
    return degrees(asin(teta2))
