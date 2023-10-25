#escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros...
#... elementos de uma sequeência de Fibonacci.
#Ex: 0►1►1►2►3►5►8
elementos = int(input('Quantos elementos da sequência de Fibonacci deseja exibir? '))
a = 0
b = 1
print('{} > {}'.format(a, b),end='')
while elementos > 2:
    c = a + b
    print(' > {}'.format(c),end='')
    a = b
    b = c
    elementos -= 1
print(' > FIM')

