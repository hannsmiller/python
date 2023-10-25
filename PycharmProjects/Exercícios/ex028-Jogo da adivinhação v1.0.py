#escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#o programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

num = randint(1,3)
print('-=-' * 20)
print('Estou pensando em um número de 1 a 3...')
print('-=-' * 20)
adv = int(input('Em qual número estou pensando? '))
print('PROCESSANDO...')
sleep(1)
if adv == num:
    print('Parabéns, você acertou! Eu pensei em ','\033[7m', num, '\033[m')
else:
    print('Hum... não foi dessa vez. Eu pensei em ','\033[7m', num, '\033[m')