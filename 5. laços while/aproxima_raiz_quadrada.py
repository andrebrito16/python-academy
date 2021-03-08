def aproxima_raiz(n):
    i = 1
    while i**2 <= n:
        i += 1
        
    if n - (i-1)**2 < abs(n - i**2):
        return i-1
    else:
        return i
    