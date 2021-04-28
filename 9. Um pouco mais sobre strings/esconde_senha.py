def esconde_senha(senha):
    hided_password = list()

    for c in senha:
        hided_password.append("*")

  

    return "".join(hided_password)
