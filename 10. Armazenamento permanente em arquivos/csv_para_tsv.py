import csv 

with open("dados.csv", "r") as arquivocsv, open("dados.tsv", "w") as arquivotsv:
  arquivocsv = csv.reader(arquivocsv)

  arquivotsv = csv.writer(arquivotsv, delimiter='\t')

  for row in arquivocsv:
    arquivotsv.writerow(row)