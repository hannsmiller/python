#reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação...
# ...de um número de tipo inválido. aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from leiatipo import leiaint, leiafloat
i = leiaint('Número inteiro: ')
f = leiafloat('Número real: ')
print(f'Você digitou {i} como inteiro e {f} como real')