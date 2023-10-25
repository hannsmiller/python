#refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os...
#... 10 primeiros termos da progressão usando a estrutura while.
from time import sleep
início = int(input('Digite o primeiro termo de uma PA: '))
razão = int(input('Digite a razão da PA: '))
c = 1
pa = início
print(início,'- ', end='')
while c < 10:
    pa += razão
    print('{} -'.format(pa), end=' ')
    c += 1
print('ACABOU!')
sleep(2.5)

#agora com for
início = int(input('Digite o primeiro termo de uma PA: '))
razão = int(input('Digite a razão da PA: '))
pa = início
print(início,'- ', end='')
for c in range (1, 10):
    pa += razão
    print('{} -'.format(pa), end=' ')
    c += 1
print('ACABOU!')
