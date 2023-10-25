#faça um programa que mostre a tabuada de vários números, um de cada vez, para cada...
#... valor digitado pelo usuário. o programa será interrompido quando o número...
#solicitado for negativo.
from time import sleep
print('_'*20)
print('GERADOR DE TABUADA')
print('_'*20)
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} X {c} = {n * c}')
    print('=-'*10)
    sleep(1)
print('FIM.')