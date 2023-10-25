#crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um...
# ... arquivo de texto simples. o sistema só vai ter 2 opções: cadastrar uma nova pessoa e...
# ... listar todas as pessoas cadastradas.
from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'CursoEmVídeo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        lerarquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Encerrando o sistema...')
        break
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
