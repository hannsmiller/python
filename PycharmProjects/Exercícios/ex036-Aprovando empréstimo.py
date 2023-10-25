#escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. o programa vai perguntar...
#... o valor da casa, o salário do comprador, e em quantos anos ele vai pagar. Calcule o valor da prestação...
#... mensal, sabendo que ela não pode exceder 30 % do salário ou então o empréstimo será negado.

from time import sleep
print('=-'*25)
print('SIMULADOR DE CRÉDITO')
print('=-'*25)
casa = float(input('Bem vindo ao simulador de crédito! Para começarmos, informe o valor da casa: R$ '))
print('PROCESSANDO...')
sleep(1)
salario = float(input('Muito bem, agora informe a sua renda mensal: R$ '))
print('PROCESSANDO...')
sleep(1)
parcelas = int(input('Ótimo. Agora para finalizar, em quantos anos pretende pagar? '))
print('OK, AGUARDE ENQUANTO PROCESSAMOS AS INFORMAÇÕES...')
sleep(1)
trinta = salario * 0.3
mensalidade = casa / (parcelas * 12)
print('O valor da mensalidade será de R$ \033[7m{:.2f}\033[m.'.format(mensalidade), end='')
print(' O valor mínimo que você pode pagar é R$ ',trinta)
if mensalidade <= trinta:
    print('Parabéns! Sua solicitação foi \033[32mAPROVADA!\033[m')
else:
    print('Infelizmente sua solicitação foi \033[31mREPROVADA.\033[m')
