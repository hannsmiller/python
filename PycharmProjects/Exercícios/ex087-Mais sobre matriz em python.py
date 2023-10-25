#aprimore o desafio anterior, mostrando no final:
#a) soma de todos os valores pares digitados.
#b) a soma dos valores da terceira coluna.
#c) o maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = ter = seg = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = (int(input(f'Digite um valor para [{i},{c}]: ')))
        if matriz[i][c] % 2 == 0:
            pares += matriz[i][c]
print('=-'*15)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]',end=' ')
    print()
print('=-'*15)
for i in range(0, 3):
    ter += matriz[i][2]
    if matriz[1][i] > seg:
        seg = matriz[1][i]
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {ter}')
print(f'O maior valor da segunda linha é: {seg}')
