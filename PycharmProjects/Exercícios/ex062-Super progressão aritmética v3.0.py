#melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#o programa encerra quando ele disser que quer mostrar 0 termos.
from time import sleep
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termos = int(input('Digite a quantidade de termos a exibir: '))
pa = primeiro
print(primeiro, end='')
mais = 1
tottermos = termos
while mais != 0:
    while termos != 0 and termos > 1:
        pa += razão
        print(' {}'.format(pa), end=' ')
        termos -= 1
    print('- PAUSA.')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    termos = mais + 1
    tottermos += mais
for c in range (1,4):
    print('.',end='')
    sleep(0.5)
print('')
print('Progressão finalizada com {} termos mostrados'.format(tottermos))
