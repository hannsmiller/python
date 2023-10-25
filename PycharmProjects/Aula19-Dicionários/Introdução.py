pessoas = {'Nome': 'Hanns', 'Sexo': 'Masculino', 'Idade': 34}
print(pessoas)
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='*50)
for k in pessoas.keys():
    print(k)
print(' ')
for v in pessoas.values():
    print(v)
print(' ')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(' ')
del pessoas['Sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(' ')
pessoas['Peso'] = 103
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(' ')
pessoas["Nome"] = 'Bê'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*50)
brasil = []
estado1 = {'Uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'Uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['Uf'])
print(brasil[1]['Sigla'])
print('-='*50)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['Uf'] = str(input('Estado: '))
    estado['Sigla'] = str(input('Sigla: ' ))
    brasil.append(estado.copy())
print(brasil)
print(' ')

for e in brasil:
    print(e)
print(' ')

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print(' ')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print(' ')
print('-='*50)
#Para ordenar um dicionário, utilize o comando "itemgetter" da biblioteca "operator".
#ex: key=itemgetter(?)
#Ex: rank = sorted(jogo.items(), key=itemgetter(1)) Ex091