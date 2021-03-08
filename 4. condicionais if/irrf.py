import math from sin, cos, tan, radians
salario = float(input("Insira seu salário bruto: "))
dependentes = int(input("Insira o número de dependentes: "))

# Contribuição para o INSS

if salario <=1045:
    inss = salario * (7.5/100)
elif 1045.01 <= salario <=2089.60:
    inss = salario * 0.09
elif 2080.61 <=salario <=3134.40:
    inss = salario * 0.12
elif 3134.41 <= salario <=6101.06:
    inss = salario * 0.14
else:
    inss = 671.06

# Base de cálculo

base = salario - inss - (dependentes*189.59)

//

#Cálculo da dedução
if base <=1903.98:
    deducao = 0
    al = 0
elif 1903.99 <=base <=2826.65:
    deducao = 142.80
    al = (7.5/100)
elif 2826.66 <=base <=3751.05:
    deducao = 354.80
    al = 0.15
elif 3751.06 <=base <=4664.68:
    deducao = 636.13
    al = 0.225
else:
    deducao = 869.36
    al = 0.275



# Cálculo do IRRF
irrf = (base*al) - deducao
print(irrf)