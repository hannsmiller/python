#crie um programa que leie o nome, ano de nascimento e carteira de trabalho de uma pessoa...
#e cadastre-os(com idade) em um dicionário. se por acaso o ctps for diferente de zero...
#o dicionário receberá também o ano de contratação e o salário. calcule e acrescente...
#além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = {'nome': str(input('Nome: ')),
            'nascimento': int(input('Ano de nascimento: ')),
            'ctps': int(input('CTPS: [0 interrompe]'))}
cadastro['idade'] = datetime.now().year - cadastro['nascimento']
if cadastro['ctps'] == 0:
    print('-='*30)
    for k, v in cadastro.items():
        print(f'  -{k} = {v}')
else:
    cadastro['contrato'] = int(input('Ano da contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = cadastro['contrato'] - cadastro['nascimento'] + 35
    print('-='*30)
    for k, v in cadastro.items():
        print(f'  -{k} = {v}')