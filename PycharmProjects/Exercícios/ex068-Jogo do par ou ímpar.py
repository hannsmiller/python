#faça um programa que jogue par ou ímpar com o computador. o jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from time import sleep
from random import randint
vitórias = 0
print('='*15)
print('PAR OU ÍMPAR')
print('='*15)
while True:
    escolha = ' '
    while escolha not in 'pi':
        escolha = str(input('Você quer par ou ímpar [P/I]? ')).strip().lower()[0]
    computador = randint (0,5)
    jogador = int(input('Quantos dedos[0...5]? '))
    total = computador + jogador
    print('-'*15)
    print(f'Computador: {computador}')
    print(f'Jogador: {jogador}')
    if escolha == 'p':
        if total % 2 == 0:
            print(f'{computador} + {jogador} = {total} que é PAR!\n\033[32mVOCÊ VENCEU!\033[m')
            vitórias += 1
        else:
            print(f'{computador} + {jogador} = {total} que é ÍMPAR!\n\033[31mCOMPUTADOR VENCEU!\033[m')
            break
    elif escolha == 'i':
        if total % 2 == 1:
            print(f'{computador} + {jogador} = {total} que é ÍMPAR!\n\033[32mVOCÊ VENCEU!\033[m')
            vitórias += 1
        else:
            print(f'{computador} + {jogador} = {total} que é PAR!\n\033[31mCOMPUTADOR VENCEU!\033[m')
            break
    print('='*20)
print(f'Você obteve {vitórias} vitórias sobre o computador')
