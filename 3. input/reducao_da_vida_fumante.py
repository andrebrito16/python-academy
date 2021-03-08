# 1 cigarro tira 10 minutos da expectativa de vida

dia = int(input("Quantos cigarros voce fuma por dia?"))
anos = int(input("Ha quantos anos voce fuma?"))

total = (anos*365)*dia

minutos = total*10

dias = minutos/24/60

if dias < 0:
    print(f"Você não teve a expectativa de vida")
else:
    print(f"Expectativa de vida resumida em {dias} dias")


