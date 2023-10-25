#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
n = int(input('Digite um número: '))
dob = n * 2
tri = n * 3
rq = sqrt(n)
print(f'''O número digitado foi {n}.
Seu dobro é {dob};
Seu triplo é {tri};
E sua raiz quadrada é {rq}''')