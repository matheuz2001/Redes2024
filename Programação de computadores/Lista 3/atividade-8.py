import subprocess
import os
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)
salvarArquivo = open(dirArquivos + '\\rastreio.txt','w',encoding='utf-8')
destino = input("Coloque um site para fazer o teste de conexão: ")
strCMD = 'tracert -d4 ' + destino
caminho = subprocess.run (strCMD, capture_output=True).stdout.decode('latin1')
caminho = caminho.split('\r\n')
caminho = [i.split() for i in caminho]
for x in caminho:
    print(x)
salvarArquivo.write(caminho)
salvarArquivo.close()
'''
lerArquivo = open(dirArquivos + '\\rastreio.txt','r',encoding='utf-8')
saltos = [i.split('\r\n') for i in lerArquivo]
print(saltos)
'''
#'\r\n'