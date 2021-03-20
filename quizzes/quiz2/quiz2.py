""" 
0-11 anos: A.AA %
12-17 anos: B.BB %
18-25 anos: C.CC %
26-35 anos: D.DD %
36-59 anos: E.EE %
Acima de 60 anos: F.FF %
"""
# Inicialização das variáveis de controle:
def teste_quiz(idade):
    total = 0

    cont_0_11 = 0
    cont_12_17 = 0
    cont_18_25 = 0
    cont_26_35 = 0
    cont_36_69 = 0
    cont_acima_60 = 0
    while True:
        
        #idade = int(input("Insira sua idade: "))

        if idade < 0:
            break

        if  0<= idade <=11:
            cont_0_11 += 1
            total += 1
        elif 12 <=idade <=17:
            cont_12_17 += 1
            total += 1
        elif 18 <=idade <=25:
            cont_18_25 += 1
            total += 1
        elif 26 <=idade <=35:
            cont_26_35 += 1
            total += 1
        elif 36 <=idade <=59:
            cont_36_69 += 1
            total += 1
        else:
            cont_acima_60 += 1
            total += 1
    
""" 
0-11 anos: A.AA %
12-17 anos: B.BB %
18-25 anos: C.CC %
26-35 anos: D.DD %
36-59 anos: E.EE %
Acima de 60 anos: F.FF %
"""
print(f'0-11 anos: {cont_0_11*100/total:.2f}%')
print(f'12-17 anos: {cont_12_17*100/total:.2f}%')
print(f'18-25 anos: {cont_18_25*100/total:.2f}%')
print(f'26-35 anos: {cont_26_35*100/total:.2f}%')
print(f'36-59 anos: {cont_36_69*100/total:.2f}%')
print(f'Acima de 60 anos: {cont_acima_60*100/total:.2f}%')
