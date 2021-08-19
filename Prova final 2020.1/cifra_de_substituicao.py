# String codificada e dicionário de trocas
def decodifica(codificada, trocas):
  # Preciso trocar o valor pela chave
  decodificada = []

  for c in codificada:
    encontrei = False
    for k, v in trocas.items():
      if v == c:
        decodificada.append(k)
        encontrei = True
        break
    if not encontrei:
      decodificada.append(c)

    

  return ''.join(decodificada)

trocas = {'a': '*', 'e': '&'}
string = '*b*c*t&'
print(decodifica(string, trocas))