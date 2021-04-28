def login_disponivel(login, usuarios):
  
  for l in usuarios:
   
    
    if login == l[:-1] and l[-1].isnumeric():
      numero = int(l[-1]) + 1
      return f"{login}{numero}"
    

  if login in usuarios:
    return f"{login}1"

  return login


print(login_disponivel('luciop', ['andrek', 'fabio', 'luciop', "luciopk"]))
