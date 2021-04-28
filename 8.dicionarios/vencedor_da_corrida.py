from math import sqrt

def calcula_tempo(aceleracao):
    tempo  = sqrt(200/aceleracao)
    return tempo

atletas = dict()

while True:
    nome = input("Digite o nome do atleta. [sair PARA PARAR]").strip()

    if nome == 'sair':
        break

    aceleracao = float(input(f"Digite a aceleração da performance de {nome}"))

    atletas[nome] = calcula_tempo(aceleracao)

## REVISAR!!!
menor = list(atletas.values())[0]
campeao = list(atletas.keys())[0]
for k, v in atletas.items():
    if v < menor:
        menor = v
        campeao = k

print(f'O vencedor é {campeao} com tempo de conclusão de {menor} s')

    