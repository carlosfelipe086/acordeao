import random

def cria_baralho():
    lista = ['K♠', 'Q♠', 'J♠', '10♠',
    '9♠', '8♠', '7♠', '6♠', 
    '5♠', '4♠', '3♠', '2♠', 
    'A♠', 'K♥', 'Q♥', 'J♥', 
    '10♥', '9♥', '8♥', '7♥',
    '6♥', '5♥', '4♥', '3♥', 
    '2♥', 'A♥', 'K♦', 'Q♦', 
    'J♦', '10♦', '9♦', '8♦',
    '7♦', '6♦', '5♦', '4♦', 
    '3♦', '2♦', 'A♦', 'K♣', 
    'Q♣', 'J♣', '10♣', '9♣',
    '8♣', '7♣', '6♣', '5♣', 
    '4♣', '3♣', '2♣', 'A♣']

    random.shuffle(lista)
    return lista
    
def extrai_valor(string):
    return string[:-1:] 

def extrai_naipe(string):
    return string[-1]

def lista_movimentos_possiveis(lista,indice):
    tamanho = range(len(lista))
    posicao1 = (indice-1)
    posicao3 = (indice-3)
    lista_movimento = []
    
    if posicao1 in tamanho:
        posicao1_naipe = extrai_naipe(lista[posicao1])
        posicao1_valor = extrai_valor(lista[posicao1])

        if posicao1_naipe == extrai_naipe(lista[indice]) or posicao1_valor == extrai_valor(lista[indice]):
            lista_movimento.append(1)

    if posicao3 in tamanho:
        posicao3_naipe = extrai_naipe(lista[posicao3])
        posicao3_valor = extrai_valor(lista[posicao3])

        if posicao3_naipe == extrai_naipe(lista[indice]) or posicao3_valor == extrai_valor(lista[indice]):
            lista_movimento.append(3)

    return lista_movimento

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

def possui_movimentos_possiveis(lista):
    movimentos = 0
    contador = 0 
    for contador in range(len(lista)):
        indicador = lista_movimentos_possiveis(lista,contador)
        if len(indicador) > 0:
            movimentos += 1

    if movimentos > 0:
        return True
    else:
        return False

print('Bem vindo(a) ao Paciência Acordeão')
print('\n---------------------------------')
print('\nNesse jogo você pode apenas empilhar:\nUma carta sobre a carta imediantamente anterior \nOu empilhar sobre a terceira carta anterior')
print('\nPara isso acontecer, as cartas, tanto a selecionada quanto a primeira e/ou terceira carta anterior, \nDevem ou ter o mesmo naipe ou mesmo valor!')
print('\nUm pouco complexo, mas você vai pegar o jeito.\n\n')
print('\t\tBom jogo!')

print('O baralho inicial está assim:')
baralho_inicial = cria_baralho()
contador = 1
for carta in baralho_inicial:
    print('{}. {}'.format(contador, carta))
    contador += 1