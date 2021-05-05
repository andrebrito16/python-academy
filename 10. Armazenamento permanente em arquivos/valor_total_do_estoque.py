import json
with open("estoque.json", "r") as arquivo:
  arquivo = arquivo.read()

dic = json.loads(arquivo)
total = 0

for v in dic.values():
  for item in v:
    total += item['quantidade']*item['valor']

print(total)