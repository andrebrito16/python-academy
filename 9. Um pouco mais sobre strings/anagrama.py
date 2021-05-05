def anagrama(p1, p2):

  for l in p1:
    i2 = p2.find(l)
    if i2 < 0:
      return False
    p2 = p2[:i2] + p2[i2+1:]
  
  return len(p2) == 0

print(anagrama("alegriag", "alegriaa"))