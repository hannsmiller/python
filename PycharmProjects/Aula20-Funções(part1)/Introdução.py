#uma "def" deve manter a distância de duas linhas vazias do programa principal, como mostrra abaixo.
def lin():
    print('_'*30)


#programa principal
lin()
print(f'{"CURSO EM VÍDEO":^30}')
lin()

#pode-se criar uma "def" para incluir uma mensagem, como abaixo.
def tit(txt):
    print('_'*30)
    print(txt)
    print('_'*30)


tit(f'{"CURSO EM VÍDEO":^30}')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 3)


#quando não se sabe o tamanho do parãmetro que vai para a "def", usa-se o "*"., como abaixo.
def cont(*num):
    for valor in num:
        print(f'{valor} ',end='')
    print('FIM.')


cont(0, 1, 5, 4)
cont(10, 88)
cont(0)


def cont2(*n):
    tam = len(n)
    print(f'Recebi os valores {n} e são ao todo {tam} números.')


cont2(2, 1, 7)
cont2(8, 0,)
cont2(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def som(*val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}')


som(5, 2)
som(2, 9, 4)