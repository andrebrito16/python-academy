
logins = []
while True:
    contador = 0
    login = input("Insira um Login: ")
    
    if login == 'fim':
        break
    
    # Contador
    for l in logins:
        # Percorrer o elemento do array procurando login nele
        if login in l:
            contador += 1

    if login in logins:
        logins.append(f"{login}{contador}")
    else:
        logins.append(login)

# Imprimir o elemento
for elemento in logins:
    print(elemento)