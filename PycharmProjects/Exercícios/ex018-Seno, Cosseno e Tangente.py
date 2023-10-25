#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.

import math

an = float(input('Informe o ângulo: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print('O ângulo informado foi \033[30;41m{}\033[m'.format(an))
print('Seu seno é de \033[36m{:.2F}\033[m'.format(se))
print('Seu cosseno é de \033[36m{:.2F}\033[m '.format(co))
print('Sua tangente é de \033[36m{:.2F}\033[m'.format(ta))

#necessita usar o comando "radians" para converser Radianos para Graus Centigrados".