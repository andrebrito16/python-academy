
def monta_dicionario(l1, l2):
    dic = dict()
    c = 0
    while c < len(l1):
        dic[l1[c]] = l2[c]
        c += 1

    return dic