import requests
import sys
import statistics
import os
import json
from datetime import datetime

strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURL += '/Moedas?$top=100&$format=json'
dictMoedas = requests.get(strURL).json()
while True:
    try:
        ano = int(input('Qual o ano da cotação? '))
        if(ano > datetime.now().year):
            print(f'O ano colocado é de um ano futuro')
        else:
            break
    except ValueError:
        print(f'\\ERRO: {sys.exc_info()[0]}')
        print(f'Não é um número inteiro')
dictSimbolos = list(map(lambda x : x['simbolo'], dictMoedas['value']))
print(f'Escolha uma das seguintes moedas:')
for x in dictSimbolos:
    print(f'{x} ', end='')
print(': ')
moeda = input("")
moeda = moeda.upper()
moedas = list(filter(lambda x : x['simbolo'] == moeda, dictMoedas['value']))
if (len(moedas) <= 0):
    sys.exit('moeda inexistente')

strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += f'@moeda=%27{moeda}%27&@dataInicial=%2701-01-{ano}%27&'
strURL += f'@dataFinalCotacao=%2712-31-{ano}%27&$format=json'
dictCotacoes = requests.get(strURL).json()

meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']




cotacoes = list(map(lambda x:[x['cotacaoCompra'],x['cotacaoVenda'],datetime.strptime(x['dataHoraCotacao'],"%Y-%m-%d %H:%M:%S.%f")],dictCotacoes['value']))
medias = {value: {'MediaCompra':round(statistics.mean([x[0] if x[2].month == mes else 0 for x in cotacoes]),5),'MediaVenda':round(statistics.mean([x[1] if x[2].month==mes else 0 for x in cotacoes ]),5)}for value,mes in zip(meses,range(1,13))}

dirarquivo = os.path.abspath(__file__)
dirarquivo = os.path.dirname(dirarquivo)
arqSaida =open(dirarquivo + f'\\medias_cotacoes_{moeda}_{ano}.json','w', encoding='utf-8') #Write
json.dump(medias,arqSaida,indent=6,ensure_ascii=False)
arqSaida.close()
arqSaida =open(dirarquivo + f'\\medias_cotacoes_{moeda}_{ano}.csv','w', encoding='utf-8') #Write
arqSaida.write(f"moeda;mes;MediaCompra;MediaVenda;\n")
for x in medias.keys():
    arqSaida.write(f'{moeda};{x};{medias[x]["MediaCompra"]};{medias[x]["MediaVenda"]}\n')