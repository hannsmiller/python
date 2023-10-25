#faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores M ou F...
#...caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))