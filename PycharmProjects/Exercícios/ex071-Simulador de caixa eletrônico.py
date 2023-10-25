#crie um programa que simule o funcionamento de um caixa eletrônico. no início, pergunte...
#... ao usuário qual será o valor sacado (valor inteiro) e o programa vai informar...
#...quantas cédulas de cada valor serão entregues.
#obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*30)
print('{:^30}'.format('BANCO PYTHON'))
print('='*30)
saque = int(input('Valor a sacar: R$ '))
valor = saque
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'>>> Foram {totced} cédulas de R$ {ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if valor == 0:
            break
