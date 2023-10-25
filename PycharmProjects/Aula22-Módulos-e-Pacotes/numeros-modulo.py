
#O python sugere que ao importar um módulo que criamos, é bom evitar o "from...", pois se houver outras bibliotecas...
#...com os mesmos comandos, ex: sleep, p python pode gerar uma confusão quando for escolher qual usar.
#... Na prática ele vai utilizar o último que tiver sido importado, mas para evitar, usa-se o import no lugar do from.
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}')

#vantagens de se usar o módulo:
# - organização do código;
# - facilidade de manutenção;
# - ocultação de código detalhado;
# - reutilização em outros projetos, copiando o arquivo do módulo e colando na pasta do novo projeto.
