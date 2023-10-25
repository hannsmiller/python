#crie um progra que tenha uma tupla única com nomes de produtos e seus...
#respectivos preços na sequência. no final, mostre uma listagem de preços...
#organizando os dados em forma de tabular.
print('_'*62)
print(f'{"TABELA DE PREÇOS":^62}')
print('_'*62)
tabela = ('Camisa de malha', 39.90,
          'Bermuda de linho', 69,
          'Calça jeans', 89,
          'Meias lupo pct c/ 5', 18.90,
          'Cueca zorba pct c/ 3',25.90,
          'Jaqueta jeans', 290,
          'toca de lã', 15.90,
          'Boné NY', 89.90,
          'Relógio tecnus', 229,
          'Mochila', 129)
for item in range (0, len(tabela)):
    if item % 2 == 0:
        print(f'{tabela[item]:.<50}',end='')
    else:
        print(f'R${tabela[item]:>10.2f}')
print('_'*62)



