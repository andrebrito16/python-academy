n = [0, 2, 4, 6]

def verifica_progressao(n):
    eh_pa = False
    eh_pg = False
#Verificando se é uma PA:

#Razão da PA:
    r_pa = n[1] - n[0]

    if n[len(n)-1] == n[0] + (len(n)-1)*r_pa:
        eh_pa = True


#Verificando se é uma PG:

#Razão da PG: 
    if n[0] != 0:
        r_pg = n[1]/n[0]
        if n[len(n)-1] == n[0]*(r_pg**(len(n)-1)):
            eh_pg = True
    
    if eh_pa and eh_pg:
        return "AG"
    elif eh_pa:
        return "PA"
    elif eh_pg:
        return "PG"
    else:
        return "NA"

print(verifica_progressao(n))