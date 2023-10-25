#def soma(a, b, c):
#    s = a + b + c
#    print(f'a soma dos valores é {s}')


#soma(3, 2, 5)

# e se fosse passado menos valores para a def? resolva isso com o seguinte modelo


def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Hanns Miller.
    """
    s = a + b + c
    print(f'Somando os valores... {s}')


soma(3, 2, 9)
soma(5, 1)
soma(8)
soma()
soma(b=4, c=2)
soma(c=2, b=7)
print('-='*20)
help(soma)