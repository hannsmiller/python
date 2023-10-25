#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos números separados.
#exemplo: número 1834.
# unidades: 4, dezenas: 3, centenas: 8, milhar: 1.

num = int(input('Digite um valor até 4 dígitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[1;36munidades:\033[m {}'.format(u))
print('\033[1;35mdezena:\033[m {}'.format(d))
print('\033[1;34mcentena: \033[m{}'.format(c))
print('\033[1;32mmilhar:\033[m {}'.format(m))
#existe um jeito mais fácil usando estrutura de repetição, mas ainda não chegamos nessa parte da aula.
