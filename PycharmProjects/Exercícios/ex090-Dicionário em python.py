#faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#no final mostre o conteúdo da estrtura na tela.
boletim = {}
boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input(f'Média do aluno {boletim["Nome"]}: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
elif 5 <= boletim['Média'] < 7:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Reprovado'
for k, v in boletim.items():
    print(f'  - {k} é igual a {v}')