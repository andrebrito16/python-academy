def quando_passa(grade, titulo):
  saida = {}

  for k, v in grade.items():
    for horario, t in v.items():
      if t == titulo:
        if horario in saida:
          prev_list = saida[horario]
          prev_list.append(k)
          saida[horario] = prev_list
        else:
          saida[horario] = [k]
  
  return saida
