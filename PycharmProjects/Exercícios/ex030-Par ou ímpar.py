#crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O valor digitado é par.')
else:
    print('O valor digitado é ímpar.')