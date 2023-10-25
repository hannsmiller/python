#comando break
totn = soman = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    totn += 1
    soman += n
#print('Você digitou {} e o somatório de todos é {}'.format(totn, soman))
print(f'Você digitou {totn} e o somatório de todos é {soman}')
#Bônus
nome = 'José'
idade = 33
salário = 987.30
from time import sleep
sleep(2.5)
print('')
print(f'{nome} tem {idade} anos e recebe R$ {salário} por mês')
sleep(2.5)
print(f'{nome:-^20} tem {idade} anos e recebe R$ {salário:.2f} por mês')
sleep(2.5)
print(f'{nome:~>20} tem {idade} anos e recebe R$ {salário} por mês')
sleep(2.5)
print(f'{nome:=<20} tem {idade} anos e recebe R$ {salário} por mês')
