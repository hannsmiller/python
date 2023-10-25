#Fatiamnto de string
frase = 'Hanns Miller'
print('a)',frase[9])
print('b)',frase[2:5])
print('c)',frase[2:10:2])
print('d)',frase[:7])
print('e)',frase[7:])
print('f)',frase[9::3])
print('g)',len(frase))
print('h)',frase.count('a'))
print('i)',frase.count('n',0,12))
print('j)',frase.find('ll'))
print('k)',frase.find('poly'))
print('l)','Miller' in frase)

#Transformação da string
print('m)',frase.replace('Nogueira', 'Dias'))
print('n)',frase.upper())
print('o)',frase.lower())
print('p)',frase.capitalize())
print('q)',frase.title())
txt = '    Hanns Miller  '
print('r)',txt)
print('s)',txt.strip())

#Divisão de string
print('t)',frase.split())

#Junção
print('u)','-'.join(frase))

#Três áspas """txt"""
print()
print("""Sou um animal, sentimental, me apego facilmente
ao que desterta o meu desejo...
Tente me obirgar a fazer o que não quero e "c"
vai logo ver, o que acontece....""")