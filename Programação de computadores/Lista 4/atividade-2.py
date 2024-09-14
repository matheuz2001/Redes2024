import requests
import os
import json
import sys
import fATV2
from datetime import datetime

strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
dictCartola = requests.get(strURL).json()
dirarquivo = os.path.abspath(__file__)
dirarquivo = os.path.dirname(dirarquivo)

Ano_Atual = datetime.now().year
while True:
    try:
        ano = input("Digite um ano para pesquisa entre 2021 para 2024: ")
        print(int(ano))
        if(int(ano) >= 2021 and int(ano) < 2024):
            x = open(dirarquivo + rf'\Arquivos\cartola_fc_{ano}.json','r', encoding='UTF-8')
            dictCartola = json.load(x)
            x.close()
            break
        elif(int(ano) > int(Ano_Atual)):
            print(f'O Ano de {ano} está no futuro!')
        elif(int(ano)==2024):
            break
        else:
            print(f'O ano de {ano} se perdeu.')

    except ValueError:
        print('Valor invalido')
    except KeyboardInterrupt:
        sys.exit('Interrompido pelo usuário')
    except:
        print(f'\\ERRO: {sys.exc_info()[0]}')

#Organização dos dados do dicionario 
jogadores = [x for x in dictCartola['atletas']]
posicoes = [dictCartola['posicoes'][i] for i in dictCartola['posicoes']]
clubes = [x for x in dictCartola['clubes']]

while True:
    try:
        print('Escolha um esquema tático:\n3-4-3;\n3-5-2;\n4-3-3;\n4-4-2;\n4-5-1;\n5-3-2;\n5-4-1:\n')
        tatica = input().split('-')
    except KeyboardInterrupt:
        sys.exit('Interrompido pelo usuário')
    except:
        print(f'\\ERRO: {sys.exc_info()[0]}')
    if not(fATV2.CheckTatica(tatica)):
        print('Tatica invalida!')
    else: 
        break

#Organizando os jogadores
jogadores = {value['atleta_id']:
            {value['atleta_id']:{'Atleta_id':value['atleta_id'],
                                 'Nome':value['nome'],
                                 'Apelido':value['apelido'],
                                 'Foto':[value['foto'] if value['foto'] != '' or None else None][0], 
                                 'Clube':dictCartola['clubes'][str(value['clube_id'])]['nome'],
                                 'Posicao':dictCartola['posicoes'][str(value['posicao_id'])]['nome'], 
                                 'Pontuacao':(value['media_num']*value['jogos_num'])}
                                } for value in jogadores}
#Organizar Fotos
for i in jogadores.keys():
    if jogadores[i][i]['Foto'] != None and jogadores[i][i]['Foto'].find('photo_Formato_'):
        jogadores[i][i]['Foto'] = jogadores[i][i]['Foto'].replace('photo_FORMATO_','photo_220x220_')
for i in jogadores.keys():
    if jogadores[i][i]['Foto'] != None and jogadores[i][i]['Foto'].find('_Formato.'):
        jogadores[i][i]['Foto'] = jogadores[i][i]['Foto'].replace('_FORMATO.','_220x220.')

#Esquemática
try:
    tatica = fATV2.Esquemas(tatica,jogadores)
except:
    print(f'\\ERROR: {sys.exc_info()[1]}')

try:
    arqentrada = open(dirarquivo + f'\\CartolaFC_{Ano}.json','w',encoding='utf-8')
    json.dump(jogadores,arqentrada,indent=6,ensure_ascii=False)
    arqentrada.close()
except:
    print(f'\\ERROR: {sys.exc_info()[0]}')

# Apresentando da tática e pontos
print('------------------------------------------')
print('Goleiro(s):')
print(' Nome:' + tatica['Tatica']['Goleiro']['Nome'])
print(' Apelido:' + tatica['Tatica']['Goleiro']['Apelido'])
print(' Time:' + tatica['Tatica']['Goleiro']['Clube'])
print(' Pontuação:' + str(tatica['Tatica']['Goleiro']['Pontuacao']) + '\n')
print('Zagueiro(s):')
for i in tatica['Tatica']['Zagueiros']:
    print(' Nome:' + i['Nome'])
    print(' Apelido:' + i['Apelido'])
    print(' Time:' + i['Clube'])
    print(' Pontuacao:' + str(i['Pontuacao']) + '\n')
print('Lateral(is):')
if tatica['Tatica']['Laterais'] != 0:
    for i in tatica['Tatica']['Laterais']:
        print(' Nome:' + i['Nome'])
        print(' Apelido:' + i['Apelido'])
        print(' Time:' + i['Clube'])
        print(' Pontuacao:' + str(i['Pontuacao']) + '\n')
else:
    print(' Não possui.\n')
print('Meia(s):')
for i in tatica['Tatica']['Meias']:
    print(' Nome:' + i['Nome'])
    print(' Apelido:' + i['Apelido'])
    print(' Time:' + i['Clube'])
    print(' Pontuacao:' + str(i['Pontuacao']) + '\n')
print('Atacante(s):')
for i in tatica['Tatica']['Atacantes']:
    print(' Nome:' + i['Nome'])
    print(' Apelido:' + i['Apelido'])
    print(' Time:' + i['Clube'])
    print(' Pontuacao:' + str(i['Pontuacao']) + '\n')
print('Tecnico(s):')
print(' Nome:' + tatica['Tatica']['Tecnico']['Nome'])
print(' Apelido:' + tatica['Tatica']['Tecnico']['Apelido'])
print(' Time:' + tatica['Tatica']['Tecnico']['Clube'])
print(' Pontuação:' + str(tatica['Tatica']['Tecnico']['Pontuacao']))
print('------------------------------------------')



