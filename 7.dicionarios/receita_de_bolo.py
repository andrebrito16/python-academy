# Receita em forma de dicionário. 
# Chaves são os igredientes e os valores a quantidades em xícaras ou colheres

# Retornar um dicionário, com as quantidades em ml

# X ml

def converte_receita(receita):
    convertido = dict()

    for k, v in receita.items():
        if len(v) > 1:
            # Verificar se é uma xícara:
            if v[2] == 'x':
                # Converter xícara para ml
                convertido[k] = f'{int(v[0])*250} ml'
            # Verificar se é uma colher de sopa
            elif v[2:] == 'colher de sopa' or v[2:] == 'colher de sopa':
                convertido[k] = f'{int(v[0])*15} ml'
            # Verificar se é uma colher de chá
            elif v[2:] == 'colher de chá' or v[2:] == 'colheres de chá':
                convertido[k] = f'{int(v[0])*5} ml'
        else:
            convertido[k] = v
            

    return convertido

receita = { 
    "ovos":"4", 
    "açúcar":"2 xícaras", 
    "leite":"1 xícara", 
    "farinha":"2 xícaras", 
    "fermento": "1 colher de sopa",
    "baunilha":"1 colher de chá" 
    }

saida = {
    'ovos': '4', 
    'açúcar': '500 ml', 
    'leite': '250 ml', 
    'farinha': '500 ml', 
    'fermento': '15 ml', 
    'baunilha': '5 ml'
    }

print(converte_receita(receita))