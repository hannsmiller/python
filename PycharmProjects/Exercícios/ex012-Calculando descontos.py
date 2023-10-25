#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço do produto: R$ '))
d = p * 0.95
print(f'Um produto no valor de R${p:.2f}, com o desconto de 5% sai por R${d:.2f}')