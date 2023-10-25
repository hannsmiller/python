#crie um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o ultimo nome separadamento.
#exemplo: Ana Maria de Souza.
#primeiro nome: Ana.
#último nome: Souza.

nom = str(input('Digite seu nome completo: ')).strip()
n = nom.split()
print('Seu \033[4mprimeiro\033[m nome é: {}'.format(n[0]))
print('Seu \033[4múltimo\033[m nome é: {}'.format(n[len(n)-1]))

#Exemplo Bernardo Souza Nogueira.
#O cmd split, separa o nome em 3,
#porém, a contagem começa do zero.
#sendo assim, o Nogueira fica na posição 2.
#O cmd len, mostra quantas palavras tem.
#como o nome está "splitado", len retorna 3.
#mas para achar o último nome que está na posição 2,
#deve-se subtrair 1 no comando.