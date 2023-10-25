#crie um programa que leia vários números e colocar em uma lsita. depois disso, crie...
#duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados...
#ao final, mostre o conteúdo das 3 listas geradas.
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Continuar? [S/N]')).strip().lower()[0]
    if resp in 'n':
        break
for c in range (0,len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print('_'*30)
print(f'Valores digitados: {lista}')
print(f'Valores pares: {par}')
print(f'Valores ímpares: {impar}')