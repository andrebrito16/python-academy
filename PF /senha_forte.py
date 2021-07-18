# True se for forte e False se for fraca

def valida_senha(senha):
  crit1 = False
  crit2 = False
  crit3 = False

  especiais = ['?', '!', '@', '#', '$', '%', '&', '*']
  # Precisa possuir dois

  lista_especiais = []
  for e in especiais:
    for c in senha:
      if e == c:
        if c not in lista_especiais:
          lista_especiais.append(c)
      

  if len(lista_especiais) >= 2:

    crit1 = True
  
  # Mais de 8 caracteres
  if len(senha) >= 8:
    crit2 = True
  
  repetidos = False
  # Não pode possuir caracteres repetidos em sequência
  for i in range(len(senha)-1):
    if senha[i+1] == senha[i]:
      repetidos = True
    
  if not repetidos:
    crit3 = True

  print("C1", crit1)
  print("C2", crit2)
  print("C3", crit3)
  
  if crit1 and crit2 and crit3:
    return True
  else:
    return False

  

print(valida_senha("!abcdef!"))