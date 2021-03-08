from math import radians, sin

v = float(input("Insira a velocidade: "))
angulo = float(input("Insira o ângulo em graus: "))

d = ((v**2)*sin(radians(2*angulo)))/9.8
print(d)

# Raio da Jaca é 2m

if d >= 98 and d <= 102:
    print("Acertou!")
elif d < 100:
    print("Muito perto")
elif d > 100:
    print("Muito longe")