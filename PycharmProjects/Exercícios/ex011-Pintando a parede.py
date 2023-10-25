#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de...
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input('Digite a largura de sua parede em metros: '))
h = float(input('Digite a altura de sua parede em metros: '))
a = l * h
r = a / 2
print('-='*25)
print(f'''Sua parede de {l:.2f}m X {h:.2f}m,
tem uma área total de {a:.2f}m².
Indicamos no mínimo {r} L de tinta, 
para uma cobertura de qualidade.''')