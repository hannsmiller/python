from random import randint
computador = randint(0, 10)
palpite = int(input('Tente adivinhar um número entre 0 e 10 que estou pensando: '))
totpalpites = 1
while palpite != computador:
    if palpite > computador:
        palpite = int(input('Menos... tente novamente: '))
        totpalpites += 1
    elif palpite < computador:
        palpite = int(input('Mais... tente novamente: '))
        totpalpites += 1
print('PARABÉNS! Você acertou com {} palpites.'.format(totpalpites))
