palavras_com_a = list()
while True:
    
    palavra = input("Insira uma palavras: ")

    if palavra == "fim":
        break

    if palavra[0] == "a":
        palavras_com_a.append(palavra)

for e in palavras_com_a:
    print(e)
    