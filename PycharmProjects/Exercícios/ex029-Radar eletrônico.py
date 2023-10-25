#escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#a multa vai custar R$ 7,00 por cada km acima do limite.

vel = float(input('Digite a velocidade registrada: '))
if vel > 80:
    print('Você foi \033[1;31mMULTADO!\033[m')
    mul = (vel - 80) * 7
    print('O valor da sua multa é de: R$ \033[1;31m{:.2f}\033[m'.format(mul))
print('Tenha um bom dia, dirija com segurança.')