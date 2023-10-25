#crie um programa que leia uma frase qualquer, e diga se ela é um palíndromo.
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print('Temos um PALÍNDROMO.')
else:
    print('Não temos um PALÍNDROMO.')