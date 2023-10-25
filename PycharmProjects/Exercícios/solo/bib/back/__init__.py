from solo.bib.front import *
from random import randint
from time import sleep


def mostra_jogos(num):
    jogo = []
    c = 1
    while c <= num:
        i = 1
        while i <= 6:
            n = randint(1, 60)
            if n not in jogo:
                jogo.append(n)
                i += 1
        sleep(1)
        print(jogo)
        jogo.clear()
        c += 1
