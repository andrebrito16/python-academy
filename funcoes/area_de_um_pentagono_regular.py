from math import tan, radians

tg_36 = tan(radians(36))
print(tg_36)
def area_pentagono(lado):
    apotema = lado/(4*tg_36)
    area = 5*lado*apotema
    return area