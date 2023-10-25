#crie um programa que leia uma frase e mostre:
#quantas vezes aparece a letra  'A'.
#em que posição ela aparece a primeira vez.
#em que posição ela aparece a última vez.7

fra = str(input('Digite uma frase: ')).strip().upper()
print('A letra \033[4;31m"A"\033[m ocorre {} vezes.'.format(fra.count('A')))
print('A primeira letra \033[4;31m"A"\033[m apareceu na posição {}'.format(fra.find('A') + 1))
print('A última ocorrência da letra "A" foi na posição {} '.format(fra.rfind('A') + 1))