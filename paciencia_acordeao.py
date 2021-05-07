import random
from colorama import Fore,Style

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

    def color(string):
        naipe = extrai_naipe(string)
        if naipe == '♣':
            return Fore.GREEN
        if naipe == '♦':
            return Fore.BLUE
        if naipe == '♥':
            return Fore.RED
        if naipe == '♠':
            return Fore.MAGENTA

print('Bem vindo(a) ao Paciência Acordeão')
print('\n---------------------------------')
print('\nNesse jogo você pode apenas empilhar:\nUma carta sobre a carta imediantamente anterior \nOu empilhar sobre a terceira carta anterior')
print('\nPara isso acontecer, as cartas, tanto a selecionada quanto a primeira e/ou terceira carta anterior, \nDevem ou ter o mesmo naipe ou mesmo valor!')
print('\nUm pouco complexo, mas você vai pegar o jeito.\n\n')
print('\t\tBom jogo!')

#----------------------------------------------------------------jogo-------------------------------------------------------------#

jogo = False
iniciar = False

while iniciar != True:
    print('Para iniciar jogo, digite: "Iniciar"')
    estado = input('')
    if estado == 'Iniciar':
        iniciar = True
        jogo = True

print('\nO baralho inicial está assim:\n')
baralho_inicial = cria_baralho()

while jogo:
    contador = 1
    tamanho = range(len(baralho_inicial))
    for carta in baralho_inicial:
        print(f'{contador}. {carta}')
        contador += 1
    
    contador = 1
    numero = int(input('\nEscolha uma carta entre 1 e {}: '.format(max(tamanho)+1)))
    print('')
    posicao = (numero-1)
    while posicao not in tamanho:
        numero = int(input('Carta inválida. Escolha uma carta entre 1 e {}: '.format(max(tamanho)+1)))
        print('')
        posicao = (numero-1)
    
    posicao1 = (posicao-1)
    posicao3 = (posicao-3)

    movimento = lista_movimentos_possiveis(baralho_inicial, posicao)

    if movimento == []:
        print(f'Não há movimentos possíveis para a carta {baralho_inicial[posicao]}\n')

    elif movimento == [1]:
        empilha(baralho_inicial, posicao, posicao1)

    elif movimento == [3]:
        empilha(baralho_inicial, posicao, posicao3)

    elif movimento == [1,3]:
        print(f'Quer empilhar {baralho_inicial[posicao]} sobre qual carta?')

        print(f'\n 1. {baralho_inicial[posicao1]}')

        print(f' 2. {baralho_inicial[posicao3]}')

        escolha = int(input(''))
        possibilidades = [1,2]
        while escolha not in possibilidades:
            print('Posição inválida. Escolha entre 1 ou 2: ')
            escolha = int(input(''))

        if escolha == 1:
            empilha(baralho_inicial, posicao, posicao1)
        elif escolha == 2:
            empilha(baralho_inicial, posicao, posicao3)

    verificacao = possui_movimentos_possiveis(baralho_inicial)
    if verificacao != True:
        if len(baralho_inicial) > 1:
            for carta in baralho_inicial:
                print(f'{contador}. {carta}')
                contador += 1 
            print('\nNão há mais movimentos possíveis.')
            print('Você perdeu!')
            jogo = False

        elif len(baralho_inicial) == 1:
            for carta in baralho_inicial:
                print(f'1. {carta}')
            print('\n\t\t\t\t\t\tVOCÊ EMPILHOU TODAS AS CARTAS!!!')
            print('\t\t\t\t\t\t\tVOCÊ GANHOU O JOGO!!!')
            jogo = False