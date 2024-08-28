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
pings = list()
for x in caminho:
    if(len(x)>6):
        pings.append([x[0],x[1],x[3],x[5],x[7]])
        #print(x)
        #print(x[0],x[1],x[3],x[5],x[7])
#pings.sort(key=lambda x: x[1],reverse=True)
pings.sort(key=lambda x: x[1])
print(pings)
for x in pings:
    if x[4] == 'limite':
        pings.pop(0)
print(pings)
for x in pings:
    salvarArquivo.write(f'{x}\n')
salvarArquivo.close()
