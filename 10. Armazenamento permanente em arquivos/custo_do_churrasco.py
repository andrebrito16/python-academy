import csv 
total = 0
with open("churras.txt") as arquivo:
  plots = csv.reader(arquivo, delimiter=",")


  for row in plots:
    total += float(row[1])*float(row[2])

print(total)

