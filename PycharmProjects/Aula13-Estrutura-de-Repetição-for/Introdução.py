for c in range(1,5):
    print('Oi')
print('Fim')
print('')
#para ter uma contagem até 5, deve-se começar do zero, pois o python ignora o último número.
for c in range (0,5):
    print('Oi')
print('Fim')
print('')
#regressiva.
for c in range(5,0,-1):
    print(c)
print('Fim')
print('')
#para dar saltos na contagem.
for c in range (0,12,2):
    print(c)
print('Fim')
print('')
#mais complexo.
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('Fim')
print('')
#somando.
s = 0
for c in range (0,3):
    n = int(input('Digite um valor: '))
    s = s + n
    #ou
    #s += n
print('A soma dos valores é', s)
print('Fim')