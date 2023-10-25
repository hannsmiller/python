#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#depois disso, mostre a listagem de números gerados e também indique...
#o menor e o maior valor que estão na tupla.
from random import randint
valores = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for n in valores:
    print(n,end=' ')
print(f'\nMaior valor: {max(valores)}')
print(f'Menor valor: {min(valores)}')