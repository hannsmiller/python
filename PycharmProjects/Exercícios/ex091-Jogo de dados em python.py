#crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#guarde esses resultados em um dicionário. no final coloque esse dicionário em ordem,
#sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
rank = []
for k, v in jogo.items():
    print(f'{k} tirou: {v}')
    sleep(0.75)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('_' * 30)
print(f'{"ranking dos jogadores":^30}')
print('_' * 30)
for i, v in enumerate(rank):
    print(f'{i + 1}ª lugar: {v[0]} com {v[1]}')

