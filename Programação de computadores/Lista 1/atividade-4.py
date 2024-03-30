import sys
DD1 = int(input("Informe o dia da primeira data: "))
DM1 = int(input("Informe o mês da primeira data: "))
DD2 = int(input("Informe o dia da segunda data: "))
DM2 = int(input("Informe o mês da segunda data: "))
#Número de dias de cada mês de um ano não bissexto
#1  janeiro 31 
#2  fevereiro 28
#3  março 31
#4  abril 30
#5  maio 31
#6  junho 30
#7  julho 31
#8  agosto 31
#9  setembro 30
#10 outubro 31
#11 novembro 30
#12 dezembro 31
if(DM2 < DM1):
    print('A segunda data é mais recente que a primeira')
    sys.exit()
elif(DD2 < DD1 and DM2 == DM1):
    print('A segunda data é mais recente que a primeira')
    sys.exit()
elif(DD2 == DD1 and DM2 == DM1):
    print('Ambas são as mesma data')
    sys.exit()
if(DD1 < 1):
    print('Dia inválido.')
    sys.exit()
elif(DD1 > 31 and (DM1 == 1 or DM1 == 3 or DM1 == 5 or DM1 == 7 or DM1 == 8 or DM1 == 10 or DM1 == 12)):
    print('Dia inválido.')
    sys.exit()
elif(DD1 > 30 and (DM1 == 4 or DM1 == 6 or DM1 == 9 or DM1 == 11)):
    print('Dia inválido.')
    sys.exit()
elif(DD1 > 28 and DM1 == 2):
    print('Dia inválido.')
    sys.exit()
if(DD2 < 1):
    print('Dia inválido.')
    sys.exit()
elif(DD2 > 31 and (DM2 == 1 or DM2 == 3 or DM2 == 5 or DM2 == 7 or DM2 == 8 or DM2 == 10 or DM2 == 12)):
    print('Dia inválido.')
    sys.exit()
elif(DD2 > 30 and (DM2 == 4 or DM2 == 6 or DM2 == 9 or DM2 == 11)):
    print('Dia inválido.')
    sys.exit()
elif(DD2 > 28 and DM2 == 2):
    print('Dia inválido.')
    sys.exit()
if(DM1 == 1):
    #334
    Dias1 = 31 - DD1 + 334
elif(DM1 == 2):
    #306
    Dias1 = 28 - DD1 + 306
elif(DM1 == 3):
    #275
    Dias1 = 31 - DD1 + 275
elif(DM1 == 4):
    #245
    Dias1 = 30 - DD1 + 245
elif(DM1 == 5):
    #214
    Dias1 = 31 - DD1 + 214
elif(DM1 == 6):
    #184
    Dias1 = 30 - DD1 + 184
elif(DM1 == 7):
    #153
    Dias1 = 31 - DD1 + 153
elif(DM1 == 8):
    #122
    Dias1 = 31 - DD1 + 122
elif(DM1 == 9):
    #92
    Dias1 = 30 - DD1 + 92
elif(DM1 == 10):
    #61
    Dias1 = 31 - DD1 + 61
elif(DM1 == 11):
    #31
    Dias1 = 30 - DD1 + 31
elif(DM1 == 12):
    Dias1 = 31 - DD1
else:
    print('mês inexistente')
if(DM2 == 1):
    #334
    Dias2 = 31 - DD2 + 334
elif(DM2 == 2):
    #306
    Dias2 = 28 - DD2 + 306
elif(DM2 == 3):
    #275
    Dias1 = 31 - DD2 + 275
elif(DM2 == 4):
    #245
    Dias2 = 30 - DD2 + 245
elif(DM2 == 5):
    #214
    Dias2 = 31 - DD2 + 214
elif(DM2 == 6):
    #184
    Dias2 = 30 - DD2 + 184
elif(DM2 == 7):
    #153
    Dias2 = 31 - DD2 + 153
elif(DM2 == 8):
    #122
    Dias2 = 31 - DD2 + 122
elif(DM2 == 9):
    #92
    Dias2 = 30 - DD2 + 92
elif(DM2 == 10):
    #61
    Dias2 = 31 - DD2 + 61
elif(DM2 == 11):
    #31
    Dias2 = 30 - DD2 + 31
elif(DM2 == 12):
    Dias2 = 31 - DD2
else:
    print('mês inexistente')
print(f'A diferença de dias é de {Dias1 - Dias2}')