#faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
maior = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('\033[33m{}\033[m foi o menor valor digitado e \033[33m{}\033[m o maior.'.format(menor, maior))