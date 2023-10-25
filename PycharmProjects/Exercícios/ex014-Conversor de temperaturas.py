#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Digite a temperatura em °C: '))
f = (c * 1.8) + 32
print('-=' * 25)
print(f'''Convertendo °C para °F...
{c}°C equivale a {f:.2f}°F.''')