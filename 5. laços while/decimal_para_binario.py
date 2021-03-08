def decimal_para_binario(n):
    restos = []
    if n < 0:
        return "Negativo"
    
    while n >= 1:
        resultado = n//2
        resto = n%2
        restos.append(str(resto))
        n = resultado
        
    return ''.join(restos[::-1])

print(decimal_para_binario(10))



