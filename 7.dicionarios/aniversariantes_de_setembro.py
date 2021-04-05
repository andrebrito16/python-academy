def aniversariantes_de_setembro(dic):
    setembro = dict()
    for e in dic:
        if dic[e][4] == "9":
            setembro[e] = dic[e]
        
    return setembro

aniversariantes = {
    "André": "16/03/2003",
    "Ana Lívia": "27/05/2004",
    "Juvenal": "10/09/2000"
}

print(aniversariantes_de_setembro(aniversariantes))