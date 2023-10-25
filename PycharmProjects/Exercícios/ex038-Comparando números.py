#escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#o primeiro valor é maior;
#o segundo valor é maior;
#não existe valor maior, os dois são iguais.

print('>'*25)
print('COMPARADOR DE NÚMEROS')
print('>'*25)
v1 = int(input('Digite um valor inteiro: '))
v2 = int(input('Digite outro valor inteiro: '))
if v1 > v2:
    print('O primeiro valor é o maior')
elif v2 > v1:
    print('O segundo valor é o maior')
else:
    print('Ambos os valores são iguais')
