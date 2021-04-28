def lista_celulares(lista):
  celulares = []
  for item in lista:
    print(str(item)[0])
    if str(item)[0] == "+":
      if str(item)[5] == "9":
        celulares.append(item[5:])
    
    if len(str(item)) >= 10:
      if str(item)[2] == "9":
        celulares.append(item[2:])

    if str(item)[0] == "9":
      celulares.append(item)

  return celulares

print(lista_celulares(['+5511912345678']))