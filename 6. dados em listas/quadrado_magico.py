# [0][0] + [1][0] + [2][0] == [0][1] + [1][1] + [2][1]  == [0][2] + [1][2] + [2][2]



def quadrado_magico(matrix):
    quadrado_magico = False
    # Verificação da linha
    ref_linha = 0
    soma_linha = 0
    for n in matrix[0]:
        ref_linha += n
    

    for linhas in matrix:
        for n in linhas:
            soma_linha += n
        if soma_linha == ref_linha:
            quadrado_magico = True
    
   
    # Verificação das colunas:
    # [0][0] + [1][0] + [2][0]
    ref_coluna = matrix[0][0]
    soma_coluna = 0
    coluna = 0
    
    while coluna < len(matrix):
        if ref_coluna == matrix[coluna][0]:
            quadrado_magico = True
        else:
            quadrado_magico == False
        coluna += 1
    
    # Verificação da diagonal:
    diagonal = 0
    d1 = 0
    d2 = 0
    while diagonal < len(matrix):
        d1 += matrix[diagonal][-1]
        d2 += matrix[diagonal][diagonal]
        diagonal += 1

    print("Valor da D1", d1)
    print("Valor da D2", d2)
    if d1 == d2:
        quadrado_magico = True
    else:
        quadrado_magico = False
    




    return quadrado_magico


matriz = [  [6, 1, 8], 
            [7, 5, 3], 
            [2, 9, 4] 
        ]
print(quadrado_magico(matriz))