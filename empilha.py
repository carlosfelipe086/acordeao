def extrai_valor(string):
    return string[:-1:] 

def extrai_naipe(string):
    return string[-1]

def empilha(lista,origem,destino):
    destino_naipe = extrai_naipe(lista[destino])
    destino_valor = extrai_valor(lista[destino])

    origem_naipe = extrai_naipe(lista[origem])
    origem_valor = extrai_valor(lista[origem])

    if origem_naipe == destino_naipe:
        lista[destino] = lista[origem]
        del lista[origem]
        return lista

    elif origem_valor == destino_valor:
        lista[destino] = lista[origem]
        del lista[origem]
        return lista