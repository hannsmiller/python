#desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo...
#com a tabela abaixo:
#abaixo de 18.5: Abaixo do peso;
#entre 18.5 e 25: Peso ideal;
#acima de 25 até 30: Sobrepeso;
#acima de 30 até 40: obsesidade;
#acima de 40: Obesidade mórbida.

print('o'*25)
print('  CALCULADORA DE IMC')
print('o'*25)
print('')
altura = float(input('Digite a sua altura em m: '))
peso = float(input('Digite o seu peso em kg: '))
imc = peso / altura**2
print('Seu IMC é \033[7m{:.2f}\033[m, e você está na classificação de '.format(imc),end='')
if imc < 18.5:
    print('\033[31mABAIXO DO PESO.\033[m')
elif 18.5 <= imc <= 25:
    print('\033[32mPESO IDEAL.\033[m')
elif 25 < imc <= 30:
    print('\033[33mSOBREPESO.\033[m')
elif 30 < imc <= 40:
    print('\033[31mOBESIDADE.\033[m')
elif imc > 40:
    print('\033[31;40mOBSIDADE MÓRBIDA.\033[m')