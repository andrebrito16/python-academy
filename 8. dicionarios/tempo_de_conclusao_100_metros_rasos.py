from math import sqrt

def calcula_tempo(dic):
    tempos = dict()
    for k, v in dic.items():
        tempos[k]  = sqrt(200/v)
        
    return tempos
# 200 = a*t**2

# t = sqrt(200/a)


atletas = {
    "André": 2.5,
    "João": 3.9
}

print(calcula_tempo(atletas))