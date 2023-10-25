#faça um programa que ajude o jogador da megasena a criar palpites...
#o programa vai perguntar quantos jogos serão gerados e vai sortear...
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('='*35)
print(f'{"MEGA-SENA":^35}')
print('='*35)
mega = []
jogo = []
quant = int(input('Número de jogos: '))
while quant > 0:
    cont = 1
    while cont <= 6:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
    jogo.sort()
    mega.append(jogo[:])
    jogo.clear()
    quant -= 1
for j, m in enumerate(mega):
    sleep(1)
    print(f'Jogo {j+1}: {m}')
sleep(1)
print('PROGRAMA FINALIZADO')
