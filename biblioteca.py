def gera_nome_do_convite(convite):
    parte1 = convite[0:4]
    parte2 = convite[len(convite)-4:]
    return parte1 + ' ' + parte2
