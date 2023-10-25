#crie um programa que leie o nome e o preço de vários produtos. o programa deverá...
#...perguntar se o usuário quer continuar. no final mostre:
#a) qual o total gasto na compra
#b) quantos produtos custam mais de R$1000,00
#c) qual é o nome do produto mais barato
total = totmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Produto: '))
    preço = float(input('Valor: R$ '))
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    if preço > 1000:
        totmil += 1
    total += preço
    resp = ' '
    while resp not in 's/n':
        resp = str(input('Continuar [S/N]? ')).strip().lower()[0]
    if resp in 'n':
        break
print('{:-^50}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Dos produtos cadastrados, {totmil} custam mais que R$ 1000,00')
print(f'O produto mais barato foi {barato}, custando R$ {menor}')
