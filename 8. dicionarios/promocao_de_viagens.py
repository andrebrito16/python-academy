
# 1 mais buscado e 5 o menos
# 10% a 50% de desconto

def promocao_viagens(destinos):
    destinos_promocao = dict()
    for k, v in destinos.items():
        destinos_promocao[k] = (1-v[0]/10)*v[1]
        
    return destinos_promocao
    



destinos={
"Miami":[1,1000], 
"Ilhas Sandwich do Sul":[4,5000], 
"Barcelona":[2, 2000], "Antártica":[5,200], 
"Buenos Aires":[3,500]}

print(promocao_viagens(destinos))

destinos_promocao={ 'Miami': 900.0,'Ilhas Sandwich do Sul': 3000.0, 'Barcelona': 1600.0, 'Antártica':100.0, 'Buenos Aires': 350.0}


