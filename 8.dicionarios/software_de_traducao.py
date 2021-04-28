
def traduz(palavras, eng2port):
    traduzido = []
    for p in palavras:
        traduzido.append(eng2port[p])
    
    return traduzido



palavras = ['blackberry', 'cherry', 'plum', 'apple', 'pineapple']

eng2port = {'pineapple': 'abacaxi', 'plum': 'ameixa', 'blackberry': 'amora', 'apple': 'maçã', 'cashew': 'caju', 'cherry': 'cereja'}

print(traduz(palavras, eng2port))