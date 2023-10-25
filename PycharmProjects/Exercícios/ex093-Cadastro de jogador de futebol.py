#crie um programa que gerencie o aproveitamento de um jogador de futebol, o programa vai ler...
#o nome do jogador e quantas partidas ele jogou. depois vai ler a quantidade de gols feitos em...
#cada partida. no final tudo isso será guardado em um dicionário, incluindo o total de gols feito...
#durante o campeonato.
atleta = {}
atleta['Jogador'] = str(input('Nome do jogador: '))
quant = int(input(f'Número de jogos de {atleta["Jogador"]} no campeonato: '))
gols = []
for c in range(0, quant):
    gols.append(int(input(f'  Quantos gols no {c+1}º jogo? ')))
print('-='*30)
atleta['gols'] = gols.copy()
atleta['total'] = sum(gols)
print(atleta)
print('-='*30)
for k, v in atleta.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {atleta["Jogador"]} jogou {quant} partidas.')
for c in range(0, quant):
    print(f'  => Na partida nº {c+1}, fez {atleta["gols"][c]} gols.')
print(f'Foi um total de {atleta["total"]} gols.')