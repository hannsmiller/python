#faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
#no final, mostre:
#a) quantas pessoas foram cadastradas.
#b) uma listagem com as pessoas mais pesadas.
#c) uma listagem com as pessoas mais leves.
pessoas = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'No total, {len(pessoas)} pessoas foram cadastradas.')
pesado = leve = 0
nomepesado = ''
for i, p in enumerate(pessoas):
    if p[1] > pesado:
        pesado = p[1]
        nomepesado = p[0]
print(f'O mais pesado foi [{nomepesado}] pesando {pesado:.2f} kg.')
nomeleve = ''
for i, p in enumerate(pessoas):
    if i == 0:
        leve = p[1]
    if p[1] < leve:
        leve = p[1]
        nomeleve = p[0]
print(f'O mais leve foi [{nomeleve}] pesando {leve:.2f} kg.')