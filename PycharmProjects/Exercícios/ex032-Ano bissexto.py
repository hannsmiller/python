#faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Que ano deseja analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[1;32mBISSEXTO\033[m.'.format(ano))
else:
    print('O ano {} não é \033[1;31mBISSEXTO\033[m.'.format(ano))