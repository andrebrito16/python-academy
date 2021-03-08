def eh_primo(n):
    
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    c = 3
    while c < n:
        print(c)
        if n % c == 0:
            return False
        else:
            c += 2
    return True