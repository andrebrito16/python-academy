def estritamente_crescente(lista):
    sorted_list = []
    for e in lista:
        if len(sorted_list) == 0:
            sorted_list.append(e)
        
        if e > sorted_list[len(sorted_list)-1]:
            sorted_list.append(e)

    return sorted_list

lista = [10, 15, 11, 12, 13, 14]
print(estritamente_crescente(lista))