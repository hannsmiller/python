#faça um programa que tenha uma função cahamada ficha(), que receba dois parâmetros opcionais:
#o nome de um jogador e quantos gols ele marcou. o programa deverá ser capaz de mostrar...
#a ficha do jogador mesmo que algum dado não tenha sido informado corretamente.
def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gols no campeonato.')


n = str(input('Jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
