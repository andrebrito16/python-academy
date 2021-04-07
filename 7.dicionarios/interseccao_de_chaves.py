def interseccao_chaves(dic1, dic2):  
       

    return list(set(dic1.keys()) & set(dic2.keys()))

dic1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

dic2 = {'A': 5, 'B': 6, 'C': 7, 'E': 8}

print(interseccao_chaves(dic1, dic2))