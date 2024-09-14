import random
import sys
import fATV3
dictCartelas = dict()
while True:
    print('1. Gerar Cartela')
    print('2. Salvar Cartela')
    print('3. Ler Cartelas')
    print('4. Imprimir Cartela')
    print('5. Sair do programa')
    valor = int(input('informe a opção:'))
    if (valor == 1):
        quantia = int(input('Quantas cartelas?: '))    
        dictCartelas = fATV3.QCartelas(quantia)
        dictCartelas = dictCartelas[1]
        for x in dictCartelas:
            print(x)
    elif (valor == 2):
        print(fATV3.SCartelas(dictCartelas))
    elif(valor == 3):
        dictCartelas = fATV3.LerCartelas()[1]
        for x in dictCartelas:
            print(x,dictCartelas[x])
    elif(valor == 4):
        NomeCartela = input("Identificação da Cartela: ")
        imprimircartela = fATV3.ImprimirCartelas(NomeCartela)
        cartelaimpressa = imprimircartela[1]
        NCartela = imprimircartela[2]
        print( '+----+----+----+----+----+')
        print(f'| {NCartela}            |')
        print( '+----+----+----+----+----+')
        print( '|  B |  I |  N |  G |  O |')
        print( '+----+----+----+----+----+')
        print('| ',end='')
        for x in range(0,5):
            if (int(cartelaimpressa['B'][x]) < 10):
                print(" "+ cartelaimpressa['B'][x],end='')
            else:
                print(cartelaimpressa['B'][x],end='')
            print(' |',end='')
        print()
        print( '+----+----+----+----+----+')
        print('| ',end='')
        for x in range(0,5):
            print(cartelaimpressa['I'][x],end='')
            print(' |',end='')
        print()
        print( '+----+----+----+----+----+')
        print('| ',end='')
        for x in range(0,5):
            print(cartelaimpressa['N'][x],end='')
            print(' |',end='')
        print()
        print( '+----+----+----+----+----+')
        print('| ',end='')
        for x in range(0,5):
            print(cartelaimpressa['G'][x],end='')
            print(' |',end='')
        print()
        print( '+----+----+----+----+----+')
        print('| ',end='')
        for x in range(0,5):
            print(cartelaimpressa['O'][x],end='')
            print(' |',end='')
        print()
        print( '+----+----+----+----+----+')
        
    elif (valor == 5):
        break