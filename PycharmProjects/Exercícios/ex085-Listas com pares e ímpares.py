#crie um programa onde o usuário pode digitar 7 valores numéricos e caadstre-os em uma lista única..
#...que mantenha separados os valores pares e ímpares. no final mostre os pares e ímpares..
#ordem crescente.
valores = [[],[]]
for c in range (0,7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(f'Valores pares digitados: {sorted(valores[0])}')
print(f'Valores ímpares digitados: {sorted(valores[1])}')
