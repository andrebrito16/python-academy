def contabiliza_combustivel(dic):
  combustiveis_usados = []
  combustiveis_contabilizados = dict()

  for v in dic.values():
    if v['tipo'] not in combustiveis_usados:
      combustiveis_usados.append(v['tipo'])

  for combustivel in combustiveis_usados:
    total_litros = 0
    custo_total = 0
    # queremos total_litros/custo total

    for k1, v1 in dic.items():
      if v1['tipo'] == combustivel:
        total_litros += v1['litros']
        custo_total += v1['custo']
    
    combustiveis_contabilizados[combustivel] = {
      'total litros': total_litros,
      'custo por litro': custo_total/total_litros
    }

  return combustiveis_contabilizados

  

entrada = {
    'dia 1': {
        'tipo': 'Etanol',
        'litros': 20,
        'custo': 50.0
    },
    'dia 4': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 150.5
    },
    'dia 10': {
        'tipo': 'Gasolina',
        'litros': 15,
        'custo': 49.5
    },
    'dia 14': {
        'tipo': 'Etanol',
        'litros': 30,
        'custo': 70.0
    }
}

print(contabiliza_combustivel(entrada))








