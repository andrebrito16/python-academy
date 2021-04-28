def anagrama(p1, p2):
  letras_p1 = []
  letras_p2 = []

  for l1 in p1:
    letras_p1.append(l1)
  
  for l2 in p2:
    letras_p2.append(l2)

  if set(letras_p1) == set(letras_p2):
    return True
  else:
    return False
