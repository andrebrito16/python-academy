

def lista_em_zigue_zague(lista):
  zigue_zague = True

  padrao_menor_maior = False
  padrao_maior_menor = False

  if len(lista) == 0 or len(lista) == 1:
    return zigue_zague
  
  if len(lista) == 2 and (lista[0] != lista[1]):
    return zigue_zague
  
  if len(lista) >= 3:
    if lista[1] < lista[0]:
      padrao_menor_maior = True
    else:
      padrao_maior_menor = True

  if not padrao_maior_menor and not padrao_menor_maior:
    zigue_zague = False
    return zigue_zague
  
  for i in range(1, len(lista) - 1, 2):
    if padrao_menor_maior:
      if lista[i + 1] < lista[i] or lista[i + 1] == lista[i]:
        zigue_zague = False
        return zigue_zague
    
    if padrao_maior_menor:
      if lista[i + 1] > lista[i] or lista[i + 1] == lista[i]:
        zigue_zague = False
        return zigue_zague
    
  return zigue_zague

print(lista_em_zigue_zague([2, 1, 5, 2, 3, 1]))