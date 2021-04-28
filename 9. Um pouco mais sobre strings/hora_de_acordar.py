def converteHora(hora):
 
  # Se a hora for 00:
  if int(hora[:2]) == 0:
    return f"12{hora[2:]} AM"

  # Se for 12
  if int(hora[:2]) == 12:
    return f"12{hora[2:]} PM"
  
  # Se for de tarde
  if int(hora[:2]) > 12:
    
    return f"0{int(hora[:2]) - 12 }{hora[2:]} PM"

  return f"{hora} AM"

print(converteHora("09:39"))