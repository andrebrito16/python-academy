def eh_primo(n):
    
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    c = 3
    while c < n:
        if n % c == 0:
            return False
        else:
            c += 2
    return True


def lista_primos(n):
    primos = []
    # Colocar os n primeiros números primos nessa lista
    controle = 0
    contador = 0
    while contador < n:
        if eh_primo(controle):
            primos.append(controle)
            contador += 1
            controle += 1
        else:
            controle += 1
    return sorted(primos, key=int)
print(lista_primos(10))

