def atualiza_telefone(numero):
  # Verificar se tem traço

  if numero.find("-") == -1 and len(str(numero)) == 8:
    return f"9{numero}"
  elif numero.find("-") != -1 and len(str(numero)) == 9:
    return f"9{numero}"
  else:
    return numero


print(atualiza_telefone("99999999"))