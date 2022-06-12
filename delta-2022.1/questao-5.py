# def numero_digitos(string):
#   numero_digitos = 0
#   for i in range(len(string)):
#     if string[i].isdigit():
#       numero_digitos += 1
  
#   return numero_digitos

# Agora do jeito difícil
def numero_digitos(string):
  NUMBERS = '0123456789'
  numero_digitos = 0
  for i in range(len(string)):
    if string[i] in NUMBERS:
      numero_digitos += 1
  return numero_digitos

numero_digitos("senha123")