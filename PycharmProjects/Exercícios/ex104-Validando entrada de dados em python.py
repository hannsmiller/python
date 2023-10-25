#crie um programa que tenha uma função cahamda leiaint() do python, só que fazendo...
#avaliação para aceitar apenas valores numéricos.
#EX: n = leiaint('Digite um n')
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input('Digite um número inteiro: '))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um valor válido!\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {n}')