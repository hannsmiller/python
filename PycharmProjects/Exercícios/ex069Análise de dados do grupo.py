#crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada,...
#... o programa deverá perguntar ao usuário se ele quer continuar. no final mostre:
#a) quantas pessoas tem mais de 18 anos
#b) quantos homens foram cadastrados
#c) quantas mulheres tem menos de 20 anos
maior = homens = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    print('='*20)
    if idade > 18:
        maior += 1
    if sexo in 'm':
        homens += 1
    if idade < 20 and sexo in 'f':
        mulher += 1
    if continuar in 'n':
        break
print(f'{maior} pessoas são maiores de 18 anos.')
print(f'{homens} são homens.')
print(f'{mulher} são mulheres com menos de 20 anos.')