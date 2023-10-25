#crie um programa que leie duas notas de um aluno e calcule sua média, mostrando uma mensagem...
#... no final, de acordo com a média atingida.
# média abaixo de 5.0: REPROVADO;
# média entre 5.0 e 6.9: RECUPERAÇÃO;
# média 7.0 ou superior: APROVADO.

print('~'*25)
print('CALCULADORA DE MÉDIA')
print('~'*25)
print('')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m < 5:
    print('\033[31mREPROVADO!\033[m')
elif m >= 5 and m <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('\033[32mAPROVADO!\033[m')