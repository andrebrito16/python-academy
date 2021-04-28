def conserta_teclado(palavra):
  if len(palavra) == 0:
    return palavra
  palavra_consertada = [palavra[0].lower()]
  
  
  for c in range(0, len(palavra)):
    if palavra_consertada[-1] != palavra[c].lower():
      palavra_consertada.append(palavra[c].lower())
  return "".join(palavra_consertada)

print(conserta_teclado(""))
