

def compras_da_semana(receitas, pratos):
    igredientes = dict()
    for p in pratos:
        for k, v in receitas[p].items():
            igredientes[k] = igredientes.get(k, 0) + v
        


    return igredientes



receitas = {
    'Bolo de chocolate': {
        'Leite': 0.25,
        'Óleo': 0.25,
        'Ovo': 2.0,
        'Farinha': 0.5,
        'Açúcar': 0.2,
        'Achocolatado': 0.3
    },
    'Bolinho de chuva': {
        'Óleo': 1.0,
        'Leite': 0.3,
        'Ovo': 3.0,
        'Farinha': 0.6,
        'Açúcar': 0.3
    },
    'Mingau': {
        'Açúcar': 0.1,
        'Maizena': 0.1,
        'Leite': 0.25
    }
}

pratos = ['Bolinho de chuva', 'Bolo de chocolate', 'Bolinho de chuva'] 

print(compras_da_semana(receitas, pratos))