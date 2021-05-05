def extrai_valor(string):
    return string[:-1:] 

def extrai_naipe(string):
    return string[-1]

def lista_movimentos_possiveis(baralho,indice):
    tamanho  = range(len(baralho))
    posicao1 = (indice-1)
    posicao3 = (indice-3)
    lista = []
    
    if posicao1 in tamanho:
        posicao1_naipe = extrai_naipe(baralho[posicao1])
        posicao1_valor = extrai_valor(baralho[posicao1])

        if posicao1_naipe == extrai_naipe(baralho[indice]) or posicao1_valor == extrai_valor(baralho[indice]):
            lista.append(1)


    if posicao3 in tamanho:
        posicao3_naipe = extrai_naipe(baralho[posicao3])
        posicao3_valor = extrai_valor(baralho[posicao3])

        if posicao3_naipe == extrai_naipe(baralho[indice]) or posicao3_valor == extrai_valor(baralho[indice]):
            lista.append(3)

    return lista