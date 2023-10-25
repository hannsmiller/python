#a confederação nacional de natação precisa de um programa que leia o ano de nascimento...
#... de um atleta e mostre sua categoria, de acordo com a idade:
#até 9 anos: MIRIN;
#até 14 anos: INFANTIL;
#até 19 anos: JÚNIOR;
#até 20 anos: SÊNIOR;
#acima: MASTER.
import datetime
from time import sleep
print('M'*35)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('W'*35)
nasc = int(input('Digite o ano de nascimento do atleta: '))
idad = datetime.date.today().year - nasc
print('PROCESSANDO...')
sleep(1)
if idad <= 9:
    print('O atleta tem {} anos e sua categoria é a \033[4mMIRIN\033[m.'.format(idad))
elif idad > 9 and idad <= 14:
    print('O atleta tem {} anos e sua categoria é a \033[4mINFANTIL\033[m.'.format(idad))
elif idad > 14 and idad < 19:
    print('O atleta tem {} anos e sua categoria é a  \033[4mJÚNIOR\033[m.'.format(idad))
elif idad > 19 and idad <= 20:
    print('O atleta tem {} anos e sua categoria é a  \033[4mSÊNIOR\033[m.'.format(idad))
else:
    print('O atleta tem {} anos e sua categoria é a  \033[1;4;7mMASTER\033[m.'.format(idad))