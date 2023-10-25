#faça um programa utilizando while, que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5x4x3x2x1 = 120
from time import sleep
from math import factorial
nwhile = int(input('Digite um número para calculcar seu fatorial: '))
c = nwhile
print('Calculando {}! = '.format(nwhile), end='')
while c > 0:
    print((c),end='')
    print(' X ' if c > 1 else' = ', end='')
    c -= 1
print(factorial(nwhile))
sleep(2.5)
#agora utilizando for.
nfor = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}! = '.format(nfor), end='')
for c in range (nfor, 1, -1):
    print('{} X'.format(c), end=' ')
print('1 = {}'.format(factorial(nfor)))