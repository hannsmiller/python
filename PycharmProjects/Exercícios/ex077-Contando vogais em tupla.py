#crie um programa que tenha uma tupla com várias palavras (não usar acentos)...
#depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Deus','familia','amor','saude','prosperidade','bençao',
            'vitoria','dialogo','conquistas','paz','compreensao',
            'felicidade','satisfaçao','realizaçoes','viagens', 'parceiria')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
