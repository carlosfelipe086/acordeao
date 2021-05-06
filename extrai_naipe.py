def extrai_naipe(carta):
    if len(carta) > 2:
        return carta[2]
    if len(carta) == 2:
        return carta[1]
