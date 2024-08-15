import random as rand
from termcolor import colored
from colorama import Back, Style

with open('some_words.txt', 'r', encoding='utf-8') as arquivo:
    lista_palavras = arquivo.readlines()

palavra_secreta = rand.choice(lista_palavras).upper()
tamanho_palavra = len(palavra_secreta) - 1
palavra_user = '*' * tamanho_palavra
tentativas = 1
palavra=''


# print(palavra_secreta)
while palavra != palavra_user:

    listado_palavra_user = list(palavra_user)
    print(f'\n{tentativas}x. Palavra Secreta: {palavra_user}')

    palavra = input('Digite uma palavra de 5 letras: ').upper()
    contador = 0
    if len(palavra) >= 6 or len(palavra) <5:
        print('\nDIGITE APENAS 5 LETRAS CABEÇA DE PIKA!!!\n')
        continue

    tentativas += 1
    for i in palavra:
        if i in palavra_secreta:
            if palavra_secreta[contador] == i:
                listado_palavra_user[contador] = i
                palavra_user = ''.join(listado_palavra_user)
                print(Back.GREEN, colored(f'{i} ', 'green'), end='')
                print(Style.RESET_ALL, end='')
            else:
                print(Back.YELLOW, colored(f'{i} ', 'yellow'),end='')
                print(Style.RESET_ALL, end='')
        else:
            print(Back.WHITE, f'{i} ', end='')
            print(Style.RESET_ALL, end='')
        contador += 1

    if tentativas == 6:
        print('\nPerdeu. A Palavra era', palavra_secreta)
        break
    elif tentativas < 6:
        continue
    elif palavra == palavra_user:
        print(f'\nPARABÉNS, VOCÊ DESCOBRIU A PALAVRA SECRETA COM {tentativas} TENTATIVAS')
        break
