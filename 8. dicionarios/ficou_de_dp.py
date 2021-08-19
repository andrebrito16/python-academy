#Primeiramente, espero que não!! kkkkkkkk

def notas_dp(notas):
    lista_dp = list()
    for aluno in notas:
        soma_notas = 0
        soma_notas = (aluno['PI'] + aluno['PF'])/2
        if soma_notas < 5:
            lista_dp.append(aluno['matricula'])

    return lista_dp
        


notas = [
    {'matricula': 123, 'PI': 7, 'PF': 3}, 
    {'matricula': 456, 'PI': 4, 'PF': 8}, 
    {'matricula': 789, 'PI': 5, 'PF': 1}, 
    {'matricula': 848, 'PI': 10, 'PF': 0},
    {'matricula': 357, 'PI': 1, 'PF': 2}
]

print(notas_dp(notas))