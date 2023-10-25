#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
v = float(input('Digite um valor em metros: '))
cem = v * 100
mim = v * 1000
print(f'{v} metros equivale a {cem} centímetros ou {mim} milímetros.')