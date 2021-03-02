def classifica_triangulo(a, b, c):
    if a == b == c:
        return "equilátero"
    if a == b or a == c or b == c:
        return "isósceles"
    else:
        return "escaleno"
    
print(classifica_triangulo(1, 1, 2))