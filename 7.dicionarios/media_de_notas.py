def calcula_media(lista):
    soma = 0
    tot = 0
    for e in lista:
        for v in e.values():
            soma += v
            tot += 1
    return soma/tot
    
    

alunos = [ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5} ]
print(calcula_media(alunos))