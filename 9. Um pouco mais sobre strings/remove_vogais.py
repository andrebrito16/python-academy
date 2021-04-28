def remove_vogais(palavra):
  nova_palavra = palavra
  vogais = ["a", "e", "i", "o", "u"]
  for v in vogais:
    if v in nova_palavra:
      nova_palavra = nova_palavra.replace(v, "")
  return nova_palavra



print(remove_vogais("banana"))