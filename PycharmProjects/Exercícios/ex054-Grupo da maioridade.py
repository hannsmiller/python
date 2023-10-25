#crie um programa que leia o ano de nascimento de 7 pessoas. no final, mostre quantas...
#pessoas ainda não atingiram a maioridade e quantas já atingiram.
from datetime import date
maior = 0
menor = 0
for c in range (1,8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if date.today().year - ano > 18:
        maior += 1
    else:
        menor += 1
print('Das 7 pessoas cadastradas, {} já são de maiores e {} ainda são menores'.format(maior, menor))
