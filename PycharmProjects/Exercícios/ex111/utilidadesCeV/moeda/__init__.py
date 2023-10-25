#ex107-Exercitando módulos em python
def aumentar(n=0, taxa=0, formato=False):
    """
    -> Aumenta o valor em x porcento.
    :param n: valor a ser aumentado
    :param taxa: valor da porcentagem a ser aplicada
    :param formato: formatação monetária (opcional)
    :return: valor de n acrescido com a porcentagem
    """
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(n=0, taxa=0, formato=False):
    """
    -> Diminui o valor em x porcento.
    :param n: valor a ser diminuido
    :param taxa: valor da porcentagem a ser aplicada
    :param formato: formatação monetário (opcional)
    :return: valor de n diminuido com a porcentagem
    """
    res = n - (n * taxa/100)
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    """
    -> Dobra o valor.
    :param n: Valor a ser dobrado
    :param formato: formatação monetária (opcional)
    :return: o dobro do valor de n
    """
    res = n * 2
    return res if formato is False else moeda(res)


def metade(n=0, formato=False):
    """
    -> Divide o valor pela metade.
    :param n: Valor a ser dividido
    :param formato: formatação monetária (opcional)
    :return: metade do valor de n
    """
    res = n / 2
    return res if formato is False else moeda(res)


def moeda(n=0, moeda='R$'):
    """
    -> Formata o valor para o padrão monetário.
    :param n: valor a ser formatado
    :param moeda: moeda a ser aplicada, por padrão é R$
    :return: valor formatado no padrão monetário
    """
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(n=0, aumento=0, redução=0):
    """
    -> Faz um resumo do valor digitado, aplicando todos os
    métodos do módulo moeda (dobro, metade, aumentar e diminuir).
    :param n: valor a ser submetido
    :param aumento: porcentagem a ser acrescida em n
    :param redução: porcentagem a ser reduzida em n
    :return: resultado das aplicações de n nos métodos, em uma tabela organizada.
    """
    print('_'*30)
    print('RESUMO DO VALOR'.center(30))
    print('_'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'O dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(n, aumento, True)}')
    print(f'{redução}% de desconto: \t{diminuir(n, redução, True)}')
    print('_'*30)
