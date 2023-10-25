from ex113.leiatipo import leiaint


def linha(tam=42):
    return '_' * tam


def cabeçalho(txt):
    print(linha())
    print(f'{txt.center(42)}')
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for i, v in enumerate(lista):
        print(f'\033[33m{i+1}\033[m - \033[34m{v}\033[m')
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc
