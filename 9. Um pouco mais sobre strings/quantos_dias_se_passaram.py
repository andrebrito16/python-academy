def dias_do_ano(data):
  dia = int(data[:2])
  mes = int(data[3:5])
  ind_mes = mes-1

  ano = data[6:]

  meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  # Calcular os dias até o mês anterior
  
  if mes == 1:
    return dia -1


  total = 0
  for c in range(0, ind_mes):
    total += meses[c]

  return total + dia - 1


print(dias_do_ano("02/03/2018"))