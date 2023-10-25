#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Salário atual: R$'))
ns = s * 1.15
print(f'Novo salário R${ns:.2f}')