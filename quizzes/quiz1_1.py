contador = 0
q1 = input("Pergunta 1")
if q1 == "sim":
    contador += 1

q2 = input("Pergunta 2")
if q2 == "sim":
    contador += 1

q3 = input("Pergunta 3")
if q3 == "sim":
    contador += 1

q4 = input("Pergunta 4")
if q4 == "sim":
    contador += 1

q5 = input("Pergunta 5")
if q5 == "sim":
    contador += 1

if contador == 2:
    print("Alguma coisa")
elif 3<=contador <=4:
    print("outra coisa")
else:
    print("...")

    