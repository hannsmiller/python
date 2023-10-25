#ao invés de mandar o próprio def printar o resultado, cria-se uma variável para receber esse re3sultado. fugindo...
#assim, daquele padrão repetitivo de mostrar a ,mesma mensagem  na tela várias vezes.


def soma(a=0, b=0, c=0):
    s = a + b +c
    return s


r1 = soma(12 + 24)
r2 = soma(13 + 48 +9)
r3 = soma(4 + 3)
print(f'Os resultados foram: {r1} {r2} {r3}')
print('-='*30)


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um valor: '))
print(f'O fatorial de {n} é {fatorial(n)}')
print('-='*30)


def par(num=0):
    if num%2==0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
if par(n):
    print('É par.')
else:
    print('Não é par.')

