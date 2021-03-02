velocidade = float(input("Insira a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80)*5
    print(f"Você foi multado! O valor da multa é {multa:.2f}")
else:
    print("Não foi multado")