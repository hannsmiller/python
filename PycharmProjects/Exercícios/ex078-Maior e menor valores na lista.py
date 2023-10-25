#faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e sas suas respecitvas posições na lista.
lista = []
for c in range (0,5):
    lista.append(int(input('Digite um valor: ')))
print('_'*20)
print(f'Você digitou {lista}')
mai = max(lista)
men = min(lista)
print(f'Maior valor digitado foi {mai}, nas posições',end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'...{i+1}',end='')
print(f'\nMenor valor digitado foi {men}, nas posições',end='')
for i, v in enumerate(lista):
    if v == men:
        print(f'...{i+1}',end='')