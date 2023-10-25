#crie um programa que leia vários números inteiros pelo teclado. no final da execução...
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos...
#o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
totn = nmédia = 0
while resp in 'S':
    n = int(input('Digite um número: '))
    nmédia += n
    totn += 1
    if totn == 1:
        nmaior = nmenor = n
    else:
        if n > nmaior:
            nmaior = n
        elif n < nmenor:
            nmenor = n
    resp = str(input('Desaja continuar? [s/n]: ')).upper().strip()[0]
print('Você digitou {} números. A média deles é {}. O maior Valor foi {} e o menor {}'.format(totn, (nmédia/totn), nmaior, nmenor))
