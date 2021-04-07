def mais_medalhas(paises):
    medalhas_max = 0
    melhor_pais = ''
    for p in paises:
    
        if p['ouro'] > medalhas_max:
            
            melhor_pais = p['nacionalidade']
            medalhas_max = p['ouro']
    return melhor_pais

paises = [
    {'nome': 'Fulano', 'nacionalidade': 'brasileiro', 'ouro': 2, 'prata': 0, 'bronze': 0}, 
    {'nome': 'Beltrano', 'nacionalidade': 'paraguaio', 'ouro': 1, 'prata': 1, 'bronze': 1}, 
    {'nome': 'Ciclano', 'nacionalidade': 'brasileiro', 'ouro': 0, 'prata': 0, 'bronze': 1}
    ]

print(mais_medalhas(paises))