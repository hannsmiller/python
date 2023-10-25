#código para adicionar cor aos textos: \033[style;txt,backm
#existem códigos para cada elemento dentro do código acima (style;txt;back)
#exemplo:

print('\033[1;31;40mHanns Miller')
print('\033[m')
#para ajustar a faixa de cor faça da seguinte maneira:

print('\033[7mHanns Miller\033[m')
print('\033[m')
#mais exemplos...

print('\033[1;31;40mHanns Miller\033[m')
#consultar lista de códigos no grupo estudos