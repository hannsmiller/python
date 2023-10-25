#crie um programa que leia nome, idade e sexo de 4 pessoas, no final do programa mostre:
#a média de idade do grupo;
#o nome do homem mais velho;
#quantas mulheres tem menos de 21 anos.
from datetime import date
anoatual = date.today().year
mediaidade = 0
homemvelho = ''
contidade = 0
contmulher21 = 0
for c in range (1,5):
    print('-'*10,c,'º Pessoa','-'*10)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).lower().strip()
    if idade > contidade and sexo == 'm':
        contidade = idade
        homemvelho = nome
    if idade < 21 and sexo == 'f':
        contmulher21 += 1
    mediaidade += idade
print('A média de idade do grupo é {}.'.format(mediaidade/4))
print('{} é o homem mais velho.'.format(homemvelho.upper()))
print('Existem {} mulheres com idade abaixo de 21 anos.'.format(contmulher21))


