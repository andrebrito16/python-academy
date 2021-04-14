# [ [Nome do aluno, [notas dos quizzes], [AI, AF]] 

def calcula_estado(alunos):
    retorno_alunos = list()
    for aluno in alunos:
        media = 0
        # Descartar a menor nota do quiz
        del aluno[1][aluno[1].index(min(aluno[1]))]
        
        # Nota do quiz
        soma_quiz = 0
        for q in aluno[1]:
            soma_quiz += q
        
        media_quiz = soma_quiz/4

        media = 0.1*media_quiz + 0.4*aluno[2][0] + 0.5*aluno[2][1]

        if media >=5:
            retorno_alunos.append([aluno[0], 'A'])
        else:
            retorno_alunos.append([aluno[0], 'R'])

    return retorno_alunos

alunos = [
    ['Maria', [5.0, 10.0, 0.0, 10.0, 10.0], [6.7, 8.0]],
    ['Joao', [0.0, 10.0, 10.0, 10.0, 0.0], [6.7, 2.0]],
    ['Joana', [10.0, 0.0, 10.0, 0.0, 10.0], [6.7, 8.0]]
]
print(calcula_estado(alunos))
