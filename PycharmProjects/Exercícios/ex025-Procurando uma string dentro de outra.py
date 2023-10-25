#crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nom = str(input('Digite seu nome completo: ')).strip()
print('O nome digitado tem "Silva"? {}'.format('silva' in nom.lower()))