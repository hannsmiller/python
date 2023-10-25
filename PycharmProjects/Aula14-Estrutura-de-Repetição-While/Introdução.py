#exemplo de programa usando WHILE
n = 1
print('A qualquer momento que desejar sair, é só digitar 0')
while n != 0:
    n = int(input('Digite um valor: '))
print('ACABOU')
#quantos pares e impares
n = 1
par = impar = 0
print('A qualquer momento que desejar sair, é só digitar 0')
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Dos valores digitados, {} é(são) par(es) e {} é(são) ímpar(es).'.format(par, impar))