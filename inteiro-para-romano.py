# Número de combate

entradas = int(input())

intToroman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
  50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}

print_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

for i in range(entradas):
  numero = int(input())
  for x in print_order:
    if numero != 0:
        quotient= numero//x

        #If quotient is not zero output the roman equivalent
        if quotient != 0:
            for y in range(quotient):
                print(intToroman[x], end="")

        #update numero with remainder
        numero = numero%x
  print()