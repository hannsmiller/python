#desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética...
#no final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = primeiro + (10 - 1) * razão
#o comando acima é uma fórmula matemática.
for c in range (primeiro, décimo, razão):
    print('{}'.format(c), end=' → ')
print('ACABOU.')

