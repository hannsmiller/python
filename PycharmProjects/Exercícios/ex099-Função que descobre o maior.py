#faça um programa que tenha uma função maior(), que receba vários parâmetros com valores inteiros.
#seu programa tem que analisar todos os alores e dizer qual deles é o maior.
valores = []


def maior(*lst):
    m = 0
    print('-=' * 20)
    print('Analisando os valores...')
    for c in range(0, len(valores)):
        if valores[c] > m:
            m = valores[c]
    print(f'Ao todo foram informados {len(valores)} valores: {valores}. ')
    print(f'O maior valor informado foi {m}')
    print('-=' * 20)


while True:
    while True:
        num = int(input('[999 interrompe] Digite qualquer valor inteiro: '))
        if num == 999:
            break
        valores.append(num)
    maior()
    valores.clear()
    while True:
        resp = str(input('Continuar? [S/N]'))
        if resp not in 'SsNn':
            print('ERRO! Responda apenas S ou N. ',end='')
        else:
            break
    if resp in 'Nn':
        break
print('PROGRAMA FINALIZADO!')