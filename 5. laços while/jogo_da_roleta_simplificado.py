from random import randint

dinheiro = 100

while dinheiro > 0:
    print(f'Dinheiro disponível: {dinheiro}')
    numero_computador = randint(0, 36)

    aposta = int(input("Faça sua aposta"))
    if aposta == 0:
        break
    
    tipo_aposta = input("Escolha o tipo da aposta número, ou paridade. [n/p]: ")

    if tipo_aposta == 'n':
        aposta_n = int(input("Faça sua aposta"))
        if numero_computador == aposta_n:
            dinheiro = dinheiro + 35*aposta
            print(f"Você ganhou, seu dinheiro agora é {dinheiro}")
        else:
            dinheiro = dinheiro - aposta
            print(f'Você perdeu, seu dinheiro agora é {dinheiro}')
    
    if tipo_aposta == "p":
        par_impar = input("Escolha par ou ímpar [p/i]: ")
        if par_impar == "p" and numero_computador % 2 == 0:
            dinheiro = dinheiro + aposta
            print(f"Você ganhou, seu dinheiro agora é {dinheiro}")
        elif par_impar == "i" and numero_computador % 2 == 1:
            dinheiro = dinheiro + aposta
            print(f"Você ganhou, seu dinheiro agora é {dinheiro}")
        else:
            dinheiro = dinheiro - aposta
            print(f"Você perdeu, seu dinheiro agora é {dinheiro}")

