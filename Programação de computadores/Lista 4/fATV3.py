import random
import os
import sys

def QCartelas(quantia: int):
    if not isinstance(quantia, int):
        return(False,"Informe um valor inteiro")
    elif (quantia <= 0):
        return(False,"Informe um valor maior que 0")
    dictCartelas = {}
    while quantia > 0:
        n = str(random.randint(0,100000))
        n = (6-len(n))* "0" + n
        if (n not in dictCartelas):
            cartela = {"CART_" + n:{'B':sorted(random.sample(range(1,15),5)),
                          'I':sorted(random.sample(range(16,30),5)),
                          'N':sorted(random.sample(range(31,45),5)),
                          'G':sorted(random.sample(range(46,60),5)),
                          'O':sorted(random.sample(range(61,75),5))}}
            duplicada = 0
            for x in dictCartelas:
                if(dictCartelas[x] == cartela):
                    duplicada +=1
            if duplicada < 1:
                dictCartelas.update(cartela)
                quantia -= 1
    return(True,dictCartelas)



def SCartelas(Cartelas: dict):
    if not isinstance(Cartelas, dict) or len(Cartelas)<1:
        raise Exception('Não é um dicionário ou o dicionário é pequeno demais...')
    dirArquivos = os.path.abspath(__file__)
    dirArquivos = os.path.dirname(dirArquivos)
    Salvarcartelas = open(dirArquivos + '\\cartelas.txt','w', encoding='utf-8')
    for x in Cartelas:
        Salvarcartelas.write(f"{x};B;{Cartelas[x]['B']};I;{Cartelas[x]['I']};N;{Cartelas[x]['N']};G;{Cartelas[x]['G']};O;{Cartelas[x]['O']};\n")
    return(True,"Arquivo salvo com sucesso!")



def LerCartelas():
    dirArquivos = os.path.abspath(__file__)
    dirArquivos = os.path.dirname(dirArquivos)
    try:
        LerCartela = open(dirArquivos + '\\cartelas.txt','r', encoding='utf-8')

    except ValueError:
        print('Arquivo inexistente...')
        return(False)
    
    dicionario = {}
    while True:
        linha = LerCartela.readline()
        if linha[-1:] == '\n': linha = linha[:-1]
        if not linha: break
        newl = linha.replace('[','').replace(']','')
        newl = newl.split(';')
        newl[2] = newl[2].split(',')
        newl[4] = newl[4].split(',')
        newl[6] = newl[6].split(',')
        newl[8] = newl[8].split(',')
        newl[10] = newl[10].split(',')
        cartela = {newl[0]:{newl[1]:newl[2],
                               newl[3]:newl[4],
                               newl[5]:newl[6],
                               newl[7]:newl[8],
                               newl[9]:newl[10]}}
        dicionario.update(cartela)
    return(True,dicionario)



def ImprimirCartelas(IDcartela: str):
    Cartelas = LerCartelas()[1]
    if not isinstance(Cartelas, dict) or len(Cartelas)<1:
        raise Exception('As cartelas não estão carregadas')
    if not isinstance(IDcartela, str):
        raise Exception('Informe um valor válido...')
    
    if(len(IDcartela)>6):
        if("CART_" in IDcartela and IDcartela in Cartelas):
            return(True,Cartelas[IDcartela])
    elif(len(IDcartela)<=6):
        IDcartela = "CART_" + (6-len(IDcartela))* "0" + IDcartela
        if(IDcartela in Cartelas):
            return(True,Cartelas[IDcartela],IDcartela)
    return(False,'ID informado errado')