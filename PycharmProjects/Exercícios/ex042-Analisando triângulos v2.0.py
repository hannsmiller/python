#desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário
#se elas podem formar um triângulo.
#mostre também qual tipo de triângulo será formado.
#equilátero: todos os lados iguais;
#isóceles: dois lados iguais;
#escaleno: todos os lados diferentes.

from time import sleep
print('>' * 25)
print('Analisador de Triângulo')
print('<' * 25)
print('')
a = float(input('Digite o valor do primeiro segmento: '))
b = float(input('Digite o valor do segundo segmento: '))
c = float(input('Digite o valor do terceiro segmento: '))
print('')
print('PROCESSANDO...')
sleep(1)
if a < (b+c) and b < (a+c) and c < (a+b):
    print('Esses segmentos \033[4;32mFORMAM\033[m um triângulo do tipo: ', end='')
    if a == b == c:
        print('\033[7mEQUILÁTERO!\033[m')
    elif a != b != c != a:
        print('\033[7mESCALENO!\033[m')
    else:
        print('\033[7mISÓCELES!\033[m')
else:
    print('Esses segmentos \033[4;31mNÃO FORMAM\033[m um triângulo!')
