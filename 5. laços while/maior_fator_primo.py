def fatores_primos(n):

    fatores = []
    d = 2
    while n > 1:
        while n % d == 0:
            fatores.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1:
                fatores.append(n)
            break
    return fatores

def maior_fator_primo(n):
    fp = fatores_primos(n)
    return max(fp)

# 243423423330