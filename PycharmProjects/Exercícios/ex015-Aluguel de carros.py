#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de...
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15...
# por Km rodado.
km = float(input('KM rodado: '))
d = int(input('Dias alugado: '))
p = (km * 0.15) + (d * 60)
print(f'Nas condições informadas, o valor do aluguel ficou R${p:.2f}')