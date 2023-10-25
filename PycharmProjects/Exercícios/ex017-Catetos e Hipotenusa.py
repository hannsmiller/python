#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa.

from math import hypot
ce = float(input('Comprimento do cateto menor em cm: '))
ca = float(input('Comprimento do cateto maior em cm: '))
hi = hypot(ce, ca)
print('O comprimento da hipotenusa é: \033[31;40m{:.2f}\033[m cm'.format(hi))
