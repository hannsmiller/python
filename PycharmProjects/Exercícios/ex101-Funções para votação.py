#crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de...
#nascimento de uma pessoa. retornando um valor literal indicando se uma pessoa tem voto NEGADO,
#OPCIONAL OU OBRIGATÓRIO nas eleições.
def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos, NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é OPCIONAL.'
    else:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO.'


print('_'*35)
ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))
