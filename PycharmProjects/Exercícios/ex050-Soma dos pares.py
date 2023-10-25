#desenvolva um programa que leia 6 números inteiros e mostre a soma apenas...
#daqueles que forem pares, se o valor digitado for ímpar, desconsidere-o.
s = 0
q = 0
for c in range (1,7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n
        q += 1
print('Você digitou {} valor(es) par(es) e a soma dele(s) é: \033[4;7m{}\033[m.'.format(q, s))
