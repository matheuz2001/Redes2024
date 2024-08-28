import os
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)

lerArquivo = open(dirArquivos + '\\CotacoesDolar2023.csv','r',encoding='utf-8')
arquivo =list()
cotaçãomedia = [['Janeiro'],['Fevereiro'],['Março'],['Abril'],['Maio'],['Junho'],['Julho'],['Agosto'],['Setembro'],['Outubro'],['Novembro'],['Dezembro']]
cotaçãomax = [['Janeiro'],['Fevereiro'],['Março'],['Abril'],['Maio'],['Junho'],['Julho'],['Agosto'],['Setembro'],['Outubro'],['Novembro'],['Dezembro']]
#Ler arquivo
while True:
    linha = lerArquivo.readline()
    if linha[-1:] == '\n':
        linha = linha[:-1]
    if not linha:
        break
    arquivo.append(linha.split(";"))

for data in range(1,13):
    aux = [arquivo[x] for x in range(len(arquivo)) if str(data) + arquivo[x][0][-4] + arquivo[x][0][-3] + arquivo[x][0][-2] + arquivo[x][0][-1] in arquivo[x][0]]
    aux.sort(key=lambda x: x[5], reverse=True)
    media = 0
    cotaçãomax[data-1].append(aux[data-1][5])
    cotaçãomax[data-1].append(aux[data-1][0])

    for x in range(len(aux)):
        media += float(aux[data-1][5].replace(',','.'))
    cotaçãomedia[data-1].append(media/len(aux))
       

for x in range(len(cotaçãomax)):
    print(cotaçãomax[x])
print('---')
for x in range(len(cotaçãomedia)):
    print(cotaçãomedia[x])
lerArquivo.close()

#Teste com 2024
lerArquivo = open(dirArquivos + '\\CotacoesDolar2024.csv','r',encoding='utf-8')
arquivo =list()
cotaçãomedia = [['Janeiro'],['Fevereiro'],['Março'],['Abril'],['Maio'],['Junho'],['Julho'],['Agosto'],['Setembro'],['Outubro'],['Novembro'],['Dezembro']]
cotaçãomax = [['Janeiro'],['Fevereiro'],['Março'],['Abril'],['Maio'],['Junho'],['Julho'],['Agosto'],['Setembro'],['Outubro'],['Novembro'],['Dezembro']]
#Ler arquivo
while True:
    linha = lerArquivo.readline()
    if linha[-1:] == '\n':
        linha = linha[:-1]
    if not linha:
        break
    arquivo.append(linha.split(";"))
    
for data in range(1,9):
    aux = [arquivo[x] for x in range(len(arquivo)) if str(data) + arquivo[x][0][-4] + arquivo[x][0][-3] + arquivo[x][0][-2] + arquivo[x][0][-1] in arquivo[x][0]]
    aux.sort(key=lambda x: x[5], reverse=True)
    media = 0
    cotaçãomax[data-1].append(aux[data-1][5])
    cotaçãomax[data-1].append(aux[data-1][0])

    for x in range(len(aux)):
        media += float(aux[data-1][5].replace(',','.'))
    cotaçãomedia[data-1].append(media/len(aux))
    
    
print('---')
for x in range(len(cotaçãomax)):
    print(cotaçãomax[x])
print('---')
for x in range(len(cotaçãomedia)):
    print(cotaçãomedia[x])
lerArquivo.close()
