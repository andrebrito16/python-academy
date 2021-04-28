
def remove_vogais(palavras):
  vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

  sem_vogais = list()

  for l in str(palavras):
    if l not in vogais:
      sem_vogais.append(l)

  

  return "".join(sem_vogais)

print(remove_vogais("aeioBA"))