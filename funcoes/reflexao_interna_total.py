from math import sin, radians


def reflexao_total_interna(n1, n2, teta2):
    # n1*sin(teta1) = n2 * sin(teta2)
    # teta2 = n1
    teta1 = (n2 * sin(radians(teta2)))*n1
    print(teta1)
    if teta1 > 1:
        return True
    else:
        return False

