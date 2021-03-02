n = float(input("Insira um número: "))
soma = 0
while True:
    soma += n
    if n != 0:
        n = float(input("Insira outro: "))
        
    else:
        break
    
print(soma)