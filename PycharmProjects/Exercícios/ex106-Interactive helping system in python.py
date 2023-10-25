#faça um minisistema que utilize o interactive help do python. o usuáio vai digitar um comando...
#e o manual vai aparecer. quando o usuário digitar a palavra FIM o programa encerrará. use cores.
from time import sleep


def manual(msg):
    print(f'\033[1;7m',end='')
    help(msg)
    print('\033[m', end='')


def busca(msg):
    print('\033[1;44m~' * (31 + len(msg) + 4))
    print(f"  Acessando o manual do comando '{msg}'")
    print('~' * (31 + len(msg) + 4))
    print('\033[m',end='')
    sleep(2)
    manual(msg)


while True:
    sleep(1)
    print('\033[1;42m~' * 25)
    print(' SISTEMA DE AJUDA PyHELP ')
    print('~' * 25)
    comando = str(input('\033[mFunção ou Biblioteca > ')).strip().lower()
    if comando == 'fim':
        print('\033[1;41m~' * 11)
        print(' ATÉ LOGO! ')
        print('~' * 11)
        break
    busca(comando)
