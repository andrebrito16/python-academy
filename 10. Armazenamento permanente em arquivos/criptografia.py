with open("criptografado.txt", "r") as arquivo:
  data = arquivo.readlines()

for l in data:
  linha = ""
  for letra in l:
    if letra == "s":
      linha += "z"
    elif letra == "a":
      linha += "e"
    elif letra == "e":
      linha += "a"
    elif letra == "r":
      linha += "b"
    elif letra == "b":
      linha += "r"
    elif letra == "z":
      linha += "s"
    else:
      linha += letra

  print(linha)