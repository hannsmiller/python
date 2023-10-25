#escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#ppara inferiores ou iguais o aumento é de 15%.

sal = float(input('Digite o valor do seu salário: R$ '))
if sal > 1250:
    sal = sal + (sal * 0.1)
    print('Seu novo salário será R$','\033[1;32m', sal, '\033[m')
else:
    sal = sal + (sal *0.15)
    print('Seu novo salário será R$','\033[1;32m', sal, '\033[m')