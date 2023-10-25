from solo.bib.back import *


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def gerador_de_jogos(q):
    cabecalho('GERANDO JOGOS...')
    mostra_jogos(q)
