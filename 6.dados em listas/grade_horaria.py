

def compromisso_no_periodo(grade, dia, periodo):
    if grade[periodo][dia] == '':
        return 'Livre'
    else:
        return grade[periodo][dia]



grade = [
    ['GDE',     'Tópicos', 'NatDes',  'Tópicos',   ''         ],
    ['DesSoft', 'GDE',     'DesSoft', 'InstruMed', 'NatDes'   ],
    ['ModSim',  '',        '',        '',          ''         ],
    ['',        'ModSim',  '',        'ModSim',    'InstruMed']
]

print(compromisso_no_periodo(grade, 2, 1))