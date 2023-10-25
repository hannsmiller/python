#tupla
lanche = ('Hambúrguer','Suco','Pizza','Pudim','Batata frita')
print(lanche)
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[:-2])
print(len(lanche))
#tuplas são imnutáveis

for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi demais.')
print(' ')
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print(' ')
for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(' ')
print(sorted(lanche))
print(lanche)
print(' ')
a = (2,5,4)
b = (5,8,1,2)
c = b + a
# a ordem influencia, se fosse a + b seria diferente
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(5,1))
pessoa = ('Hanns', 34, 'M', 103.5)
print(pessoa)
del (pessoa)
print(pessoa)
