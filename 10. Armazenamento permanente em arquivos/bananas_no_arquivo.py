
with open("macacos-me-mordam.txt", "r") as arquivo:
  conteudo = arquivo.read()

cont = 0
for p in conteudo.split():
  if p.strip().lower() == "banana":
    cont += 1

print(cont)