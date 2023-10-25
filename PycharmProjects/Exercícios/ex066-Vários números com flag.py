#crie um programa que leia vários números inteiros pelo teclado. o programa só...
#vai parar quando o usuário digitar o valor 999, que é a condição de parada...
#no final, mostre quantos números foram digitados e qual foi a soma entre eles.
#(desconsiderando o flag).
totn = soman = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    totn += 1
    soman += n
print(f'Você digitou {totn} números e o somatório deles é {soman}')