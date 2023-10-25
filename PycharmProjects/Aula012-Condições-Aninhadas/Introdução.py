nome = str(input('Digite seu nome: ')).lower()
if nome == 'hanns':
    print('Uau, que nome bonito!')
elif nome == 'lalleska':
    print('Esse é novo, sua mãe inventou?')
else:
    print('Hum... seu nome não tem nada demais...')
print('Prazer em te conhecer \033[31m{}\033[m!'.format(nome))