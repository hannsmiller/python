#crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso...
#de zero a vinte. seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrar-lo...
#por extenso.
valores = ('zero','um','dois','três','quatro',
           'cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','catorze',
           'quinze','dezesseis','dezessete',
           'dezoito','dezenove','vinte')
resp = ''
while resp in 's':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.',end=' ')
    print(f'Você digitou {valores[num]}')
    resp = str(input('Deseja continuar? (S/N) ')).strip().lower()[0]
print('ENCERRANDO...')