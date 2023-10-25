# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira

#importando uma biblioteca inteira
import math
num = float(input('Digite um valor: '))
print('o valor inteiro de {} é \033[7;40m{}\033[m'.format(num, math.trunc(num)))
print()

#importando apenas uma função de uma determinada biblioteca
from math import trunc
num = float(input('Digite um valor: '))
print('o valor inteiro de {} é \033[7;40m{}\033[m'.format(num, trunc(num)))


