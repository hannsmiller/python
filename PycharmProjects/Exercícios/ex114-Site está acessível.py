#crie um código que CursoEmVídeo.txt se o site Pudim está acessível pelo computador usado.
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mSite está off-line!\033[m')
#ou...
# ...except: urllib.error.URLError:...
# ...print('Erro')
else:
    print('\033[32mSite está on-line!\033[m')
#Extra: Se quiser mostrar na tela o código do site, faça:...
# ...print(site.read())