#crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma...
#lista. caso o número já exista lá dentro, ele não seerá adicionado. no final, serão exibidos todos...
#valores únicos digitados em ordem crescente.
lista = []
resp = ''
while resp in 's':
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não adicionado...')
    resp = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
print(sorted(lista))