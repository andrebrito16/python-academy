def eh_primo(n):
    if n == 1 or n == 0:
        return True
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
maior = 0
def maior_primo_menor_que(n):
    if n < 2:
        return -1
    if eh_primo(n):
        return n
    c = 0
    while c < n:
        if eh_primo(c):
            maior = c
        c += 1
    return maior

print(maior_primo_menor_que(-10))