def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mPrograma interrompido pelo usuário.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mPrograma interrompido pelo usuário.\033[m')
            return 0
        else:
            return n