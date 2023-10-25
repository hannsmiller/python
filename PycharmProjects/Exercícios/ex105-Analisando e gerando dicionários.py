#faça um programa que tenha uma função notas() que pode receber várias notas...
#de alunos e vai retornar um dicionário com as seguintes informações:
#-quantidade de notas;
#-a maior nota;
#-a menor nota;
#-a méida da turma;
#-a situação (opcional)
#adicione també as doctrings da função


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param show: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dic = {}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n)/len(n)
    if sit:
        if dic['média'] <= 6:
            dic['situação'] = 'RUIM'
        elif 6 < dic['média'] <= 7:
            dic['situação'] = 'REGULAR'
        else:
            dic['situação'] = 'BOA'
    return dic


resp = notas(7, 9, 6, 7, sit=True)
print(resp)
print('-='*100)
help(notas)
