#elabore um programa que calcule  o valor a ser pago por um produto,...
#considerando o seu preço normal e condição de pagamento:
#à vista dinheiro ou cheque: 10% de desconto;
#à vista no cartão: 5% de desconto;
#em até 2x no cartão: preço normal;
#3x ou mais no cartão: 20% de juros.

print('{:=^40}'.format('LOJAS MILLER'))
print('')
prod = float(input('Qual o valor do produto? R$ '))
print('''FORMAS DE PAGAMENTO
[1] avista ou cheque
[2] a vista no cartão
[3] 2x no cartão
[4] 3x no cartão
[5] encerrar''')
form = int(input('Qual a forma de pagamento? '))
if form == 1:
    print('Você ganhou 10% de desconto na sua compra. O valor total a ser pago é de R$ \033[32m{:.2f}\033[m'.format(prod*0.9))
elif form == 2:
    print('Você ganhou 5% de desconto na sua compra. O valor total a ser pago é de R$ \033[32m{:.2f}\033[m'.format(prod*0.95))
elif form == 3:
    print('Ok, total a ser pago: R$ {:.2f}'.format(prod))
elif form == 4:
    print('Ok, total a ser pago com o juros é de R$ \033[31m{:.2f}\033[m'.format(prod+(prod*0.2)))
elif form == 5:
    print('ENCERRANDO...')
else:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m')
