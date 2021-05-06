def extrai_valor (carta):
    if len(carta) < 3:
        return carta[0]
    if len(carta) > 2:
        return carta[0]+carta[1]