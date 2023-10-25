#faça um programa que leia um número inteiro e diga se ele é ou não primo.
tot = 0
n = int(input('Digite um valor: '))
for c in range (1, n+1):
    if n % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[32m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divido {} vezes, por isso ele'.format(n,tot), end=' ')
if tot > 2:
    print('NÃO É PRIMO')
else:
    print('É PRIMO')
