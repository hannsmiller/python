import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a \033[32m{}\033[m'.format(num, raiz))

#a mesma coisa só que diferente...

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a \033[32m{}\033[m'. format(num, raiz))

#para baixar novas bibliotecas, acesse o site: https://pypi.org/
