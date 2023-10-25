#crie um programa que mostre na tela todos os números pares entre 1 e 50.
from time import sleep
for c in range (0,51):
    if c % 2 == 0:
        print(c, end=' ')
        sleep(0.25)
print('')
#codando de uma forma mais leve para o PC
for c in range (2,51,2):
    if c % 2 == 0:
        print(c, end=' ')
        sleep(0.25)