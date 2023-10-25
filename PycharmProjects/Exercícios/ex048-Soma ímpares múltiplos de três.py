#faça um programa que calcule a soma de todos os números ímpares que são...
#múltiplos de 3 entre 1 e 500.
s = 0
q = 0
for c in range (1,501, 2):
    if c % 3 == 0:
        s += c
        q += 1
print('Existem {} números ímpares e múltiplos de três entre 1 e 500. E {} é o somatório de todos eles'.format(q,s))