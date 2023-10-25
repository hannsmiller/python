#desenvolva um programa que pergunte a distância de uma viagem em km.
#calcule o preço da passagem, cobrando R$ 0,50 / km por viagens até 200 km.
#e R$ 0,45 por km para viagens mais longas.

via = float(input('Digite a distância (em km) da sua viagem: '))
if via <= 200:
    val = via * 0.5
else:
    val = via * 0.45
print('O valor da sua viagem será R$ \033[32m{:.2f}\033[m'.format(val))