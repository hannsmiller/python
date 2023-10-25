#aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema...
#de visualização de detalhes de aproveitamento de cada jogador.
atleta = {}
grupo = []
gols = []
while True:
    atleta['Nome'] = str(input('Jogador: '))
    quant = int(input('Número de jogos no campeonato: '))
    for c in range(0, quant):
        gols.append(int(input(f'Número de gols no {c+1}º jogo: ')))
    atleta['gol/jogo'] = gols.copy()

    atleta['tot/gol'] = sum(gols)
    grupo.append(atleta.copy())
    gols.clear()
    atleta.clear()
    while True:
        resp = str(input('Continuar? [S/N]'))
        if resp in 'SsNn':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp in 'Nn':
        break
print('-='*25)
print(f'{"Cod":<5}{"Nome":<15}{"Gols/jogo":<15}{"Total":<5}')
print('_'*50)
for k, v in enumerate(grupo):
    print(f'{k:<5}{v["Nome"]:<15}{str(v["gol/jogo"]):<25}{v["tot/gol"]:>5}')
print('_' * 50)
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if opc == 999:
        break
    if opc >= len(grupo):
        print(f'ERRO! Não existe jogador com código {opc}')
    else:
        print('_'*35)
        print(F'    --DADOS DO JOGADOR {grupo[opc]["Nome"]}\033--    ')
        print(f'{"Cod":<5}{"Gols/jogo":<25}{"Total":>5}')
        for k, v in enumerate(grupo):
            if k == opc:
                print(f'{k:<5}{str(v["gol/jogo"]):<25}{v["tot/gol"]:>5}')
    print('_'*35)
