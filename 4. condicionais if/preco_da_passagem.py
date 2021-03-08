km = float(input("Qual a distância em km? "))

if km <= 200:
    preco = km*(0.50)
else:
    preco = (200*(0.50))+((km-200)*0.45)

print(f"{preco:.2f}")