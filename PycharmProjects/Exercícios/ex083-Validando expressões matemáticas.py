#crie um programa onde o usuário digite uma expressão qualquer que use parênteses...
#seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos...
#e fechados na ordem correta.
exp = str(input('Digite a expressão: '))
aberto = []
fechado = []
for simb in exp:
    if simb == '(':
        aberto.append('(')
    elif simb == ')':
        fechado.append(')')
if len(aberto) == len(fechado):
    print('\033[32mExpressão válida!\033[m')
else:
    print('\033[31mExpressão inválida!\033[m')
