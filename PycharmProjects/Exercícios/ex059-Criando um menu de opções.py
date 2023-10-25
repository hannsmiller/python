#crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
from time import sleep
opção = 0
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
while opção != 5:
    print('''-----MENU-----
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    opção = int(input('>>>>> Escolha uma das opções acima: '))
    if opção == 1:
        print('\033[7mA soma dos dois valores é {}\033[m'.format(valor1+valor2))
    elif opção == 2:
        print('\033[7mO produto dos dois valores é {}\033[m'.format(valor1*valor2))
    elif opção == 3:
        if valor1 > valor2:
            print('\033[7mO valor maior é {}\033[m'.format(valor1))
        elif valor1 == valor2:
            print('\033[7mOs valores são iguais\033[m')
        else:
            print('\033[7mO valor maior é {}\033[m'.format(valor2))
    elif opção == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('\033[7mENCERRANDO...\033[m')
    else:
        print('\033[31mOPÇÃO INVÁLIDA.\033[m')
    print('=-'*20)
    sleep(2.5)