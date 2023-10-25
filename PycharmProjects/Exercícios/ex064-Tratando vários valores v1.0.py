#crie um programa que leia vários números inteiros pelo teclado. o programa só...
#vai parar quando o usuário digitar o valor 999, que é a condição de parada....
#no final, mostre quantos números foram digitados e qual foi a soma entre eles...
#(desconsiderando o flag)
n = int(input('Digite um número qualquer ou 999 para parar o programa: '))
totn = soman = 0
while n != 999:
    totn += 1
    soman += n
    n = int(input('Digite um número qualquer ou 999 para parar o programa: '))
print('Você digitou {} números e o somatório deles é {}'.format(totn, soman))