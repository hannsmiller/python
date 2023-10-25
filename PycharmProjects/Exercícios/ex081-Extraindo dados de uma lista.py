#crie um programa que vai ler vários números e colocar em uma lista. depois disso mostre:
#a) quantos números foram digitados;
#b) a lista de valores ordenada de forma decrescente;
#c) se o valor 5 foi digitado e está ou não na lista.
valores = []
q = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if resp == 'n':
        break
print(f'Lista criada: {valores}')
print('=-'*30)
print(f'No total {len(valores)} valores foram digitados')
if 5 not in valores:
    print('Valor 5 não digitado')
else:
    print('Valor 5 nas posições',end='')
    for i, v in enumerate(valores):
        if v == 5:
            print(f'...{i+1}',end='')
valores.sort(reverse=True)
print('\nLista em ordem decrescente:',valores)