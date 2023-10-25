#crie um programa que faça o computador jogar JOKENPÔ com vc.

import random
import time
print('{:=^40}'.format('JOKENPÔ'))
itens = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.randint(0,2)
print('''ESCOLHA
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
jogador = int(input('Escolha: '))
print('JO...',end=' ')
time.sleep(0.75)
print('KEN...',end=' ')
time.sleep(0.75)
print('PÔ!!!')
time.sleep(0.75)
print('-='*25)
print('Computador escolheu \033[4m{}\033[m,'.format(itens[computador]), end=' ')
if computador == 0:
    if jogador == 0:
        print('\033[7mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 2:
        print('\033[31mVOCÊ PERDEU!!!\033[m')
    else:
        print('\033[7;31mMAS A JOGADA FEITA POR VOCÊ FOI INVÁLIDA!\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[31mVOCÊ PERDEU!!!\033[m')
    elif jogador == 1:
        print('\033[7mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[32mVOCÊ VENCEU!!!\033[m')
    else:
        print('\033[7;31mMAS A JOGADA FEITA POR VOCÊ FOI INVÁLIDA!\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 1:
        print('\033[31mVOCÊ PERDEU!!!\033[m')
    elif jogador == 2:
        print('\033[7mEMPATE!\033[m')
    else:
        print('\033[7;31mMAS A JOGADA FEITA POR VOCÊ FOI INVÁLIDA!\033[m')
print('-='*25)
