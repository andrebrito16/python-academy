

def calcula_dano(heroi):
    forca_total = 0
    forca_total += heroi['força']

    for equipamento in heroi['equipamentos']:
        forca_total += equipamento["força"]


    return forca_total


heroi = {
    'nome': 'Herói',
    'força': 4,
    'vida': 25,
    'equipamentos': [
        {
            'nome': 'Martelo Mortal',
            'força': 15, 
        },
        {
            'nome': 'Luva Leve',
            'força': 2, 
        },
    ],
}

print(calcula_dano(heroi))