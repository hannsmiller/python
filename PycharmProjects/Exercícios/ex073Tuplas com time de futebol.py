#crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da tabela do CAMPEONATO BRASILEIRO DE FUTEBOL...
#... na ordem de colocação. depois mostre:
#a) apenas os 5 PRIMEIROS colocados;
#b) os ÚLTIMOS 4 colocados da tabela;
#c) uma lista com os times em ORDEM ALFABÉTICA;
#d) em que posição na tabela está o time da chapecoense.
tabela = ('Botafogo','Palmeiras','Fluminense','Atlético-MG','Cruzeiro',
          'Flamengo','Athletico-PR','São Paulo','Santos','Grêmio',
          'Fortaleza','Bragantino','Bahia','Cuiabá','Internacional',
          'Goiás','Vasco da Gama','Corinthias','América-MG','Chapecoense')
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print(f'{sorted(tabela)}')
if 'Chapecoense' in tabela:
    print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')
else:
    print('A Chapecoense não está entre os 20 classificados')