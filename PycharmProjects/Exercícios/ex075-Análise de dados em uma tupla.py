#desenvolva um programa que leia quatros valores pelo teclado e guarde-os em uma tupla.
#no final mostre:
#a) quantas vezes apareceu o valor 9;
#b) em que posição foi digitado o primeiro valor 3;
#c)quais foram os números pares.
grupo = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o último valor: ')))
print(f'O 9 apareceu {grupo.count(9)} vezes')
if 3 in grupo:
    print(f'O 3 aparece primeiro na {grupo.index(3)+1}ª posição')
else:
    print(f'O 3 não apareceu')
print('Valores pares: ',end='')
for n in grupo:
    if n % 2 == 0:
        print(n,end=' ')

