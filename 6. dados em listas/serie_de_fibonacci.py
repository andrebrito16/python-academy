def calcula_fibonacci(n):
    t1 = 0
    t2 = 1
    cont = 3
    final = [1]
    while cont <= n+1:
        t3 = t2 + t1
       
        final.append(t3)
        t1 = t2
        t2 = t3
        cont += 1
    print(final)
    return final
