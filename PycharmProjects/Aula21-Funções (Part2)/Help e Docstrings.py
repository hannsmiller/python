#o comando help exibe o manual de outro comando específico dentro do python.
#ele pode ser usado dentro do console python tbm digitando "help()" ou como o exemplo a seguir.
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)