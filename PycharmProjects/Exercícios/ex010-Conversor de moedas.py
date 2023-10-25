#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input('Quanto você tem? R$ '))
d = r / 4.91
print(f"""Convertendo Real em Dólar...
R${r:.2f} = US${d:.2f}""")