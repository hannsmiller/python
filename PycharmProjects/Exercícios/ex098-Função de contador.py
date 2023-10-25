#faça um programa que tenha uma função chamada contador (), que receba três parâmetros: início,
#fim e passo e realize a contagem. seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1; b) de 10 até 0 de 2 em 2; c) uma contagem personalizada.
from time import sleep
def lin():
    print('-=' * 20)


def contador():
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p < 0:
        p = abs(p)
    elif p == 0:
        p = 1
    lin()
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.25)
    elif i > f:
        for c in range(i, f-1, - p):
            print(c, end=' ')
            sleep(0.25)
    print('FIM!')


lin()
print('Contagem de 1 até 10 de 1 em 1')
sleep(2.5)
for c in range(1,11):
    print(c, end=' ')
    sleep(0.25)
print('FIM!')
lin()
print('Contagem de 10 até 0 de 2 em 2')
sleep(2.5)
for c in range(10, -1, -2):
    print(c, end=' ')
    sleep(0.25)
print('FIM!')
lin()
print('Agora é sua vez de personalizar a contagem!')
contador()
