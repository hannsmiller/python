#faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
#a primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai...
#mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import  sleep


def sorteio():
    print('Sorteando valores...')
    for c in range(0, 5):
        numeros.append(randint(0, 9))
    for i, v in enumerate(numeros):
        sleep(0.5)
        print(v,end=' ')


def somaPar():
    pares = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            pares += v
    sleep(0.5)
    print(f'\nSomando os valores pares temos: {pares}')


numeros = []
sorteio()
somaPar()
