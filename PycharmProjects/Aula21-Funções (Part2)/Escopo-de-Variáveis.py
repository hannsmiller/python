#variável criada dentro de uma "def" só funciona dentro dela, já a criada fora funciona dentro. Ex:


def teste():
    a = 5
    b = 3
    print(f'A dentro vale: {a}')
    print(f'B dentro vale: {b}')


a = 1
teste()
print(f'A fora vale: {a}')
print('-=' * 30)
#no exemplo acima pode-se fazer a variável "a" ser modificada dentro da função utilizando o comando "global". Ex:


def testel():
    global x
    x = 5
    b = 3
    print(f'A dentro vale: {x}')
    print(f'B dentro vale: {b}')


x = 1
testel()
print(f'A fora vale: {x}')
