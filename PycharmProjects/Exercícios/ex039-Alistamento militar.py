#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar;
# se é a hora de se alistar;
# se já passou da hora do alistamento.
# o programa deve mostrar também o tempo que falta ou que passou do prazo.

import datetime
print('#'*25)
print('EXÉRCITO BRASILEIRO')
print('#'*25)
print('')
ano = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - ano
falta = 18 - idade
passou = idade - 18
alistamento = ano + 18
if idade < 18:
    print('Você está com {} anos, falta {} anos para o seu alistamento que ocorrerá em {}.'.format(idade, falta, alistamento))
elif idade == 18:
    print('Você está com {} anos, está na hora do seu alistamento.'.format(idade))
else:
    print('Você está com {} anos, Já passou da hora do seu alistamento que deveria ter sido feito em {}, você está {} anos atrasado.'.format(idade, alistamento, passou))