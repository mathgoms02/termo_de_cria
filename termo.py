import random as rand
from termcolor import colored
from colorama import Back

with open('aula47.txt', 'r', encoding='utf-8') as arquivo:
    lista_palavras = arquivo.readlines()

palavra_secreta = rand.choice(lista_palavras).upper()
tamanho_palavra = len(palavra_secreta) - 1
palavra_user = '*' * tamanho_palavra
tentativas = 0
palavra=''

while palavra != palavra_user:
    if tentativas == 5:
        break
    tentativas += 1
    listado_palavra_user = list(palavra_user)
    print(f'\n{tentativas}x. Palavra Secreta: {palavra_user}')

    palavra = input('Digite uma palavra de 5 letras: ')
    contador = 0

    for i in palavra:
        if i in palavra_secreta:
            if palavra_secreta[contador] == i:
                listado_palavra_user[contador] = i
                palavra_user = ''.join(listado_palavra_user)
                print(Back.GREEN, colored(f'{i} ', 'green'), end='')
            else:

                print(Back.YELLOW, colored(f'{i} ', 'yellow'),end='')
        else:
            print(Back.WHITE, f'{i} ', end='')
        contador += 1

if tentativas == 5:
    print('\nPerdeu otário. A Palavra era', palavra_secreta)
else:
    print(f'\nPARABÉNS, VOCÊ DESCOBRIU A PALAVRA SECRETA COM {tentativas} TENTATIVAS')