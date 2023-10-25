#crie uma tabuada com estrutura de repetição
n = int(input('Digite um valor para mostrarmos sua tabuada: '))
for c in range (1,11):
    print('{} X {} = {}'.format(n, c, n*c))
