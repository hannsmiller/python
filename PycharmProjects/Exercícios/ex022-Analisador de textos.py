#crie um programa que leia o nome completo de uma pessoa e mostre:
#a) O nome com todas as letras maiúsculas;
#b) O nome com todas as minúsculas;
#c) Quantas letras ao todo sem considerar espaços;
#d) Quantas letras tem o primeio nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('a) seu nome em maiúsculas é: ', '\033[32m', nome.upper(), '\033[m')
print('b) seu nome em minúsculas é: ', '\033[31m', nome.lower(), '\033[m')
print('c) Seu nome ao todo tem \033[30;44m{}\033[m letras.'.format(len(nome) - nome.count(' ')))
print('d) seu primeiro nome tem \033[30;42m{}\033[m letras'.format(nome.find(' ')))
#outro modo de ateneder a letra d).
separa = nome.split()
print('d) seu primeiro nome é \033[4;31m{}\033[m e tem \033[30;42m{}\033[m letras.'.format(separa[0], len(separa[0])))
