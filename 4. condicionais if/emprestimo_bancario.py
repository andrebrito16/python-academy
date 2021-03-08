casa = float(input("Insira o valor da casa que quer comprar: "))
salario = float(input("Insira o seu salário: "))
anos = int(input("Insira a quantidade de anos a pagar: "))

mensal = casa/(anos*12)

if mensal > (0.3*salario):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')