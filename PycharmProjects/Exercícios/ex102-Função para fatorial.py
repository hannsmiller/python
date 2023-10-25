#crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que...
#indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)...
#indicando se será mostrado ou não na tela o processo de cálculo fatorial.
def fatorial(fact, show=False):
    f = 1
    for c in range(fact, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ',end='')
        f *= c
    return f


print(fatorial(4, True))
