def acha_bigramas(palavra):
  bigramas = list()
  for c in range(0, len(palavra)):
    if c+1 < len(palavra):
      if f"{palavra[c]}{palavra[c+1]}" not in bigramas:
        bigramas.append(f"{palavra[c]}{palavra[c+1]}")

  return bigramas



print(acha_bigramas("babador"))