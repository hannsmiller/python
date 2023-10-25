#PROGRAMA 1

nome = str(input('Digite seu nome: ')).upper()
if nome == 'HANNS':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print()

#PROGRAMA 2

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print()

#OUTRA MANEIRA DE FAZER:

print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')