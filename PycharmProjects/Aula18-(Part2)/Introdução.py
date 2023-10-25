dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
pessoas = list()
pessoas.append(dados[:])
pessoas = [['Pedro',25],['Maria',19],['João',32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
print('_'*50)
teste = []
teste.append('Hanns')
teste.append(34)
galera = []
galera.append(teste[:])
teste[0] = 'Poly'
teste[1] = 36
galera.append(teste[:])
teste[0] = 'Bernardo'
teste[1] = 13
galera.append(teste[:])
print(galera)
print('_'*50)
povo = []
inf = []
totmai = totmen = 0
for c in range (0,3):
    inf.append(str(input('Nome: ')))
    inf.append(int(input('Idade: ')))
    povo.append(inf[:])
    inf.clear()
print(povo)

for p in povo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maior de idade e {totmen} menor de idade')