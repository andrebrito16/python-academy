def classifica_rima(v1, v2, v3, v4):
  if v1 == v2 == v3 == v4:
    return "outra"
  elif v1 == v3 and v2 == v4:
    return "alternada"
  elif v1 == v4 and v2 == v3:
    return "interpolada"
  elif v1 == v2 and v3 == v4:
    return "emparelhada"
  else:
    return "outra"
  
  

print(classifica_rima("ada", "ada", "ada", "ada"))