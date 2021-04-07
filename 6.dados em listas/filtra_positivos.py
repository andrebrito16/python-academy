# def filtra_positivos(lista):
#     # positivos = []
#     for e in lista:
#         if e < 0:
#             lista.remove(e)

#     return lista



def filtra_positivos(lista):
    return list(filter(lambda x: x>0, lista))

    return positivos

lista = [-2, 2, 3, 4, 5]

print(filtra_positivos(lista))