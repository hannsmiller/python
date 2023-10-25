#crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#no final, mostre um boletim contendo a média de cada um e permita que o usuário...
#possa mostrar as notas de cada aluno individualmente.
boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    med = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], med])
    resp = str(input('Continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=-'*20)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>6}')
print('_'*20)
for a, b in enumerate(boletim):
    print(f'{a:<4}{boletim[a][0]:<10}{boletim[a][2]:>6.2f}')
print('_'*20)
while True:
    opc = int(input('Ver nota do aluno Nº: [?]  (999 interrompe)'))
    if 0 <= opc <= len(boletim)-1:
        print(f'As notas de {boletim[opc][0]} foram: {boletim[opc][1]}')
    if opc == 999:
        print('PROGRAMA FINALIZADO')
        break
