lanche = ['hamburguer','suco','pizza','picole']
print(lanche)
lanche.append('coockie')
print(lanche)
lanche.insert(0,'hot-dog')
print(lanche)
del lanche[3]
print(lanche)
#para remover o último use:
lanche.pop()
print(lanche)
#para remover por valor use:
lanche.remove('suco')
print(lanche)
print('.'*100)
valores = list(range(4,11))
print(valores)
valores = [8,7,4,3,1,9,4,9,4,5,7,8]
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
print('.'*100)
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print('.'*100)
valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
print('.'*100)
#para criar uma cópia de uma lista, siga o exemplo a seguir:
#a = [2,3,4,7]
#b = a[:]
#se colocar apenas b = a, cria-se uma ligação entre a listas e n uma cópia...
#daí tudo que altera em um altera na outra.
