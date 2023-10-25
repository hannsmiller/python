#crie um programa que leia nome, idade e sexo de várias pessoas. guardando os dados de cada...
# pessoa em um dicionário e todos os dicionários em uma lista. no final mostre:
#a) quantas pessoas foram cadastradas.
#b) a média de idade do grupo.
#c) uma lista com todas as mulheres.
#d) uma lista com todas as pessoas com idade acima da média.
from operator import itemgetter
dados = []
cad = {}
somaidade = 0
mulheres = []
while True:
    cad['Nome'] = str(input('Nome: '))
    cad['Idade'] = int(input('Idade: '))
    somaidade += cad['Idade']
    while True:
        cad['Sexo'] = str(input('Sexo: [M/F]')).strip().lower()[0]
        if cad['Sexo'] in 'MmFf':
            break
        print('ERRO! Responda apenas M ou F.')
    if cad['Sexo'] in 'Ff':
        mulheres.append(cad['Nome'])
    dados.append(cad.copy())
    while True:
        resp = str(input('Continuar? [S/N]'))
        if resp in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'Nn':
        break
mediaidade = somaidade/len(dados)
print('-='*30)
print(f'  - No total foram cadastradas {len(dados)} pessoas.')
print(f'  - A média de idade do grupo é de {mediaidade:.2f} anos.')
print(f'  - As mulheres cadastradas foram: {mulheres}')
acimadaidade = []
for p in dados:
    if p['Idade'] > mediaidade:
        acimadaidade.append(p['Nome'])
print(f'  - As pessoas com idade acima da média são: {acimadaidade}')
