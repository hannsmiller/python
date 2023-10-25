#faça um porgama que leia o peso de cinco pessoas e mostre qual é a mais pesada e a mais leve.
mais = 0
menos = 0
for c in range (1,6):
    peso = float(input('Digite o peso em (Kg) da {}º pessoa: '.format(c)))
    if c == 1:
        mais = peso
        menos = peso
    if peso > mais:
        mais = peso
    if peso < menos:
        menos = peso
print('A pessoa mais pesada tem {} Kg, \njá a menos pesada possui {} Kg.'.format(mais, menos))
