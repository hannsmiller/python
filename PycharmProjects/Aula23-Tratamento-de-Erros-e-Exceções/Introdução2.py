try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos problemas com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('\nO usuário preferiu não inserir todos os dados.')
else:
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte sempre, muito obrigado.')